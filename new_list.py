list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
i=0
empty=[ ]
while i<len(list1):
    if list2[i] not in list1:
        empty.append(list2[i])
    i=i+1
print(empty)