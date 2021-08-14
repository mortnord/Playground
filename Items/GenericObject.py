class GenericObject:
    weight = 0
    name = ""

    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def get_weight(self):
        return self.weight

    def get_name(self):
        return self.name
