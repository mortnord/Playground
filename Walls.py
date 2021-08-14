import arcade


def setup_walls(self):

    self.wall_list = arcade.SpriteList(use_spatial_hash=True)
    wall = arcade.Sprite("Sprites/boxCrate.png", 1)
    wall.position = [50, 200]
    self.wall_list.append(wall)