# Error handling
from typing import Type


def enter_number():
    age = int(input("What is your age? "))
    print(10/age)

while True:
    try:
        enter_number()
    except (ValueError, TypeError):
        print("please enter a number \n")
        continue
    except ZeroDivisionError:
        print("please enter a number greater than zero\n")
        continue
    else:
        print('Thank you.')
        break
    finally:
        print("The error handling is done.")