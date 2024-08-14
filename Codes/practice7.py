
class animal:
    def __init__(self,Name,type_animal):
        self.name=Name
        self.type=type_animal

    
    def animal_eats(self):
        if self.type=='cat':
            print(self.name,"eats fish")




if __name__=="__main__":
    simba=animal(Name='Simba',type_animal='cat')
    simba.animal_eats()

    with open ('practice7.txt','w') as writer:
        writer.write("this is practice 7\n")

with open('practice7.txt','a') as writer:
    writer.write("this is an appended text\n")

with open('practice7.txt','r') as writer:
  reader=  writer.read()
  print(reader)
