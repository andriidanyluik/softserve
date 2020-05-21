print("enter your four significant number for product: ")
a = int(input())
mult = 1
while (a != 0):
    mult = mult * (a % 10)
    a = a // 10
print("result: ", mult)

print("enter your number for reverse: ")
a = input()
a = list(a)
a.reverse()
a = ''.join(a)
print("reverse number: ", a)

print("enter your four for sorted: ")
a = input()
a = list(a)
a = sorted(a)
a = ''.join(a)
print("sorted number: ", a)