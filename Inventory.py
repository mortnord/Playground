import arcade

INVENTORY_SCALING = 2  # Konstant for størrelse


class InventoryPosition:
    def __init__(self, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY


class Inventory:
    def __init__(self):
        self.inventory_sprite = arcade.Sprite("Sprites/Inventory V1.png", INVENTORY_SCALING)
        self.inventory_sprite_list = arcade.SpriteList()
        self.inventory_sprite_list.append(self.inventory_sprite)
        self.InventoryContents = []

    def append_to_inventory(self, ItemObjektToAppend):
        self.InventoryContents.append(ItemObjektToAppend)
        pass

    def inventory_position(self, view_left, view_bottom):
        self.inventory_sprite.center_x = view_left + 400
        self.inventory_sprite.center_y = view_bottom + 250
        pass
