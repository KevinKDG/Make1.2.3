#!/usr/bin/env python
"""
Een re-make van je rekenmachine die voldoet aan flowcontrol.

    Je vraagt de gebruiker om 2 getallen
    Je vraagt de gebruiker om een bewerking op te geven
    Je geeft correcte output

"""

#               IMPORTS               #
import time

#          AUTHOR INFORMATION         #

#        _____
#      .'     `.
#     /  .-=-.  \   \ __
#     | (  C\ \  \_.'')
#     _\  `--' |,'   _/
#    /__`.____.'__.-' The coding snail~

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__Version__ = "(Code version)"
__status__ = "Finished"


#              VARIABLES              #


#              MAIN CODE              #
def error():
    print('this is not a valid number, Please try again')    # Print this message if the input was not a number
    time.sleep(0.5)
    main()


def addition(number_1, number_2):
    """addition of the two numbers"""

    print(number_1, "+", number_2, "is", number_1 + number_2)  # Do the calculation
    time.sleep(0.5)

    again = input("Do you want to calculate again?[yes/no]\n ")  # asks the user to calculate again
    if again == "yes":
        main()
    else:
        print("Goodbye")


def subtraction(number_1, number_2):
    """subtraction of the two numbers"""

    print(number_1, "-", number_2, "is", number_1 - number_2)
    time.sleep(0.5)

    again = input("Do you want to calculate again?[yes/no]\n ")
    if again == "yes":
        main()
    else:
        print("Goodbye")


def multiplication(number_1, number_2):
    """multiplication of the two numbers"""

    print(number_1, "*", number_2, "is", number_1 * number_2)
    time.sleep(0.5)

    again = input("Do you want to calculate again?[yes/no]\n ")
    if again == "yes":
        main()
    else:
        print("Goodbye")


def division(number_1, number_2):
    """division of the two numbers"""

    print(number_1, "/", number_2, "is", number_1 / number_2)
    time.sleep(0.5)

    again = input("Do you want to calculate again?[yes/no]\n ")
    if again == "yes":
        main()
    else:
        print("Goodbye")


def main():
    try:
        number_1 = int(input("Pick a number: "))  # Input, pick your first number
        number_2 = int(input("Pick another number: "))  # Input, it lets you pick a second number

        what = input('''What would you like to do?              

            + for addition
            - for subtraction
            * for multiplication
            / for division
            ''')
        if what == "+":
            addition(number_1, number_2)

        elif what == '-':
            subtraction(number_1, number_2)

        elif what == '*':
            multiplication(number_1, number_2)

        elif what == '/':
            division(number_1, number_2)

    except ValueError:
        error()


if __name__ == '__main__':  # run tests if called from command-line
    main()