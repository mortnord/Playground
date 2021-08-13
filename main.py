import arcade

import GUI as GUI

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

game = GUI.MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
game.setup()
arcade.run()
