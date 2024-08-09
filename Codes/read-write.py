
f= open("funny.txt",'w')
f.write("Hello World\nwhats going on\nthis is me, simant\nlooking to be the best")
f.close()

f=open("funny.txt",'a')
f.write("\nhow r u doing?")
f.close()

f= open("funny.txt",'r')
s=f.read()
print(s)
f.close()

f=open("funny.txt",'r')
f_out=open("funnt.txt",'w')

for line in f:
    tokens= line.split(" ")
    linetoadd = line +"wordcount: "+ str(len(tokens))  + "\n"
    f_out.write(linetoadd)

f.close()
f_out.close()
