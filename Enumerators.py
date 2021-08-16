from enum import Enum


class Veggies(Enum):  # Liste over mulige veggies, og en fellesbenevnelse
    Carrot = 1
    Rutabaga = 2


class Icons(Enum):  # Liste over sprites til forskjellige verdier, kan kalle f.eks Icons.Carrot.Value for å
    # få spriten til Carrot
    Carrot = "Sprites/Carrot.png"
    Rutabaga = "Sprites/Rutabaga.png"


class TypeOfObject(Enum):  # Liste over type objekt
    Food = 1
