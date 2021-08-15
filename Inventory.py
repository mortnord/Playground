import arcade

INVENTORY_SCALING = 2


class Inventory:
    def __init__(self):
        self.inventory_contents = list()
        self.inventory_list = arcade.SpriteList()
        self.inventory_contents_sprite_list = arcade.SpriteList()
        # Kobler sprite .pngen til koden
        self.inventory_sprite = arcade.Sprite("Sprites/Inventory V1.png", INVENTORY_SCALING)
        # startposisjon
        self.inventory_sprite.center_x = 250
        self.inventory_sprite.center_y = 250
        # Legger til for å tegnes
        self.inventory_list.append(self.inventory_sprite)
        self.items_in_food_inventory = 0

    def update_contents(self):
        # if len(self.inventory_contents) >= 1:
        #     try:
        #         self.inventory_contents_sprite_list.append(self.inventory_contents[0].icon)
        #     except IndexError:
        #         pass  # print("tomt for carrots å tegne")

        try:
            self.inventory_contents_sprite_list.append(self.inventory_contents[self.items_in_food_inventory].icon)
            self.items_in_food_inventory = self.items_in_food_inventory + 1
        except IndexError:
            pass

    def reorder_contents(self):
        for x in range(len(self.inventory_contents)):
            print(len(self.inventory_contents))
            try:
                if x <= 3:
                    self.inventory_contents[x].icon.center_y = self.inventory_sprite.top - 15
                    self.inventory_contents[x].icon.center_x = self.inventory_sprite.left + (x * 31) + 18
                elif x >= 4:
                    self.inventory_contents[x].icon.center_y = self.inventory_sprite.top - 45
                    self.inventory_contents[x].icon.center_x = self.inventory_sprite.left + (x * 31) + 18 - 124
            except IndexError:
                pass

    def get_inventory_contents(self):
        return self.inventory_contents

    def append_to_inventory(self, object_to_append):

        self.inventory_contents.append(object_to_append)
        self.update_contents()
        self.reorder_contents()

    def update_position(self):
        print(self.inventory_sprite.left)
        print(self.inventory_sprite.top)
        pass
