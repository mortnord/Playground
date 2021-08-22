import arcade

import GUI

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
game = GUI.LonLonRanch(SCREEN_WIDTH, SCREEN_HEIGHT, "Lon Lon Ranch")
game.setup()
arcade.run()
