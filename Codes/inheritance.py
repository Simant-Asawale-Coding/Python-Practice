
class Vehicles:
    def general_purpose(self):
        print("general purpose is transportation")

class car(Vehicles):

    def __init__(self):
        wheels=4
        roof=True
    
    def specific_purpose(self):
        print("specific purpose is driving safely for long distances")

class motorcycles(Vehicles):

    def __init__(self):
        wheels=2
        roof=False
    
    def specific_purpose(self):
        print("specific purpose is riding regularly to short distances")

a=car()
b=motorcycles()

a.general_purpose()
a.specific_purpose()

b.general_purpose()
b.specific_purpose()

print(isinstance(a,car))

print(issubclass(car,Vehicles))