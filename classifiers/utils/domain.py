class Domain:
    def __init__(self):
        self.attributes = []
        self.category = None

    def get_attribute(self, name):
        for a in self.attributes:
            if a.name == name:
                return a
        return None


class Attribute:
    def __init__(self, name, is_continuous, values=None):
        self.name = name
        self.is_continuous = is_continuous
        self.values = [] if values is None else values
