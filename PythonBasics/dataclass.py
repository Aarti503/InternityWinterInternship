#without dataclass
class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    #changing my clas representation
    def __repr__(self):
        return "Human(name:{} , age:{} , gender:{})"\
             .format(self.name, self.age, self.gender)
    #changing the functionality of equality function
    def __eq__(self, other):
        return (self.name, self.age, self.gender) ==  (other.name, other.age, other.gender)
h1 = Human("Siya", 65, "Female")
h2 = Human("Siya", 65, "Female")
h3 = Human("Sameer",19,"Male")
print(h1 == h2)
print(h1)
 # with dataclass
from dataclasses import dataclass
@dataclass
class Animal:
    name: str
    age: int
    area: str

a1 = Animal('Dog',15,'Delhi')
a2 = Animal('Dog',15,'Delhi')
print(a1)
print(a1==a2)
