def shownumber(limit):
	i=0
	while i<=limit:
		if i%2==0:
			print("even no",i)
		elif i%2!=0:
			print("odd no",i)
		i=i+1
shownumber(3)