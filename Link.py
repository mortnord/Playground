import arcade

from Inventory import Inventory

SPRITE_SCALING_PLAYER = 0.05
PLAYER_MOVEMENT_SPEED = 3


# https://api.arcade.academy/en/latest/examples/platform_tutorial/step_01.html
def setup_link(self):
    """ Set up the game and initialize the variables. """

    # Create the sprite lists
    self.player_list = arcade.SpriteList()

    # Liv
    self.health = 12
    self.InventoryLink = Inventory()
    # Set up the player
    self.player_sprite = arcade.Sprite("Sprites/Link.png", SPRITE_SCALING_PLAYER)
    self.player_sprite.center_x = 50  # Starting position
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)

    self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)


def lose_health(self, amount):
    self.health = self.health - amount
    pass


def gain_health(self, amount):
    self.health = self.health + amount
    pass
