a=4
b=2

try:
    z=a/b
except TypeError as e:
    print("exception name:", TypeError)
    z=None

except Exception as e:
    print("exception name:", type(e).__name__)
    z=None


print(int(z))