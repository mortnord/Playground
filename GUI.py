import arcade
import Link


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        Link.setup(self)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.coin_list.draw()

        self.player_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass
