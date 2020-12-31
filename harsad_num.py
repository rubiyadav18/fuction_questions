def harsad():
    i=1
    empty=[ ]
    while i<=100:
        j=i
        sum=0
        while j>0:
            b=j%10
            sum=sum+b
            j=j//10
        if i%sum==0:
            empty.append(i)
        i=i+1
    print(empty)
harsad()
       