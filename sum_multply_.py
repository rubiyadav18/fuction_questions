n=int(input("enter a number"))
def multi():
    i=1
    sum=0
    while i<=n:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    return (sum)
print(multi())