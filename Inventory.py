import arcade

import SetupObjects

INVENTORY_SCALING = 2  # Konstant for størrelse
ITEM_HEIGHT = 64
ITEM_WIDTH = 64
SLOT_OVERSIZE = 1.1
SLOT_HEIGHT = int(SLOT_OVERSIZE * ITEM_HEIGHT)
SLOT_WIDTH = int(SLOT_OVERSIZE * ITEM_WIDTH)

VERTICAL_MARGIN_PERCENT = 0.01
HORIZONTAL_MARGIN_PERCENT = 0.01

BOTTOM_Y = SLOT_HEIGHT / 2 + SLOT_HEIGHT * VERTICAL_MARGIN_PERCENT
START_X = SLOT_WIDTH / 2 + SLOT_WIDTH + HORIZONTAL_MARGIN_PERCENT
X_SPACING = SLOT_WIDTH + SLOT_WIDTH * HORIZONTAL_MARGIN_PERCENT


class SpritePosition:
    def __init__(self, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY


class Inventory:
    def __init__(self, color_inventory):
        self.initialized = False
        self.item_list = None
        self.held_item = None
        self.held_item_original_position = None
        self.item_inventory_slots = None
        self.color_inventory = color_inventory

    def setup(self):
        self.held_item = []
        self.held_item_original_position = []
        self.item_list = arcade.SpriteList()
        self.item_inventory_slots: arcade.SpriteList = arcade.SpriteList()
        for i in range(9):
            item_slot = arcade.SpriteSolidColor(ITEM_WIDTH, ITEM_HEIGHT, self.color_inventory)
            item_slot.position = START_X + i * X_SPACING, BOTTOM_Y
            self.item_inventory_slots.append(item_slot)

        self.initialized = True

    def pick_up_item(self, item: arcade.Sprite):
        self.item_list.remove(item)
        self.item_list.append(item)

    def item_interaction_mouse(self, x, y, button):
        print(x)
        print(y)
        items = arcade.get_sprites_at_point((x, y), self.item_list)
        if len(items) > 0:
            primary_item = items[-1]

            # All other cases, grab the face-up card we are clicking on
            self.held_item = [primary_item]
            # Save the position
            self.held_item_original_position = [self.held_item[0].position]
            # Put on top in drawing order
            self.pick_up_item(self.held_item[0])

    def item_interaction_mouse_moving(self, dx, dy):
        for item in self.held_item:
            item.center_x += dx
            item.center_y += dy

    def item_interaction_mouse_release(self, x, y):
        if len(self.held_item) == 0:
            return

        item, distance = arcade.get_closest_sprite(self.held_item[0], self.item_inventory_slots)
        reset_position = True

        if arcade.check_for_collision(self.held_item[0], item):
            for i, dropped_item in enumerate(self.held_item):
                dropped_item.position = item.center_x, item.center_y
            reset_position = False
        if reset_position:
            for item_index, card in enumerate(self.held_item):
                card.position = self.held_item_original_position[item_index]
        self.held_item = []

    def create_carrot(self):
        testCarrot = SetupObjects.create_carrot()
        testCarrot.position = (200, 200)
        self.item_list.append(testCarrot)
        pass
