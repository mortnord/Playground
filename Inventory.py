
class Inventory:
    def __init__(self):
        self.inventory_contents = list()

    def get_inventory_contents(self):
        return self.inventory_contents

    def append_to_inventory(self, object_to_append):
        self.inventory_contents.append(object_to_append)
