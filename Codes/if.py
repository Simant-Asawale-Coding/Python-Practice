num=input("enter any interger: ")
print(type(num))
num=int(num)
print(type(num))

if num%2==0:
    print('it is an even number')
else:
    print('it is an odd number') 

indian=["samosa","dhokla","paratha","pav bhaji"]
italian=["pasta","pizza","tacos"]
Chinese=["fried rice","chicken lollipop","noodles"]

dish=input("enter the name fo the dish:")

if dish in indian:
    print("it is an Indian dish")
elif dish in italian:
        print("dish is italian")
elif dish in Chinese:
    print("dish is chinese")
else:
    print("this dish u provided is out of my limited knowledge")





