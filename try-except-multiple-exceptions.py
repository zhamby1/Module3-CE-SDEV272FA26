try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)

    
#these are built in error in python - zero division means cannot divide by zero
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
#value error in this case means it has to be a numerical type (int)
except ValueError:
    print("You must enter an integer value.")

#this except is when neither of the above happens but we get an error
except:
    print("Oh dear, something went wrong...")

print("THE END.")