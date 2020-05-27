def factorial(number,result):
	'''This func search factorial number x'''
	result = 1
	for i in range(1,number+1):
		result*=i
number = int(input("Enter number: "))
print(factorial(number)
