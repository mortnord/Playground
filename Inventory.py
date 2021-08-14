
class Inventory:
    def __init__(self):
        self.InventoryContents = list()

    def get_Inventory_Contents(self):
        return self.InventoryContents

    def append_to_inventory(self, object_to_append):
        self.InventoryContents.append(object_to_append)
