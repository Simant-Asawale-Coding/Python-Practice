
address={}

address["tom"]={
    "name":"tom",
    "address":"NY park",
    "phone":"74388973923"
}

address["bob"]={
    "name":"bob",
    "address":"NY2 park",
    "phone":"899023973923"
}

import json

f=json.dumps(address)

with open('C://Users//simant.asawale//Desktop//Python//Codes//hello.txt','w') as file:
    file.write(f)


    student={}

student["1"]={"name":"Simant","marks":"100"}
student["2"]={"name":"Sajiri","marks":"99"}
student["3"]={"name":"Aryan","marks":"99"}
student["4"]={"name":"Vedant","marks":"99"}

with open("students_data.txt",'w') as file:
    file.write(json.dumps(student))
    file.write(json.dumps("yandruss"))

new_Data=open("students_data",'r')
f=json.loads(new_Data)




