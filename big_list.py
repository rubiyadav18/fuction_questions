small_list = [[1,2,3], [5,8,9],[3,4,5],[6,7,8,],[12,14,10],[20,30,50,40],]
c1=0
while c1<len(small_list):
    big_list_length=len(small_list[c1])
    c2=0
    while c2<big_list_length:
        print(small_list[c1][c2])
        c2=c2+1
    c1=c1+1
    print('------')