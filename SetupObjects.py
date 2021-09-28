from Enumerators import Veggies, Icons, TypeOfObject
from InventoryObject import InventoryObject
from Items.RawFoodObject import RawFoodObject

identification_variable = 0
def setup_objects():  # Denne metoden kalles i starten, for å laste inn .pnger og å være klær til å lage nye objekter.
    RawFoodObject(0.1, "Gulrot", TypeOfObject.Food, Veggies, 3, Veggies.Carrot)
    RawFoodObject(0.1, "Rutabaga", TypeOfObject.Food, Veggies, 5, Veggies.Rutabaga)


def create_rutabaga():  # Denne koden returnerer en ny kålrabi, dette gjør at koden for å endre en kålrabi kun er 1 plass
    global identification_variable
    identification_variable = identification_variable + 1
    return InventoryObject(RawFoodObject(0.1, "Rutabaga", TypeOfObject.Food, Veggies, 5, Veggies.Rutabaga), Icons.Rutabaga.value, identification_variable)


def create_carrot(): #  Samme som ovenfor, bare gulrot
    global identification_variable
    identification_variable = identification_variable + 1
    return InventoryObject(RawFoodObject(0.1, "Gulrot", TypeOfObject.Food, Veggies, 3, Veggies.Carrot),Icons.Carrot.value, identification_variable)
