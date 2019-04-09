from abc import ABC, abstractmethod

class AbstractBird(ABC):
    def __init__(self, name):
        self.name = name
        super().__init__()

    @abstractmethod
    def can_fly(self):
        pass


class Penguin1 (AbstractBird):
    def __init__(self):
        super().__init__("Penguin")

class Penguin2 (AbstractBird):
    def __init__(self):
        super().__init__("Penguin")

    def can_fly(self):
        return False


try:
    penguin = Penguin1()
except:
    print("TypeError: Can't instantiate abstract class Penguin1 with abstract methods can_fly")
    penguin = Penguin2()
    
print(penguin.can_fly())


