# When a class Derives every attributes and methods from other class

# It helps reusability of code

class Base:
    a = 5
    b = 10

    def sum(self):
        print(Base.a + Base.b)

class Derived(Base):
    pass


ob = Derived()

ob.sum()