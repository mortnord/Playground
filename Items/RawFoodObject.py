import arcade

from Items.FoodObject import FoodObject


# Ett RawFoodObjekt skal brukes når man ønsker ett raw food (type carrot osv), den har healing verdi, sprite og er ett
# vanlig objekt i verdenen.
class RawFoodObject(FoodObject):
    def __init__(self, weight, name, type_object, raw_food_type, healing_value, spesific_objekt):
        self.weight = weight
        self.name = name
        self.type_object = type_object
        self.raw_food_type = raw_food_type
        self.healing_value = healing_value
        self.spesific_object = spesific_objekt

    def get_raw_food_type(self):
        return self.raw_food_type

