def list_change(no1,no2):
    sym='*'
    j=0
    while j< len(no1) and j<len(no2):
        if sym =='*':
            print(no1[j]*no2[j])
        j=j+1
list_change([4,8,2],[4,6,3])