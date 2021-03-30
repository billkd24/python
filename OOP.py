class Person():
    def __init__(self,name,age):
        self.f_name = name
        self.my_age = age

p1 = Person("Jane",20)
p2 = Person("Mike",24)
p3 = Person("Jake",22)

print(f"{p1.f_name} is {p1.my_age} years old")