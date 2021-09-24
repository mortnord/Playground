class InventoryObject:
    ItemObjekt = 0
    SpritePosition = 0
    InventoryNumber = int(0)
    def __init__(self, ItemObjekt, SpritePosition):
        self.ItemObjekt = ItemObjekt
        self.SpritePosition = SpritePosition

    def setItemNumber(self, number):
        self.InventoryNumber = number

    def getItemNumber(self):
        return self.InventoryNumber

