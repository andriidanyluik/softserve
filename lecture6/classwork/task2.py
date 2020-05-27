def absolut_value(num):
	"""function return absolut value of number"""
	if num >= 0:
		return num
	else:
		return -num
num = int(input("Enter: "))
print(absolut_value(num))