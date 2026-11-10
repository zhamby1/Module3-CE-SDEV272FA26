import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)


#check calculations
x = 7
y = 5
sum = x + y
assert sum == 12 #nothing will happen because it meats this assertion
print(sum)