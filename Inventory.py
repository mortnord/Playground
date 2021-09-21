import arcade

INVENTORY_SCALING = 2  # Konstant for størrelse


class InventoryPosition:
    def __init__(self, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY


class Inventory:
    InventoryContents = []
    def __init__(self):
        pass
    def append_to_inventory(self, ItemObjektToAppend):
        self.InventoryContents.append(ItemObjektToAppend)
        pass

