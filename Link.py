import arcade

from Inventory import Inventory
from MainCharacters import MainCharacters


class LinkCharacter(MainCharacters):
    SPRITE_SCALING_PLAYER = 0.05  # Konstant med skalering av størrelse
    PLAYER_MOVEMENT_SPEED = 3  # Konstant med fart i bevegelse

    # noinspection PyMissingConstructor
    def __init__(self):
        # Lager spriteListen som skal tegnes
        self.player_list = arcade.SpriteList()
        # starter Liv
        self.health = 12
        # Lager Inventory til Link
        self.inventory_character = Inventory()
        # Kobler sprite .pngen til koden
        self.player_sprite = arcade.Sprite("Sprites/Link.png", self.SPRITE_SCALING_PLAYER)
        # startposisjon
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        # Legger til for å tegnes
        self.player_list.append(self.player_sprite)
        self.show_inventory = False

# https://api.arcade.academy/en/latest/examples/platform_tutorial/step_01.html
