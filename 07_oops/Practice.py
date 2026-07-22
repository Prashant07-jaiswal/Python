class Student:
    def __init__(self,id,name,marks):
        self.id = id
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"ID {self.id}")
        print(f"NAME {self.name}")
        print(f"MARKS {self.marks}")
    

s1 = Student(107,"Prashant",90)
s1.display()

class Parent:
    def test_parent():
        print(("this is the parent"))
        
class Child(Parent):
        pass