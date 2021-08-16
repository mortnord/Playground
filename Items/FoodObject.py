from Items.GenericObject import GenericObject


# Ett food objekt er spisbart, men er egentlig ikke meningen det skal bruks, men kun arve metoder fra.
class FoodObject(GenericObject):
    def __init__(self, weight, name, type_object, healing_value):
        self.weight = weight
        self.name = name
        self.type_object = type_object
        self.healing_value = healing_value

    def get_healing_value(self):
        return self.healing_value
