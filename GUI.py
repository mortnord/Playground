import arcade
import Link
import Walls


class LonLonRanch(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        Walls.setup_walls(self)
        Link.setup_link(self)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.coin_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = Link.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -Link.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -Link.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = Link.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
