class Bird:
    def __init__(self, name):
        self.name = name

    def has_feathers(self):
        print(f"{self.name} has feathers")

    def can_fly(self):
        print(f"{self.name} can fly")

    def lays_eggs(self):
        print(f"{self.name} lays eggs")


class Ostrich(Bird):
    def __init__(self):
        super(Ostrich, self).__init__("Ostrich")

    def can_fly(self):
        print(f"Ostrich can NOT fly")


class Penguin(Bird):
    def __init__(self):
        Bird.__init__(self, "Penguin")

    def can_fly(self):
        print(f"Penguin can NOT fly")

Ostrich().can_fly()
Ostrich().lays_eggs()
