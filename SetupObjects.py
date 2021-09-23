from Enumerators import Veggies, Icons, TypeOfObject
from InventoryObject import InventoryObject
from Items.RawFoodObject import RawFoodObject


def setup_objects():  # Denne metoden kalles i starten, for å laste inn .pnger og å være klær til å lage nye objekter.
    RawFoodObject(0.1, "Gulrot", TypeOfObject.Food, Veggies, 3, Icons.Carrot.value)
    RawFoodObject(0.1, "Rutabaga", TypeOfObject.Food, Veggies, 5, Icons.Rutabaga.value)


def create_rutabaga():  # Denne koden returnerer en ny kålrabi, dette gjør at koden for å endre en kålrabi kun er 1 plass
    return InventoryObject(RawFoodObject(0.1, "Rutabaga", TypeOfObject.Food, Veggies, 5, Icons.Rutabaga.value), SpritePosition=(0,0))


def create_carrot(): #  Samme som ovenfor, bare gulrot
    return InventoryObject(RawFoodObject(0.1, "Gulrot", TypeOfObject.Food, Veggies, 3, Icons.Carrot.value), SpritePosition=(0,0))
