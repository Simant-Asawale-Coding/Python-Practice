
import json 
students={}

students['1']={"name":"simant",
             "age":22, "marks":100}
students['2']={"name":"simaefwwnt",
             "age":32, "marks":90}
students['3']={"name":"simanwet",
             "age":42, "marks":80}
students['4']={"name":"simfwedant",
             "age":12, "marks":90}

s=json.dumps(students)
print(s)

k=json.loads(s)

print(type(k['1']))