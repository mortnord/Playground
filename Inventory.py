import arcade

import SetupObjects
from Enumerators import Veggies

INVENTORY_SCALING = 2  # Konstant for størrelse


class SpritePosition:
    def __init__(self, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY


class Inventory:
    def __init__(self):
        self.inventory_contents_sprite_list_position = []
        self.inventory_sprite = arcade.Sprite("Sprites/Inventory V1.png", INVENTORY_SCALING)
        self.inventory_sprite_list = arcade.SpriteList()
        self.inventory_sprite_list.append(self.inventory_sprite)
        self.InventoryContents = []
        self.InventoryBusy = []
        self.setup_sprite_position()

    def append_to_inventory(self, ItemObjektToAppend):
        for x in range(len(self.InventoryBusy)):
            if self.InventoryBusy[x] == False:
                print(str(x) + " inventory slot er ledig")
                self.InventoryContents.insert(x, ItemObjektToAppend)
                self.inventory_sprite_list.append(ItemObjektToAppend.ItemObjekt.icon)
                self.InventoryBusy[x] = True
                break

        self.update_sprite_position()
        self.reorder_contents()
        pass

    def reorder_contents(self):
        for x in range(len(self.inventory_sprite_list)):
            try:
                self.InventoryContents[x].ItemObjekt.icon.center_y = self.inventory_contents_sprite_list_position[x].PosX
                self.InventoryContents[x].ItemObjekt.icon.center_x = self.inventory_contents_sprite_list_position[x].PosY
            except IndexError:
                pass

    def inventory_position(self, view_left, view_bottom):
        self.inventory_sprite.center_x = view_left + 400
        self.inventory_sprite.center_y = view_bottom + 250
        self.update_sprite_position()
        self.reorder_contents()
        pass

    def setup_sprite_position(self):  # TODO Endre på.
        for x in range(8):
            self.InventoryBusy.append(False)
            try:
                print(x)
                if x <= 3:
                    Pos = SpritePosition(self.inventory_sprite.top - 15, self.inventory_sprite.left + (x * 31) + 18)
                    self.inventory_contents_sprite_list_position.append(Pos)
                elif x >= 4:
                    Pos = SpritePosition(self.inventory_sprite.top - 45, (x * 31) + 18 - 124)
                    self.inventory_contents_sprite_list_position.append(Pos)
            except IndexError:
                print("ERROR")

    def update_sprite_position(self):
        for x in range(8):
            try:
                if x <= 3:
                    self.inventory_contents_sprite_list_position[x].PosX = self.inventory_sprite.top - 15
                    self.inventory_contents_sprite_list_position[x].PosY = self.inventory_sprite.left + (x * 31) + 18
                elif x >= 4:
                    self.inventory_contents_sprite_list_position[x].PosX = self.inventory_sprite.top - 45
                    self.inventory_contents_sprite_list_position[x].PosY = self.inventory_sprite.left + (
                            x * 31) + 18 - 124
            except IndexError:
                print("ERROR")

    def create_object(self, Object_to_create):
        if Object_to_create == Veggies.Carrot:
            self.append_to_inventory(SetupObjects.create_carrot())
            print("Gulrot generert")
        elif Object_to_create == Veggies.Rutabaga:
            self.append_to_inventory(SetupObjects.create_rutabaga())
            print("Kålrabi generert")
        pass
