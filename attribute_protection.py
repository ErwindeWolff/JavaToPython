class A:
    def __init__(self):
        self.__name = "A"
        self.__value = 10

class B(A):
    def to_string(self):
        return f"{self.__name} {self.__value}"

b = B()

try:
    print("Option one")
    print(b.to_string())
    b.__name = "B"
    b.__value = 20
    print(b.to_string())
except:
    print("Nope! Option two")
    print(b._A__name, b._A__value)
    b._A__name = "B"
    b._A__value = 20
    print(b._A__name, b._A__value)


