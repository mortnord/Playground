import arcade

INVENTORY_SCALING = 2  # Konstant for størrelse


class InventoryPosition:
    def __init__(self, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY


class Inventory:
    def __init__(self):
        self.InventoryContents = []
        pass
    def append_to_inventory(self, ItemObjektToAppend):
        self.InventoryContents.append(ItemObjektToAppend)
        pass
    def inventory_position(self):
        pass
