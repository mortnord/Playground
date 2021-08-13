import random

import arcade

SPRITE_SCALING_PLAYER = 0.1
COIN_COUNT = 20
SPRITE_SCALING_COIN = 0.1

# https://api.arcade.academy/en/latest/examples/platform_tutorial/step_01.html
def setup(self):
    """ Set up the game and initialize the variables. """

    # Create the sprite lists
    self.player_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()

    # Score
    self.score = 0

    # Set up the player
    # Character image from kenney.nl
    self.player_sprite = arcade.Sprite("Sprites/Link.png", SPRITE_SCALING_PLAYER)
    self.player_sprite.center_x = 50  # Starting position
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)

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
