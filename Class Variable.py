# Whenever we declare variable in a class is called instance variable.

# Instance Variable access using class name

class Human():
    a = 5;
    def joy(self):
        Human.a += 1
        print(Human.a)

ob = Human()
ob.joy()
print(ob.a)