exp=[2340,3450,2345,5560]

total=0

for item in exp:
    total=total+item

print(total)

for i in range(1,11):
    print(i)

print(i)   
total=0
for i in range(len(exp)):
    total+=exp[i]
    print("Month:",i+1,"Expenses:", exp[i], "Total:", total)


locations=["living room", "bedroom","garage","bathroom"]
keys_location="bedroom"

for i in locations:
    if keys_location==i:
        print("keys found in",i)
        break
    else:
        print("keys not found in:",i)