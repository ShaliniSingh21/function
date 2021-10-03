def my_fun (*a):
    i=0
    sum=0
    while i<len(a):
        sum=sum+(a[i])
        i=i+1 
    return(sum)
print(my_fun(8,7,0,2,3))