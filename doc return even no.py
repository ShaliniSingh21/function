def even(no):
    l=[]
    i=1
    while i<len(no):
        if i%2==0:
            l.append(i)
        i+=1
    return (l)  
print(even( [1, 2, 3, 4, 5, 6, 7, 8, 9]))        
