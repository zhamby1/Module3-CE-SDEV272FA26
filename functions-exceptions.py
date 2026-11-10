def divide_numbers(num):
    try:
        return 1 / num
    except ArithmeticError:
        print("Cannot calculate number..divide by zero")
    return None


answer = divide_numbers(0)
print(answer)

def divide_number_outside(num):
    return 1 / num


try:
    answer = divide_number_outside(0)
    print(answer)
except ArithmeticError:
    print("Cannot divide by zero")