def check(list):
    empty1=[]
    # " here i am using empty1 list because i want to appned big number of 50"
    for i in list:
        if i>50:
            empty1.append(i)
    return empty1

list=[56,78,55,85,95,94]
var=check(list)
empty2=[]
# here one more i am using empty2 list because i want ot  append number of divide by 5 
def big(var):
    for i in var:
         if i%5==0:
             empty2.append(i)
    return empty2
big(var)
print(var)
print(empty2)
