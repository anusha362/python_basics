def input_numbers():
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    return a,b

x,y=input_numbers()

try:
    print(x//y)
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("its final")