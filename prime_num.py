def per():
    list=[3,9,13,23,12,34,56,7,8,13,33,37,19,39,41,23]
    i=0
    empty=[]
    while i<len(list):
        j=0
        b=2
        while b<list[i]:
            if list[i]%b==0:
                j=j+1
            b=b+1
        if j==0:
            empty.append(list[i])
        i=i+1
    print(empty)
per() 