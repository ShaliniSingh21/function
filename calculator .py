def my_fun():
    num1=int(input('enter trhe no'))
    num2=int(input('enter the no'))
    sym=(input('enter the symbol'))
    if sym=="+":
        return(num1+num2)
    elif sym=='-':
        return(num1-num2)
    elif  sym=='*':
        return(num1*num2)  
    elif sym=='/':
        return(num1/num2) 
    else:
        return('stop') 
print(my_fun())                  