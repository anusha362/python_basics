# x=lambda a:a+3
# print(x(5))

# y=lambda a,b:a*b
# print(y(3,4))

def multiply(n):
    return lambda a:a*n
num1=multiply(6)
print(num1(11))
num2=multiply(7)
print(num2(11))
