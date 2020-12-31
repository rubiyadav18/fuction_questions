a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
def max():
    if a>b and a>c and c>a:
        print(a,max)
    if b>a and b>c and c>b:
        print(b,max)
    else:
        print(c,max)
max()
    