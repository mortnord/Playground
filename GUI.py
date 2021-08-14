import arcade
import Camera
import Link
import Objects
import Walls


# Dtte er enkle imports for at det skal få tilgang til de andre filene
# self referer til seg selv, slik at det er objektet som kaller koden på seg selv, om seg selv.
class LonLonRanch(arcade.Window):
    """ Main application class. """

    # Dette er konstruktøren til Classen LonLonRanch, som arver fra Window classen i Arcade.
    def __init__(self, width, height):
        # Her caller vi super-classen (den vi arver fra), sin __init__ metode, for å starte opp tegningen av vinduet.
        super().__init__(width, height)
        # Setter bakgrunnen
        arcade.set_background_color(arcade.color.AMAZON)
        # Setter hjørne for kamera
        self.view_bottom = 0
        self.view_left = 0

    # Setup kalles 1 gang i Main.Py, for å sette opp vinduet.
    def setup(self):
        # Her kaller vi de 3 metodene i de 3 forskjellige .py filene,for å ha orden i koden, og ikke en veldig lang fil.
        Walls.setup_walls(self)
        Link.setup_link(self)
        Objects.setup_coins(self)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.coin_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.physics_engine.update()
        Camera.update_camera(self)

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
