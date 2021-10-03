# def rev(string):
#     i=0
#     l=[]
#     while i>(-len(string)):
#         l.append(i)
#         i=i-1
#         return (string[-1])
       
# print(rev("1234abcd"))   
# 
#
def rev(string):
    i=0
    l=[]
    while i>(-len(string)):
        l.append(i)
        i=i-1
    return (string[-1])
       
print(rev("1234abcd"))             