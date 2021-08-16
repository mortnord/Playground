import arcade

import Camera
import Link
import Malon
import SetupObjects
import UI
import Walls
# Dtte er enkle imports for at det skal få tilgang til de andre filene
# self referer til seg selv, slik at det er objektet som kaller koden på seg selv, om seg selv.
from Enumerators import TypeOfObject


# Her henter jeg inn enumerators, en slags fast verdi som jeg kan referere til en plass, og bruke andre plasser.

def swapPositions(list_to_be_swapped, pos1, pos2):
    # popping both the elements from list_to_be_swapped
    first_ele = list_to_be_swapped.pop(pos1)
    second_ele = list_to_be_swapped.pop(pos2 - 1)

    # inserting in each others positions
    list_to_be_swapped.insert(pos1, second_ele)
    list_to_be_swapped.insert(pos2, first_ele)


class LonLonRanch(arcade.Window):
    """ Main application class. """
    link_character = 0
    malon_character = 0
    inventory_show = False

    view_bottom = 0
    view_left = 0

    # Dette er konstruktøren til Classen LonLonRanch, som arver fra Window classen i Arcade.
    def __init__(self, width, height, title):
        # Her caller vi super-classen (den vi arver fra), sin __init__ metode, for å starte opp tegningen av vinduet.
        super().__init__(width, height, title, resizable=True)
        # Setter bakgrunnen
        self.characters = list()
        arcade.set_background_color(arcade.color.AMAZON)
        # Setter hjørne for kamera
        self.view_bottom = 0
        self.view_left = 0

    # Setup kalles 1 gang i Main.Py, for å sette opp vinduet.
    def on_resize(self, width: float, height: float):
        super().on_resize(width, height)

    def setup(self):

        Walls.setup_walls(self)  # Først lager vi veggene, som våre sprites kan krasje i

        self.link_character = Link.LinkCharacter()  # Her generer vi link karakteren
        self.malon_character = Malon.Malon()  # Her generer vi malon karakteren
        self.characters.append(
            self.link_character)  # Her legger vi begge characters inn i lista over spillbare characters
        self.characters.append(self.malon_character)
        SetupObjects.setup_objects()  # Her kobler vi .png med objektene vi kan ha i inventory, slik at de blir loadet når spillet starter.
        self.physics_engine = arcade.PhysicsEngineSimple(self.link_character.player_sprite,
                                                         self.wall_list)  # Her setter vi fysikkenginene som driver collisions og annet
        self.physics_engine1 = arcade.PhysicsEngineSimple(self.malon_character.player_sprite, self.wall_list)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        UI.draw_UI(self, self.characters)  # Vi tegner UI
        for x in range(
                len(self.characters)):  # Her tegner vi begge characters, og for begge characters, vis inventory skal vises tegn inventory. TODO: Split inventory slik at 1 person kan åpne den om gangen
            self.characters[x].player_list.draw()
            if self.characters[x].show_inventory:
                self.characters[x].inventory_character.inventory_list.draw()
                self.characters[x].inventory_character.inventory_contents_sprite_list.draw()

        self.wall_list.draw()  # Her tegner vi veggene

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """

        ## hit_collision_detected_list = arcade.check_for_collision_with_list(self.characters[0].player_list[0], self.wall_list)

        self.physics_engine.update()  # Oppdater fysikk
        self.physics_engine1.update()

        Camera.update_camera(self, self.characters[0])  # Oppdater kamera

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W:  # WASD eller piltast bevegelse
            self.characters[0].player_list[0].change_y = self.characters[0].PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.characters[0].player_list[0].change_y = -self.characters[0].PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.characters[0].player_list[0].change_x = -self.characters[0].PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.characters[0].player_list[0].change_x = self.characters[0].PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.E:  # Denne er mer komplisert, først sjekk om siste lagt inn object i inventory er food,
            # og vis det er, så få liv avhengig av hvor mye healing value til objektet er.
            # Så reduser mengden food i inventory med 1, og fjern objektet fra tegnelista.
            ## TODO: split inventory i flere biter, og kun sjekk food inventory
            try:
                if self.characters[0].inventory_character.get_inventory_contents()[0].get_type_object() == TypeOfObject.Food:
                    self.characters[0].gain_health(
                        self.characters[0].inventory_character.get_inventory_contents().pop().get_healing_value())
                    print("Gulrot spist")
                    self.characters[0].inventory_character.items_in_food_inventory = self.characters[
                                                                                   0].inventory_character.items_in_food_inventory - 1
                    self.characters[0].inventory_character.inventory_contents_sprite_list.pop()
            except IndexError:  # Feilhåndtering vis tomt for food
                print("Out of carrots")
        elif key == arcade.key.Q:  # Midlertidig test for å miste liv
            self.characters[0].lose_health(3)
        elif key == arcade.key.G:  # Denne er også komplisert, denne sjekker først om inventory er mindre enn 8, og vis
            # det er, så legg til en nylig generert RawFoodObjekt med verdiene til en carrot

            if self.characters[0].inventory_character.items_in_food_inventory <= 7:
                self.characters[0].inventory_character.append_to_inventory(SetupObjects.create_carrot())
                print("Gulrot generert")
            else:
                print("Food inventory fult")
        elif key == arcade.key.R:  # Denne gjør som gulrot-koden, bare med kålrabi istedenfor
            if self.characters[0].inventory_character.items_in_food_inventory <= 7:

                self.characters[0].inventory_character.append_to_inventory(SetupObjects.create_rutabaga())
                print("Rutabaga generert")
            else:
                print("Food inventory fult")
        elif key == arcade.key.I:  # Dette er ett flag om inventory skal tegnes eller ikke
            if not self.characters[0].show_inventory:  # Nå tegnes inventory for hver character spesifikt
                self.characters[0].show_inventory = True
            elif self.characters[0].show_inventory:
                self.characters[0].show_inventory = False
        elif key == arcade.key.SPACE:  # Denne bytter plass med hvem som er hovedperson og hvem som ikke er. Uelegant
            swapPositions(self.characters, 0, 1)

    def on_key_release(self, key, modifiers):  # Her sjekker vi om knappene er blitt releaset, for å stoppe å bevege seg
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
