import arcade

import Camera
import Link
import Malon
import SetupObjects
import UI

from Enumerators import TypeOfObject

# Her importerer vi nødvendige filer, relativt sipelt

# Her setter vi de forskjellige layersa som tegnes på kartet, burde gjøres bedre
# TODO : Mindre hardcoding
from InventoryObject import InventoryObject
from Items.GenericObject import GenericObject

LAYER_NAME_BACKGROUND = "Bakke"
LAYER_NAME_DONT_TOUCH = "Gjerder"


def swapPositions(list_to_be_swapped, pos1, pos2):  # Denne funksjonen bytter plass på 2 objekter i den samme listen,
    # i vårt tilfelle så bytter den mellom hovedperson og ikke hovedperson

    first_ele = list_to_be_swapped.pop(pos1)
    second_ele = list_to_be_swapped.pop(pos2 - 1)

    list_to_be_swapped.insert(pos1, second_ele)
    list_to_be_swapped.insert(pos2, first_ele)


class LonLonRanch(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):

        super().__init__(width, height, title, resizable=True)


        #Her setter vi initial verdiene til variabler
        self.scene = None
        self.characters = list()
        self.view_bottom = 0
        self.view_left = 0

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.tile_map = None


    def on_resize(self, width: float, height: float):
        super().on_resize(width, height) ##Denne gjør at vi kan gjøre vinduet mindre og større

    def setup(self):

        self.scene = arcade.Scene() #Opprettet scene-objektet, som skal samle alt som skal tegnes hver gang.

        self.link_character = Link.LinkCharacter() ##Opprettelse av Link og Malon objektene
        self.malon_character = Malon.Malon()

        self.characters.append(self.link_character) #Her legger vi dem til i lista over karakter
        self.characters.append(self.malon_character)

        SetupObjects.setup_objects() # Her lager vi alle ting-objektene og laster in bilder.

        ##Dette er hva kart som skal lastes, #TODO : Mindre hardcoding
        map_name = "TiledMaps/Bakgroundskart_med_flisesett.json"

        # Layer specific options are defined based on Layer names in a dictionary
        # Doing this will make the SpriteList for the platforms layer
        # use spatial hashing for detection.

        layer_options = {
            LAYER_NAME_DONT_TOUCH: {
                "use_spatial_hash": True,
            },
        }

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(map_name, 1, layer_options)

        # Initialize Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        #Her lager vi en sprite list for spillbare karakterer
        self.scene.add_sprite_list("Players")
        #Her legger vi inn sprites i overnevnte liste
        self.scene.add_sprite("Players", self.malon_character.player_sprite)
        self.scene.add_sprite("Players", self.link_character.player_sprite)
        #Her sier vi hva fysikken skal håndtere, alså ikke krasj med denne listen med objekter
        self.physics_engine = arcade.PhysicsEngineSimple(self.link_character.player_sprite,
                                                         self.scene.get_sprite_list(
                                                             LAYER_NAME_DONT_TOUCH))
        self.physics_engine1 = arcade.PhysicsEngineSimple(self.malon_character.player_sprite,
                                                          self.scene.get_sprite_list(LAYER_NAME_DONT_TOUCH))

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render() #Denne tømmer bilde, og gjør klart for nytt bilde
        self.scene.draw()  ##Her tegnes alt som er lagt til i scene objektet.
        UI.draw_UI(self, self.characters)  #Her tegner vi UIet
        for x in range(len(self.characters)):  ##Her tegner vi inventory vis det skal vises på den karakteren.
            if self.characters[x].show_inventory:
                self.characters[x].inventory_character.inventory_sprite_list.draw()



    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """

        self.physics_engine.update() #Denne oppdater fysikken, og sjekker for kollisjoner osv
        self.physics_engine1.update()


        Camera.update_camera(self, self.characters[0]) #Denne flytter kamera etter hovedpersonen
        self.characters[0].inventory_character.inventory_position(self.view_left, self.view_bottom) #Denne flytter inventory etter hovedpersonen


    def process_keychange(self): ##Her håndterer vi hva retning vi skal gå med å sjekke hva knapper som er trykket inn
        if self.up_pressed and not self.down_pressed: #Opp, og ikke ned
            self.characters[0].player_sprite.change_y = self.characters[0].PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed: #Ned og ikke opp
            self.characters[0].player_sprite.change_y = -self.characters[0].PLAYER_MOVEMENT_SPEED
        else:
            self.characters[0].player_sprite.change_y = 0 #Intet

        if self.right_pressed and not self.left_pressed: #Høyre og ikke venstre
            self.characters[0].player_sprite.change_x = self.characters[0].PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed: #Venstre og ikke høyre
            self.characters[0].player_sprite.change_x = -self.characters[0].PLAYER_MOVEMENT_SPEED
        else:
            self.characters[0].player_sprite.change_x = 0 #Intet

    def on_key_press(self, key, modifiers): #Denne setter flag som matcher hva knapper som er trykket
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        self.process_keychange()

        if key == arcade.key.Q:  # Midlertidig test for å miste liv
            self.characters[0].lose_health(3)
        elif key == arcade.key.G:
            self.characters[0].inventory_character.append_to_inventory(SetupObjects.create_carrot())
            print("Gulrot generert")
        elif key == arcade.key.R:  # Denne gjør som gulrot-koden, bare med kålrabi istedenfor
            self.characters[0].inventory_character.append_to_inventory(SetupObjects.create_rutabaga())
            print("Rutabaga generert")
        elif key == arcade.key.I:
            if not self.characters[0].show_inventory:  # Nå tegnes inventory for hver character spesifikt
                self.characters[0].show_inventory = True
            elif self.characters[0].show_inventory:
                self.characters[0].show_inventory = False
            for x in range(len(self.characters[0].inventory_character.InventoryContents)):
                print(self.characters[0].inventory_character.InventoryContents[x].ItemObjekt.name)
            pass
            # Dette er ett flag om inventory skal tegnes eller ikke
        elif key == arcade.key.SPACE:  # Denne bytter plass med hvem som er hovedperson og hvem som ikke er. Uelegant
            swapPositions(self.characters, 0, 1)


    def on_key_release(self, key, modifiers): #Denne avflagger at knapper er trykket, slik at vi ikke får noen låste bevegelser osv
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

        self.process_keychange()
        if key == arcade.key.SPACE: #Denne stopper uansett begge personer når man trykker space, kanskje unødvendig
            self.characters[0].player_sprite.change_x = 0
            self.characters[0].player_sprite.change_y = 0
            self.characters[1].player_sprite.change_y = 0
            self.characters[1].player_sprite.change_x = 0
