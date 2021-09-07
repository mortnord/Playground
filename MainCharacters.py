class MainCharacters:

    PLAYER_MOVEMENT_SPEED = 1  # Konstant med fart i bevegelse

    def __init__(self):
        self.health = 0
        pass

    def lose_health(self, amount):
        # Metoden man kaller for å miste liv
        self.health = self.health - amount
        pass

    def gain_health(self, amount):
        # Metoden man kaller for å få liv
        self.health = self.health + amount
        if self.health > 40:
            self.health = 40
        pass
