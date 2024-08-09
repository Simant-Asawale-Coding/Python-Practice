import json
f = open('students_data.txt','r')
s = f.read()
print(type(s))
print(s)
students=json.loads(s)
print(type(students))
print(students)

print(students["1"])
print("full dictionary")

for keys in students:
    print(keys,students[keys])
