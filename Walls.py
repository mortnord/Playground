import arcade


def setup_walls(self):
    # Her definerer vi at walls består av sprites, der bilde er hentet fra Sprites/boxCrate.png
    self.wall_list = arcade.SpriteList(use_spatial_hash=True)
    wall = arcade.Sprite("Sprites/boxCrate.png", 1)
    # her setter vi posisjonen og legger den til i lista over walls som skal tegnes

    wall.center_x = 50
    wall.center_y = 200
    self.wall_list.append(wall)
# Her har KJ kommentert :)
#MortenKonflikter