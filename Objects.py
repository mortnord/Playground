import random

import arcade

import Link

COIN_COUNT = 0
SPRITE_SCALING_COIN = 0.1


def setup_coins(self):
    self.coin_list = arcade.SpriteList()
    # Create the coins
    for i in range(COIN_COUNT):
        # Create the coin instance
        # Coin image from kenney.nl
        coin = arcade.Sprite("Sprites/coin_01.png", SPRITE_SCALING_COIN)

        # Position the coin
        coin.center_x = random.randrange(600)
        coin.center_y = random.randrange(600)
        # Add the coin to the lists
        self.coin_list.append(coin)
