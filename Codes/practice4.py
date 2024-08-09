
with open("practice4.txt",'w') as nt:
    nt.write("this is a string\n")

s=open("practice4.txt",'a')
s.write("this is appended string")
s.close()

a=open("practice4.txt","r+")

a_out=open("practice4copy.txt",'w')

for line in a:
    tokens=line.split(" ")
    count=0
    for i in tokens:
        count=count+1
    a_out.write( line+" count:"+ str(count)+"\n")

a.close()
a_out.close()

import practice5 

print(practice5.yandruss_sum(8,10))
    

