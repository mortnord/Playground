import arcade


def setup_walls(self):
    self.wall_list = arcade.SpriteList(use_spatial_hash=True)