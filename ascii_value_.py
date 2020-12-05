chr=input("enter a any character")
b=ord(chr)
if b>=65 and b<=90:
    print("it is alpabet",chr)
elif b>=97 and b<=122:
    print("it is small character",chr)
else:
    print("not a alphabet")


