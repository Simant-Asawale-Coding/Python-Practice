f=open("new-text.txt",'w') 
f.write("hey!, i am Simant.\n what is ur name\n how r u feeling today?\n whats so special?\n")
f.close()


f=open("new-text.txt",'r')
f_out=open("new-text2.txt",'w')
for line in f:
  tokens=line.split(" ")
  print(tokens)
  f_out.write( line + "tokens: "+str(len(tokens)))


f.close()
f_out.close()