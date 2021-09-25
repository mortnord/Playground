import arcade

from Inventory import Inventory
from MainCharacters import MainCharacters


class LinkCharacter(MainCharacters):
    SPRITE_SCALING_PLAYER = 0.05  # Konstant med skalering av størrelse

    # noinspection PyMissingConstructor
    def __init__(self):
        # starter Liv
        self.health = 12
        # Lager Inventory til Link
        self.inventory_character = Inventory(arcade.csscolor.YELLOW)
        # Kobler sprite .pngen til koden
        self.player_sprite = arcade.Sprite("Sprites/Link.png", self.SPRITE_SCALING_PLAYER)
        # startposisjon
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 250
        #flag for å sjekke om inventory skal vises
        self.show_inventory = False

        self.PLAYER_MOVEMENT_SPEED = self.PLAYER_MOVEMENT_SPEED * 3  # Konstant med fart i bevegelse

        #Testing
        #Ekstra test

# https://api.arcade.academy/en/latest/examples/platform_tutorial/step_01.html
