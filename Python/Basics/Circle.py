# -*- coding: utf-8 -*- 

import turtle

def main():
    window = turtle.Screen()
    tortuga = turtle.Turtle()

    make_square(tortuga)

    input()

def make_square(tortuga):
    length = float(input('Cuanto mide la arista \n'))
    for i in range(360):
        make_line_and_turn(tortuga, length)

def make_line_and_turn(tortuga, length):
    tortuga.forward(length)
    tortuga.left(1)
    

if __name__ == '__main__':

    main()