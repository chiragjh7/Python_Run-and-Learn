class mom:
    mom_name = ""
    def mom(self):
        print(self.mom_name)
class dad:
    dad_name = ""
    def dad(self):
        print(self.dad_name)
class daughter(mom,dad):
    def parents(self):
        print("Father's name: ",self.dad_name)
        print("Mother's name: ",self.mom_name)
object=daughter()
object.dad_name="raj"
object.mom_name="nandhini"
object.parents()