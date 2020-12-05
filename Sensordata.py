#!/usr/bin/env python
"""
Information about the script goes here
"""


#               IMPORTS               #
import random
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
__status__ = "Development"

#              VARIABLES              #


#              MAIN CODE              #


def average(random_data):
    return sum(random_data) / len(random_data)  # Calculate the average from the list


def sensor():
    try:
        random_data = []
        for items in range(0, 21):
            time.sleep(0.3)
            data = random.randint(1, 25)         # value between 1 & 25
            random_data.append(data)
            print(random_data)

    except KeyboardInterrupt as p:
        exit()

    print("The average of this list is: ", average(random_data))


if __name__ == '__main__':    # run tests if called from command-line
    sensor()