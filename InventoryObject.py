import arcade


class InventoryObject(arcade.Sprite):
    item_objekt = 0
    inventory_number = int(0)
    item_stack = 0
    identification_number = 0

    def __init__(self, ItemObjekt, Icon, ID_number):
        self.item_objekt = ItemObjekt
        self.identification_number = ID_number
        self.image_file_name = Icon
        super().__init__(self.image_file_name, scale=1, hit_box_algorithm="None")


