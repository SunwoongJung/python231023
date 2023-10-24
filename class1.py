# class define

class Person:
    def __init__(self): #parameter로서 self의 의미, 선언이 없으므로 class 속성, 변수 만들려면 그냥.찍고 하면 되는지
        self.name = "default name"
        self.age = 15

    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p2 = Person()
p1.name = "전우치"

p1.print()
p2.print()

Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)
