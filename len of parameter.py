def function(a,b):
	len1=len(a)
	len2=len(b)
	if len1>len2:
		print(a,'is greater than',b)
	elif len2>len1:
		print(b, 'is greater than',a)
	else:
		print("both length equal")
		print(a)
		print(b)
a=input("enter a name")
b=input("enter a name")
function(a,b)