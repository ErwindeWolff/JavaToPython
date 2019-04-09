
class A:
    def a_function(self):
        return "The best of the best... unless you are talking about sleep!"
    
    def to_string(self):
        return "I am an instance of class A!"

class B:
    def b_function(self):
        return "B's are not quite A's, but at least you won't burn out!"
    
    def to_string(self):
        return "I am an instance of class B!"


class C(A, B):
    pass


c = C()
print(c.a_function())
print(c.b_function())
print(c.to_string())



