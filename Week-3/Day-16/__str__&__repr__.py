# Q : __str__ and __repr__ methods.

class Student :
    
    def __init__(self, name, mark) :
        self.name = name 
        self.mark = mark
    
    # Returns a user-friendly / readable string representation of an object (mainly for display).
    def __str__(self):
        return f"Student name = {self.name} , mark = {self.mark}"
    
    # Returns an official / developer-friendly string representation of an object (mainly for debugging).
    def __repr__(self):
        return f"Student(name = '{self.name}' , mark = '{self.mark}')"
    
stud = Student("JOHN","A+")
print(stud)
print(str(stud))
print(repr(stud))