def max_print(x,y):
	'''function return max number'''
	if x > y:
		print(x)
	elif x == y:
		print("x = y")
	else:
		print(y)
x = int(input("X = "))
y = int(input("Y = "))

max_print(x,y)
print(max_print.__doc__)
