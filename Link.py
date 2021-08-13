import arcade

SPRITE_SCALING_PLAYER = 0.1
PLAYER_MOVEMENT_SPEED = 5


# https://api.arcade.academy/en/latest/examples/platform_tutorial/step_01.html
def setup_link(self):
    """ Set up the game and initialize the variables. """

    # Create the sprite lists
    self.player_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()

    # Score
    self.score = 0

    # Set up the player
    # Character image from kenney.nl
    self.player_sprite = arcade.Sprite("Sprites/Link.png", SPRITE_SCALING_PLAYER)
    self.player_sprite.center_x = 50  # Starting position
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)

    self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
