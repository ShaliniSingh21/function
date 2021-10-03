def weight():
    bmi=int(input('enter the weight'))
    if bmi <= 18: 
        return "Underweight"
    elif bmi <= 25: 
        return "Normal"
    elif bmi < 30: 
        return "Overweight"
    elif bmi > 30:
        return "Obese"
    else:
        return 'nothing'    
print(weight())                        

