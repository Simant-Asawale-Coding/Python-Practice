
class animal:
    """ below is the constructor for properties"""
    def __init__(self,name,type):
        self.name=name
        self.type=type

    """Below are the methods"""

    def speaks(self):
        if self.type=="cat":
            print(self.name," meows")
        elif self.type=="dog":
            print(self.name," barks")
        else:
            print("we dont have speaking data for ",self.name)

    def eats(self):
        if self.type=="cat":
            print(self.name," eats fish")
        elif self.type=="dog":
            print(self.name," eats bones")    
        else:
            print("we dont have eating data for ",self.name)

if __name__=="__main__":

    simba=animal(name="simba", type="cat")
    rocky=animal(name="rocky", type="dog")
    humba=animal(name="humba", type="cow")

    simba.eats()
    simba.speaks()

    rocky.eats()
    rocky.speaks()

    humba.eats()
    humba.speaks()