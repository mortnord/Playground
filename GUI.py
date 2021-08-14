import arcade
import Camera
import Link
import Objects
import UI
import Walls

# Dtte er enkle imports for at det skal få tilgang til de andre filene
# self referer til seg selv, slik at det er objektet som kaller koden på seg selv, om seg selv.
from Enumerators import Veggies
from Items.RawFoodObject import RawFoodObject


class LonLonRanch(arcade.Window):
    """ Main application class. """
    link_character = 0

    # Dette er konstruktøren til Classen LonLonRanch, som arver fra Window classen i Arcade.
    def __init__(self, width, height):
        # Her caller vi super-classen (den vi arver fra), sin __init__ metode, for å starte opp tegningen av vinduet.
        super().__init__(width, height)
        # Setter bakgrunnen
        self.characters = list()
        arcade.set_background_color(arcade.color.AMAZON)
        # Setter hjørne for kamera
        self.view_bottom = 0
        self.view_left = 0

    # Setup kalles 1 gang i Main.Py, for å sette opp vinduet.
    def setup(self):

        # Her kaller vi de 3 metodene i de 3 forskjellige .py filene,for å ha orden i koden, og ikke en veldig lang fil.
        Walls.setup_walls(self)
        self.link_character = Link.LinkCharacter()
        self.characters.append(self.link_character)
        Objects.setup_coins(self)

        self.physics_engine = arcade.PhysicsEngineSimple(self.link_character.player_sprite, self.wall_list)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        UI.draw_UI(self, self.link_character)
        self.coin_list.draw()
        self.link_character.player_list.draw()
        self.wall_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.physics_engine.update()
        Camera.update_camera(self, self.link_character)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.characters[0].player_list[0].change_y = Link.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.characters[0].player_list[0].change_y = -Link.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.characters[0].player_list[0].change_x = -Link.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.characters[0].player_list[0].change_x = Link.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.E:
            try:
                if self.link_character.InventoryLink.get_inventory_contents()[0].get_type() == Veggies.Carrot:
                    self.link_character.gain_health(
                        self.link_character.InventoryLink.get_inventory_contents().pop().get_healing_value())
                    print("Gulrot spist")
                    print(len(self.link_character.InventoryLink.get_inventory_contents()))
            except IndexError:
                print("Out of carrots")
        elif key == arcade.key.Q:
            self.link_character.lose_health(3)
        elif key == arcade.key.G:

            gulrot1 = RawFoodObject(0.1, "Gulrot", Veggies.Carrot, 3)
            self.link_character.InventoryLink.append_to_inventory(gulrot1)
            print(self.link_character.InventoryLink.get_inventory_contents()[0].get_name())

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.characters[0].player_list[0].change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.characters[0].player_list[0].change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.characters[0].player_list[0].change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.characters[0].player_list[0].change_x = 0
