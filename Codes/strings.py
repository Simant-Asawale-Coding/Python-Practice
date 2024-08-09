text="ice box" #declaration
print(text)
print(text[2]) # this value cannot be changed as strings in oython are partially immutable, we need to change the entire value if we want to do so
print(text[0:3]) #sub indicing


string1='string with " double quotes'
string2="string with single '' quotes in it "
string3="my name\nis\nSimant"

print(string1)
print(string2)
print(string3)

#concatenation

string4="sim"
string5="ant"

print(string4+' '+string5)

#converting number to string

number=22
#print(string1+number)----this will not work as python cannot concatenate string with number

#hence we use str() function


print(string1+" "+str(number))