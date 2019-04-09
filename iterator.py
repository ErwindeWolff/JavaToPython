class NaturalNumbers:
    def __iter__(self):
        self.value = -1
        return self
    
    def __next__(self):
        self.value += 1
        return self.value

for x in NaturalNumbers():
    if (x <= 1000):
        print(x)
    else:
        break
