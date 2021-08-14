from Items.GenericObject import GenericObject


class FoodObject(GenericObject):
    def __init__(self, weight, name, healing_value):
        self.weight = weight
        self.name = name
        self.healing_value = healing_value

    def get_healing_value(self):
        return self.healing_value
