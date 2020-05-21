print("Enter number for factorial calculation")
number = int(input("Number: "))
result =1
for i in range(1,number+1):
	result*=i
print("Factorial number {} is {} ".format(number,result))