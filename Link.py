import arcade

from Inventory import Inventory

SPRITE_SCALING_PLAYER = 0.05
PLAYER_MOVEMENT_SPEED = 3


class LinkCharacter():
    def __init__(self):
        #Lager spriteListen som skal tegnes
        self.player_list = arcade.SpriteList()
        #start Liv
        self.health = 12
        #Lager Inventory til Link
        self.InventoryLink = Inventory()
        #Kobler sprite .pngen til koden
        self.player_sprite = arcade.Sprite("Sprites/Link.png", SPRITE_SCALING_PLAYER)
        #startposisjon
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        #Legger til for å tegnes
        self.player_list.append(self.player_sprite)

    def lose_health(self, amount):
        #Metoden man kaller for å miste liv
        self.health = self.health - amount
        pass

    def gain_health(self, amount):
        #Metoden man kaller for å få liv
        self.health = self.health + amount
        pass


# https://api.arcade.academy/en/latest/examples/platform_tutorial/step_01.html


