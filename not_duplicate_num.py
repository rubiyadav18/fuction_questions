def new_list():
    a = [1,5,10,12,16,20,1,2,10,13,16]
    i=0
    new_list=[ ]
    while i<len(a):
        j=i+1
        index=0
        while j<len(a):
            if a[i]==a[j]:
                index=index+1
            j=j+1
        if a[i] not in new_list or index>0:
            new_list.append(a[i])
        i=i+1
    print("new_list",new_list)
new_list()