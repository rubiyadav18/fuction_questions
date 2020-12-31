def max():
    marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
    i=0
    empty=[ ]
    while i<len(marks):
        j=0
        b=0
        while j<len(marks[i]):
            if b<marks[i][j]:
                b=marks[i][j]
            j=j+1
        empty.append(b)
        i=i+1
    print(empty)
max()

