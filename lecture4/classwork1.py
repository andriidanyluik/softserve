print("Enter two number: ")
first_number = int(input("first number "))
second_number = int(input("second number "))
if first_number > second_number:
	print("{} > {}".format(first_number,second_number))
elif first_number < second_number:
	print("{} < {}".format(first_number,second_number))
else:
	if first_number == second_number:
		print("{} = {}".format(first_number,second_number))

print("Good work!")