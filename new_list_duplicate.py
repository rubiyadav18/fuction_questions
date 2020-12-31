def new_list():
    list1 = [1, 342, 75, 23, 98,75,23,98,12,10,1]
    i=0
    new_list=[ ]
    while i<len(list1):
        j=i+1
        index=0
        while j<len(list1):
            if list1[i]==list1[j]:
                index=index+1
            j=j+1
        if list1[i] not in new_list and index>0:
            new_list.append(list1[i])
        i=i+1
    print("new_list",new_list)
new_list()