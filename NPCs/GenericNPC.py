class GenericNPC:
    def __init__(self, health, name):
        self.health = health
        self.name = name

    def get_health(self):
        return self.health

    def get_name(self):
        return self.name