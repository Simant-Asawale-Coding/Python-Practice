
def countNum(num):
    f=open("input.txt",'r')
    count=0
    for line in f:
        tokens=line.split(",")
        for i in range(0,2):
            if num==int(tokens[i]):
                count=count+1
        
    f.close()
    return count    
        

print(countNum(111))


def sumCount():
    f=open("input.txt",'r')
    f_out=open("input2.txt",'w')
    total=0
    for line in f:
        tokens=line.split(",")
        for i in range(0,2):
            total=total+int(tokens[i])
        
        f_out.write("sum: "+ str(total)+" " + line)

sumCount()


