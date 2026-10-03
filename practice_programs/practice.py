class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print(self.name)
        print(self.rollno)
std1=student("sanket",21)
std1.display()
std2=student("harshit",22)
std2.display()