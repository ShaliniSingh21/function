def no():
    #no1=[1, 342, 75, 23, 98]
    #no2=[75, 23, 98, 12, 78, 10, 1]
    i=0
    l=[]
    while i<len(no1) and i<len(no2):
        if no1[i] == no2[i]:
            l.append (no1[i]) and (no2[i])
            i=i+1
        print(l)
no1=[1, 342, 75, 23, 98]
no2=[75, 23, 98, 12, 78, 10, 1]            
print(no())            
            