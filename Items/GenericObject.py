class GenericObject:
    weight = 0
    name = ""

    #  ett GeneriskObjekt er det mest grunnleggende av type objekt, skal egentlig ikke brukes, kun ha metoder som arves.
    def __init__(self, weight, name, type_object):
        self.weight = weight
        self.name = name
        self.type_object = type_object


    def get_weight(self):
        return self.weight

    def get_name(self):
        return self.name

    def get_type_object(self):
        return self.type_object
