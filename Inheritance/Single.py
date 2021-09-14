class Base:
     def __init__(self , fname, fage):
          self.firstname = fname
          self.age = fage
     def view(self):
         print(self.firstname , self.age)
class Child(Base):
     def __init__(self , fname , fage):
          Base.__init__(self, fname, fage)
          self.lastname = "Machine Learning"
     def view(self):
          print(self.firstname ," is ",  self.age , " years old and he is a pro in " , self.lastname)
object = Child("Raj" , '21')
object.view()
