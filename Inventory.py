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

    def update_contents(self):
        try:
            self.inventory_contents_sprite_list.append(self.inventory_contents[0].icon)
            self.inventory_contents[0].icon.center_y = 250
            self.inventory_contents[0].icon.center_x = 250
        except IndexError:
           pass # print("tomt for carrots å tegne")

    def get_inventory_contents(self):
        return self.inventory_contents

    def append_to_inventory(self, object_to_append):
        self.inventory_contents.append(object_to_append)

    def update_position(self):
        pass
