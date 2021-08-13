import arcade

import GUI

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

game = GUI.MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
game.setup()
arcade.run()
