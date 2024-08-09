namebook={"simant":9800157, "daddy":985010007,"mamma":98500007,"dada":98500000 }
print(namebook)

namebook["mama"]=992298

print(namebook)
print(namebook["dada"])
del namebook["mama"]
print(namebook)

for key in namebook:
    print("key:",key,"value:",namebook[key])


    for k,v in namebook.items():
        print(k,v)

namebook.clear()
print("cleared")
print(namebook)