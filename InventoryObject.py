import arcade


class InventoryObject(arcade.Sprite):
    ItemObjekt = 0
    InventoryNumber = int(0)

    def __init__(self, ItemObjekt, Icon):
        self.ItemObjekt = ItemObjekt

        self.image_file_name = Icon
        super().__init__(self.image_file_name, scale=1, hit_box_algorithm="None")

    def setItemNumber(self, number):
        self.InventoryNumber = number

    def getItemNumber(self):
        return self.InventoryNumber
