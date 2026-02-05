n = 530456

name = "ksTadfjl"
# print(name[len(name)//2])

# if (n>0 or n%2==0):
#     print("hello world")

# print(n%10)

# print(n//10)
# print(n%10)

print(name.isupper())
print(name.isalpha())

if ("A"<= name <="Z"):
    print("upper case")
else:
    print("lower case")

if ("a"<= name <="z"):
    print("lower case")
else:
    print("upper case")
    
# alpha or not 

if ("A"<= name <="Z" or "a" <= name <="z"):
    print("this is alpha")
