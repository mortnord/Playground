import arcade
# Kamera sine yttre begrensning før man flytter kameraet
LEFT_VIEWPORT_MARGIN = 100
RIGHT_VIEWPORT_MARGIN = 100
BOTTOM_VIEWPORT_MARGIN = 100
TOP_VIEWPORT_MARGIN = 100


def update_camera(self, current_character):
    changed = False

    # Kamera til venstre
    left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
    if current_character.player_sprite.left < left_boundary:
        self.view_left -= left_boundary - current_character.player_sprite.left
        changed = True

    # Kamera til høyre
    right_boundary = self.view_left + self.width - RIGHT_VIEWPORT_MARGIN
    if current_character.player_sprite.right > right_boundary:
        self.view_left += current_character.player_sprite.right - right_boundary
        changed = True

    # Kamera opp
    top_boundary = self.view_bottom + self.height - TOP_VIEWPORT_MARGIN
    if current_character.player_sprite.top > top_boundary:
        self.view_bottom += current_character.player_sprite.top - top_boundary
        changed = True

    # Kamera Ned
    bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
    if current_character.player_sprite.bottom < bottom_boundary:
        self.view_bottom -= bottom_boundary - current_character.player_sprite.bottom
        changed = True

    # Faktisk endre kamera
    if changed:

        self.characters[0].inventory_character.update_position(self.view_left, self.view_bottom)
        self.view_bottom = int(self.view_bottom)
        self.view_left = int(self.view_left)
        arcade.set_viewport(self.view_left,
                            self.width + self.view_left,
                            self.view_bottom,
                            self.height + self.view_bottom)
