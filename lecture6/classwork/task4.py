def treangle():
	"""Function return area treangle"""
	
	a = float(input("Введіть довжину сторони трикутника "))
	h = float(input("Введіть довжину висоти проведеної до цієї сторони: "))
	print("Area={}".format(0.5 * a *h))
def rectangle():
	"""function return area squere"""
	a = float(input("Введіть значення сторони прямокутника а "))
	b = float(input("Введіть значення сторони прямокутника b "))
	print("Area={}".format(a*b))


def circle():
	"""function return area circle"""
	
	print("Площа кола ",(radius*radius)*Pi)
	Pi = 3.14
	radius = float(input("Введіть радіус кола: "))
	print("sSquere={}".format(Pi * r**2))


figure = input("1-treangle, 2-rectangle, 3-circle: ")
if figure == '1':
	treangle()
elif figure == '2':
	rectangle()
elif figure == '3':
	circle()
else:
	print("input error")
