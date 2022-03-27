try:
    #value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Can't divided anything by zero.")
except ValueError:
    print("Invalid input")