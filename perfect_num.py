def perfect():
    i=1
    sum=0
    while i<n:
        if n%i==0:
            a=i
            sum=sum+a
        i=i+1
    if sum==n:
        print("perfect number")
    else:
        print("not perfect")
n=int(input("enter a number"))
perfect()
