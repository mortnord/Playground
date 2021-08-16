import arcade

from Inventory import Inventory
from MainCharacters import MainCharacters



class Malon(MainCharacters):
    SPRITE_SCALING_PLAYER = 2
    PLAYER_MOVEMENT_SPEED = 3
    def __init__(self):

        # Lager spriteListen som skal tegnes
        self.player_list = arcade.SpriteList()
        # start Liv
        self.health = 12
        # Lager Inventory til Link
        self.inventory_character = Inventory()
        # Kobler sprite .pngen til koden
        self.player_sprite = arcade.Sprite("Sprites/Malon.png", self.SPRITE_SCALING_PLAYER)
        # startposisjon
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 50
        # Legger til for å tegnes
        self.player_list.append(self.player_sprite)
        self.show_inventory = False
