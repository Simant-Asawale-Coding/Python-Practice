
class animal:
    def __init__(self, name,age,type):
        self.name=name
        self.age=age
        self.type=type

    
    def speaks(self):
        if self.type=='cat':
            print(self.name," meows")
        elif self.type =='dog':
            print(self.name,"barks")
        elif self.type =='cow':
            print(self.name,"moos")
        else:
            print("no speaking data for ",self.name)

    def eats(self):
        if self.type=='cat':
            print(self.name," eats fish")
        elif self.type =='dog':
            print(self.name,"eats bones")
        elif self.type =='cow':
            print(self.name,"eats fodder")
        else:
            print("no eating data for ",self.name)


pilludi=animal(name="pilludi boys", age=2, type='cat')
pilludi.speaks()
pilludi.eats()

rocky=animal(name="Rocky", age=10, type='dog')
rocky.speaks()
rocky.eats()

toofan=animal(name="toofan", age=6, type='cow')
toofan.speaks()
toofan.eats()