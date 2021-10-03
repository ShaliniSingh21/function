def harshad_no():
    sum=0
    r=0
    while no>0:
        r=no%10
        num=no//10
        sum=sum+r
    if no%sum==0:
        print('harshad no hai') 
    else:
        ('harshad no nhi hai')
no=int(input('enter the no'))        
harshad_no()
                             