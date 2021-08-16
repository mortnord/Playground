import arcade

from Items.FoodObject import FoodObject


# Ett RawFoodObjekt skal brukes når man ønsker ett raw food (type carrot osv), den har healing verdi, sprite og er ett
# vanlig objekt i verdenen.
class RawFoodObject(FoodObject):
    def __init__(self, weight, name, type_object, raw_food_type, healing_value, icon):
        self.weight = weight
        self.name = name
        self.type_object = type_object
        self.raw_food_type = raw_food_type
        self.healing_value = healing_value
        self.icon = arcade.Sprite(icon, 0.04)

    def get_raw_food_type(self):
        return self.raw_food_type

    def get_icon(self):
        return self.icon
