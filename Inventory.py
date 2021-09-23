import arcade

INVENTORY_SCALING = 2  # Konstant for størrelse


class SpritePosition:
    def __init__(self, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY


class Inventory:
    def __init__(self):
        self.inventory_contents_sprite_list_position = []
        self.inventory_sprite = arcade.Sprite("Sprites/Inventory V1.png", INVENTORY_SCALING)
        self.inventory_sprite_list = arcade.SpriteList()
        self.inventory_sprite_list.append(self.inventory_sprite)
        self.InventoryContents = []
        self.setup_sprite_position()

    def append_to_inventory(self, ItemObjektToAppend):
        self.InventoryContents.append(ItemObjektToAppend)
        pass

    def inventory_position(self, view_left, view_bottom):
        self.inventory_sprite.center_x = view_left + 400
        self.inventory_sprite.center_y = view_bottom + 250
        pass

    def setup_sprite_position(self):  # TODO Endre på.
        for x in range(8):
            try:
                if x <= 3:
                    Pos = SpritePosition(self.inventory_sprite.top - 15, self.inventory_sprite.left + (x * 31) + 18)
                    self.inventory_contents_sprite_list_position.append(Pos)
                elif x >= 4:
                    Pos = SpritePosition(self.inventory_sprite.top - 45, (x * 31) + 18 - 124)
                    self.inventory_contents_sprite_list_position.append(Pos)
            except IndexError:
                print("ERROR")
