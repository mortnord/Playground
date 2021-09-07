class MainCharacters:

    PLAYER_MOVEMENT_SPEED = 1  # Konstant med fart i bevegelse

    def __init__(self):
        self.health = 0
        pass

    def lose_health(self, amount):
        # Metoden man kaller for å miste liv
        self.health = self.health - amount
        if self.health <= 0:
            self.health = 0
            print("Out of health")
            self.player_sprite.center_x = 70 # Sentrerer spiller til utgangspunktet når tom for liv
            self.player_sprite.center_y = 50
            self.health = 12                 # Tilbakestiller liv til 12 når tom for liv
            self.inventory_character.get_inventory_contents().clear()
            for x in range(len(self.inventory_character.inventory_contents_sprite_list)): # Tilbakestiller inventorylist
                self.inventory_character.items_in_food_inventory = self.inventory_character.items_in_food_inventory - 1
                self.inventory_character.inventory_contents_sprite_list.pop()
        pass

    def gain_health(self, amount):
        # Metoden man kaller for å få liv
        self.health = self.health + amount
        if self.health > 40:
            self.health = 40
        pass
