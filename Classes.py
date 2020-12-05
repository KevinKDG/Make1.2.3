#!/usr/bin/env python
"""
Information about the script goes here
"""


#               IMPORTS               #


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
def main():
    class Liedje:
        def __init__(self, lyrics):
            self.lyrics = lyrics

        def zingen(self):
            return verjaardagslied.lyrics


    verjaardagslied = Liedje("""Er is er één jarig, hoera, hoera
dat kun je wel zien: dat is hij.
Dat vinden wij allen zo prettig, ja ja
en daarom zingen wij blij.

Hij leve lang, hoera, hoera
hij leve lang, hoera
hij leve lang, hoera, hoera
hij leve lang, hoera!
    """)
    print(verjaardagslied.lyrics)


if __name__ == '__main__':    # run tests if called from command-line
    main()