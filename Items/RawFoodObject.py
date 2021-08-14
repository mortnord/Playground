from Items.FoodObject import FoodObject


class RawFoodObject(FoodObject):
    def __init__(self, weight, name, raw_food_type, healing_value):
        self.weight = weight
        self.name = name
        self.raw_food_type = raw_food_type
        self.healing_value = healing_value

    def get_type(self):
        return self.raw_food_type

