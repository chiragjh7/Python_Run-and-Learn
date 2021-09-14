class Granddad:
 
    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name

class dad(Granddad):
    def __init__(self, father_name, grandfather_name):
        self.father_name = father_name
 
        Granddad.__init__(self, grandfather_name)

class Son(dad):
    def __init__(self,son_name, father_name, grandfather_name):
        self.son_name = son_name
 
        dad.__init__(self, father_name, grandfather_name)
 
    def print_name(self):
        print('Grandfather name :', self.grandfather_name)
        print("Father name :", self.father_name)
        print("Son name :", self.son_name)
 
s1 = Son('Lucky', 'Raj', 'Kamal')
s1.print_name()