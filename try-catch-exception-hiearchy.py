try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")
 
print("THE END.")

try:
    y = 1 / 0
#since this is more specific...this exception will be handled by this except
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")


try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")
 
print("THE END.")
 