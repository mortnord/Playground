import arcade


def draw_UI(self, linkCharacter):
    health_text = f"Health: {linkCharacter.health}"
    arcade.draw_text(health_text, 10 + self.view_left, 10 + self.view_bottom, arcade.csscolor.WHITE, 18)