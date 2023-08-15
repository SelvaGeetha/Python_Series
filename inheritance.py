#use class with in other class and fetch the value from other class 

class classroon:
    def name(self):
        print("name")
    def age (self):
        print("age")
    def initial(self):
        print("initial")
class player(classroon):#which class we want to inherit we use inside the bracket
    def s(self):
        print("yes")

selva=player()
selva.name()