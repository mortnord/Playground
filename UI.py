import arcade


def draw_UI(self, characters):
    health_text = f"Health: {characters[0].health}"  # antall liv på hovedpersonen
    arcade.draw_text(health_text, 10 + self.view_left, 50 + self.view_bottom, arcade.csscolor.WHITE, 18)

    health_text = f"Health: {characters[1].health}"  # antall liv på reservepersonen
    arcade.draw_text(health_text, 10 + self.view_left, 70 + self.view_bottom, arcade.csscolor.WHEAT, 18)
