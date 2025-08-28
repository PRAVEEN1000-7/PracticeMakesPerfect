# Q : Create a Dog class with attributes (name, age) and methods (bark(), get_age()).

class Dog:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof !! Woof !!")
    
    def get_age(self):
        return self.age
    
    

dog = Dog("jack",5)
dog.bark()
age = dog.get_age()
print(f"{dog.name} age is {age}.")
    