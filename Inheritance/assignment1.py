class parentclass:
    def add(self, a, b):
        print("sum of 2 numbers is", a+b)

    def sub(self, a, b):
        print("subtraction of 2 numbers is", a - b)

    def mul(self, a, b):
        print("multiplication of 2 numbers is", a * b)

class childclass(parentclass):
    def div(self, a, b):
        print("division of 2 numbers is ", a/b)
x = childclass()
x.add(3,2)
x.sub(9, 5)
x.mul(9, 5)
x.div(15, 5)