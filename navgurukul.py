def my_fun1():
    if no%3==0:
        return('nav')
    elif no%7==0:
        return('gurukul')
    elif no%3==0 and no%7==0:
        return('navgurukul')
no=int(input('enter the no'))
print(my_fun1())