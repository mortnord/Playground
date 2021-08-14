from Items.GenericObject import GenericObject


class RawFoodObject(GenericObject):
    def __init__(self, weight, name, RawFoodType):
        self.weight = weight
        self.name = name
        self.RawFoodType = RawFoodType

    def get_type(self):
        return self.RawFoodType
