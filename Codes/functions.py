

toms_exp=[200, 300, 400]
johns_exp=[700, 300, 500]

def total_calculator(exp):
    total=0
    for item in exp:
        total=total + item

    return total

print("tom's total:",total_calculator(toms_exp))
print("john's total:",total_calculator(johns_exp))
print("new line")
def sum(a,b):
    print("a=",a)
    print("b=",b)
    total=a+b
    return total


print("total:", sum(b=5,a=6))