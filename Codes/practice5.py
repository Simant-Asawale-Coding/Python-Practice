def yandruss_sum(a,b):
    total=a+b
    print("this function belongs to module __name__=",__name__)
    return total

if __name__=="__main__":
    print("hello, u r in __name__=",__name__)

print(yandruss_sum(8,9))

#exception handling

a=input("enter a: ")
b=input("enter b: ")


try:
    ans=int(a)/int(b)
except ZeroDivisionError as e:
    print("there was an exception: ", "ZeroDivisionError ", "please input values over 0")
    ans=None
  

print(ans)