class Component:
    def __init__(self, name):
        self.name = name
    
    def to_string(self):
        return f"the {self.name} down in valley-o"

    def untouched(self):
        return "This is stable!"
        

class Decorator(Component):
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def to_string(self):
        return (f"{self.name} on the {self.content.name}, \n"
                + self.content.to_string())


verse = Component("bog")
verse = Decorator("hole", verse)
verse = Decorator("tree", verse)
verse = Decorator("branch", verse)
verse = Decorator("nest", verse)
verse = Decorator("bird", verse)
verse = Decorator("feather", verse)
verse = Decorator("flea", verse)

print(verse.to_string())
print(verse.untouched())


