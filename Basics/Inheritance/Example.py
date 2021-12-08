class Parent:
    def __init__(self, fname, fage) :
        self.firstname = fname
        self.age = fage
    def view(self):
        print(self.firstname, self.age)
class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self,fname, fage)
        self.lastname = "Maching learning"
    def view(self):
        print(self.firstname, "came", self.age, " years ago. Today, python is the base for ",self.lastname)
        object = Child("Python",'28')
        object.view();                
        