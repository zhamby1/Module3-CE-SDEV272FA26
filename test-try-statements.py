def divide_number(n):
    raise ZeroDivisionError


try:
    divide_number(3)
except ArithmeticError:
    print("What happened? An error?")


print("THE END.")