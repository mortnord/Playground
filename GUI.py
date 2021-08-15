import arcade
import Camera
import Link
import Malon
import Objects
import SetupObjects
import UI
import Walls

# Dtte er enkle imports for at det skal få tilgang til de andre filene
# self referer til seg selv, slik at det er objektet som kaller koden på seg selv, om seg selv.
from Enumerators import Veggies, Icons
from Items.RawFoodObject import RawFoodObject


class LonLonRanch(arcade.Window):
    """ Main application class. """
    link_character = 0
    malon_character = 0
    inventory_show = False

    view_bottom = 0
    view_left = 0
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
        self.malon_character = Malon.Malon()
        self.characters.append(self.link_character)
        self.characters.append(self.malon_character)
        Objects.setup_coins(self)
        SetupObjects.setup_objects()
        self.physics_engine = arcade.PhysicsEngineSimple(self.link_character.player_sprite, self.wall_list)
        self.physics_engine1 = arcade.PhysicsEngineSimple(self.malon_character.player_sprite, self.wall_list)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        UI.draw_UI(self, self.characters)
        self.coin_list.draw()
        for x in range(len(self.characters)):
            self.characters[x].player_list.draw()
            if self.inventory_show:
                self.characters[x].InventoryLink.inventory_list.draw()
                self.characters[x].InventoryLink.inventory_contents_sprite_list.draw()

        self.wall_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.physics_engine.update()
        self.physics_engine1.update()
        Camera.update_camera(self, self.link_character)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.characters[0].player_list[0].change_y = self.characters[0].PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.characters[0].player_list[0].change_y = -self.characters[0].PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.characters[0].player_list[0].change_x = -self.characters[0].PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.characters[0].player_list[0].change_x = self.characters[0].PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.E:
            try:
                if self.characters[0].InventoryLink.get_inventory_contents()[0].get_type() == Veggies:
                    self.characters[0].gain_health(self.characters[0].InventoryLink.get_inventory_contents().pop().get_healing_value())
                    print("Gulrot spist")
                    self.characters[0].InventoryLink.items_in_food_inventory = self.characters[0].InventoryLink.items_in_food_inventory - 1
                    self.characters[0].InventoryLink.inventory_contents_sprite_list.pop()
            except IndexError:
                print("Out of carrots")
        elif key == arcade.key.Q:
            self.characters[0].lose_health(3)
        elif key == arcade.key.G:
            if len(self.characters[0].InventoryLink.inventory_contents) <= 7:
                self.characters[0].InventoryLink.append_to_inventory(RawFoodObject(0.1, "Gulrot", Veggies, 3, Icons.Carrot.value))
                print("Gulrot generert")
            else:
                print("Food inventory fult")
        elif key == arcade.key.R:
            if len(self.characters[0].InventoryLink.inventory_contents) <= 7:
                self.characters[0].InventoryLink.append_to_inventory((RawFoodObject(0.1, "Rutabaga", Veggies, 5, Icons.Rutabaga.value)))
                print("Rutabaga generert")
            else:
                print("Food inventory fult")
        elif key == arcade.key.I:
            if self.inventory_show:
                self.inventory_show = False
            elif not self.inventory_show:
                self.inventory_show = True
        elif key == arcade.key.SPACE:
            self.swapPositions(self.characters, 0, 1)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.characters[0].player_list[0].change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.characters[0].player_list[0].change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.characters[0].player_list[0].change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.characters[0].player_list[0].change_x = 0
        elif key == arcade.key.SPACE:
            self.characters[0].player_list[0].change_x = 0
            self.characters[0].player_list[0].change_y = 0

            self.characters[1].player_list[0].change_y = 0
            self.characters[1].player_list[0].change_x = 0

    # Swap function
    def swapPositions(self, list, pos1, pos2):
        # popping both the elements from list
        first_ele = list.pop(pos1)
        second_ele = list.pop(pos2 - 1)

        # inserting in each others positions
        list.insert(pos1, second_ele)
        list.insert(pos2, first_ele)


