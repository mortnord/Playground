import arcade

INVENTORY_SCALING = 2  # Konstant for størrelse


class Inventory:
    def __init__(self):
        self.inventory_contents = list()  # Lag liste over innholdet i inventory
        self.inventory_contents_bar = list()

        self.inventory_list = arcade.SpriteList()  # Lag liste over hva inventories som skal tegnes
        self.inventory_content_sprite_list_bar = arcade.SpriteList()
        self.inventory_contents_sprite_list = arcade.SpriteList()  # Lag liste over hva innhold i inventory som skal
        # tegnes

        self.inventory_contents_sprite_list_position_y = list()  # Y-posisjonen til ting som skal tegnes
        self.inventory_contents_sprite_list_position_x = list()  # X-posisjonen til ting som skal tegnes

        self.inventory_contents_bar_sprite_list_position_x = list()
        self.inventory_contents_bar_sprite_list_position_y = list()
        # TODO: Gjør dette mer elegant...

        # Kobler sprite .pngen til koden
        self.inventory_sprite = arcade.Sprite("Sprites/Inventory V1.png", INVENTORY_SCALING)
        self.inventory_sprite_bar = arcade.Sprite("Sprites/Inventory_bar.png", INVENTORY_SCALING)
        # startposisjon
        # Legger til for å tegnes
        self.inventory_list.append(self.inventory_sprite)
        self.inventory_content_sprite_list_bar.append(self.inventory_sprite_bar)
        self.items_in_food_inventory = 0  # antall objekter i food inventory

        self.update_sprite_position()  # Posisjonen til sprites i inventory

    def update_contents(self):

        self.inventory_contents_sprite_list.append(self.inventory_contents[self.items_in_food_inventory].icon)
        # legg til icon som skal tegnes i lista over ting i inventory som skal tegnes
        self.items_in_food_inventory = self.items_in_food_inventory + 1
        # Antall objekter i food inventory

    def reorder_contents(self):  # sett posisjonen til iconene avhengig av posisjonen til inventory og inventory slots
        for x in range(len(self.inventory_contents)):
            try:
                self.inventory_contents[x].icon.center_y = self.inventory_contents_sprite_list_position_y[x]
                self.inventory_contents[x].icon.center_x = self.inventory_contents_sprite_list_position_x[x]
            except IndexError:
                pass
        for x in range(2):
            try:
                self.inventory_contents_bar[x] = self.inventory_contents[x]
            except IndexError:
                pass

    def get_inventory_contents(self):  # returnerer inventory contents
        return self.inventory_contents

    def append_to_inventory(self, object_to_append):  # Hva vi kaller for å legge items til, først vil den legge til
        # ting
        # Så vil den oppdatere innholdet, koble spriten til objektet til plasseringen i inventory, og så vil den
        # omorganisere slik at alt er på rekke og rad.

        self.inventory_contents.append(object_to_append)
        self.update_contents()
        self.reorder_contents()

    def update_position(self, view_left, view_bottom):  # : TODO: Dette må gjøres mer elegant, og til en bedre måte...
        self.inventory_sprite.center_x = view_left + 400
        self.inventory_sprite.center_y = view_bottom + 200
        self.inventory_sprite_bar.center_x = view_left + 150
        self.inventory_sprite_bar.center_y = view_bottom + 40
        self.inventory_contents_sprite_list_position_x.clear()
        self.inventory_contents_sprite_list_position_y.clear()
        self.inventory_contents_bar_sprite_list_position_x.clear()
        self.inventory_contents_bar_sprite_list_position_y.clear()
        self.update_sprite_position()
        pass

    def update_sprite_position(self):  # : TODO : Gjøres mer elegant, og til en bedre måte...
        for x in range(8):
            try:
                if x <= 3:
                    self.inventory_contents_sprite_list_position_y.append(self.inventory_sprite.top - 15)
                    self.inventory_contents_sprite_list_position_x.append(self.inventory_sprite.left + (x * 31) + 18)
                elif x >= 4:
                    self.inventory_contents_sprite_list_position_y.append(self.inventory_sprite.top - 45)
                    self.inventory_contents_sprite_list_position_x.append(
                        self.inventory_sprite.left + (x * 31) + 18 - 124)
            except IndexError:
                pass
        for x in range(2):
            try:
                self.inventory_contents_bar_sprite_list_position_y.append(self.inventory_sprite_bar.top - 15)
                self.inventory_contents_bar_sprite_list_position_x.append(self.inventory_sprite_bar.left + (x * 31) + 18)
            except IndexError:
                pass
