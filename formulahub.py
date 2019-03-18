#!/usr/bin/env python3

import math
import os
from sys import platform

##Defining vital parts of the program

def logo():
    print ("""
████  ████  ███   ██ ██  █  █  █      ██   █  █  █  █  ███
█     █  █  █  █  █ █ █  █  █  █     █  █  █  █  █  █  █ █
███   █  █  ███   █   █  █  █  █     ████  ████  █  █  █  █
█     ████  █  █  █   █   ███  ████  █  █  █  █   ███  ███  v0.11a
""")

#Defining the lists users can choose from

def salist():
    print ("Area/ Surface Area: \nTraingle · · · · · : A = 1/2b * h \nCircle · · · · · · : A = πr^2 \nTrapezoid  · · · · : A = 1/2(b1 + b2) * h \nSquare · · · · · · : A = s^2 \nRectangle  · · · · : A = l * w \nParallelogram  · · : A = b * h \nSphere · · · · · · : SA = 4πr^2 \nCube · · · · · · · : SA = 6s^2 \nCylinder · · · · · : SA = 2πrh \n")

def vollist():
    print ("Volume Formulas: \nRectangular Prism  : V = l * w * h \nSquare Pyramid · · : V = 1/3(b)^2 * h \nCone · · · · · · · : V = 1/3πr^2 * h \nVol Sphere · · · · : V = 4/3πr^3 \nVol Cube · · · · · : V = S^3 \nVol Cylinder · · · : V = πr^3 * h\n")

def triglist():
    print ("Trig Formulas: \nPythagorean Theorem: C = sqrt(a^2 + b^2) \nSlope/ Angle · · · : M = y2 - y1 / x2 - x1 \nPoint Distance · · : D = sqrt([x2 - x1]^2 + [y2 - y1]^2) \n")

def al2list():
    print ("Algebra II Formulas: \nMultiply Powers  · : a^(m+n) = (a^m)(a^n) \nDivide Powers  · · : a^(m-n) = (a^m)/(a^n) \nDiscriminant · · · : D = b^2 - 4ac \nQuadratic Formula  : X = -b +/- sqrt(b^2 - 4ac) / 2a \n")

def vislist():
    print ("Visualizers: \n30-60-90 Visualizer: '369' \n45-45-90 Visualizer: '449' \nPascal's Triangle  : 'ptri' \n")

#Defining a composition of the before lists

def complist():
    salist()
    vollist()
    triglist()
    al2list()
    vislist()

#Defining the reset feature for when a formula completes. The clear() function
#is defined before this loop is executed

def resetprog():
    print("")
    input("Press enter to continue ")
    clear()
    logo()
    complist()

##The program itself is one big while loop that will be executed later

def main():
    complist()
    deci = 4
    ptri = 9
    while True:

        def rtri369():
            print ("""
"""+ str(o) + """ u
█▀▄▄
█   ▀▀▄▄
█60°    ▀▀▄▄ """ + str(h) + """ u
█           ▀▀▄▄
█               ▀▀▄▄
█▀▀▀▀█              ▀▀▄▄
█90° █               30°▀▀▄▄
█▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██▄▄ """ + str(a) + """ u
""")

#With these two triangles I have added provexxx() functions to make sure that
#the user is inputting a proper triangle, which was easy because it's based off
#the "legs" of the triangles, 1:1 on the 45° and 1:2 on the 30° 60° 90°

        def prove369():
            if a == o*2:
                rtri369()
                resetprog()
            else:
                print ("That is not a 30° 60° 90° triangle.")

        def rtri449():
            print ("""
"""+ str(o) + """ u
█▀▄
█  ▀▄
█45° ▀▄ """ + str(h) + """ u
█      ▀▄
█        ▀▄
█▀▀▀▀█     ▀▄
█90° █    45°▀▄
█▄▄▄▄█▄▄▄▄▄▄▄▄▄█▄ """+ str(a) + """ u
""")

        def finish():
            clogo()
            complist()

        def prove449():
            if a == o:
                rtri449()
            else:
                print ("That is not a 45° 45° 90° triangle.")

#Turning the user input into a more manageable type casing

        form = input("Input: ")
        form = form.lower()

#trig list

        if form == "pythagorean theorem":
                clogo()
                u = input("Unit type: ")
                a = float(input("Side A: "))
                b = float(input("Side B: "))
                h = math.sqrt(a**2 + b**2)
                h = round(h,deci)
                print ("Hypotenuse: " + str(h) + " " + u)
                resetprog()

        if form == "slope":
                clogo()
                x = float(input("X1: "))
                y = float(input("Y1: "))
                xx = float(input("X2: "))
                yy = float(input("Y2: "))
                t = yy - y
                b = xx - x
                try:
                    m = t/b
                    m = round(m,deci)
                    print ("Slope: " + str(m) + ", or: " + str(t) + "/" + str(b))
                except ZeroDivisionError:
                    print ("Cannot divide by zero")

#Since slope is closely related to the angle of a line, I decided to add an
#option for the angle if possible (can possibly be simplified)

                yn = input("Angle? (y/n): ")
                while yn == "y":
                    if yn == "y":
                        if b == 0.0:
                            print ("Cannot divide by zero")
                            resetprog()
                            break
                        else:
                            em = round(math.degrees(math.atan(m)),deci)
                            while em < 0:
                                if em < 0:
                                    em = em + 360
                                    em = round(em,deci)
                                    break
                                    resetprog()
                            print ("Angle: " + str(em) + "°")
                            resetprog()
                            break
                    elif yesno == "n":
                        resetprog()
                    else:
                        print ("(y/n)")

        if form == "point distance":
                clogo()
                x = float(input("X1: "))
                y = float(input("Y1: "))
                xx = float(input("X2: "))
                yy = float(input("Y2: "))
                g1 = (xx - x)**2
                g2 = (yy - y)**2
                d = math.sqrt(g1 + g2)
                d = round(d,deci)
                print ("The distance is: " + str(d) + " units.")
                resetprog()

    #surface area list

        elif form == "triangle":
                clogo()
                u = input("Unit type: ")
                b = float(input("Base: "))
                h = float(input("Height: "))
                a = (b*h)/2
                a = round(a,deci)
                print ("Area: " + str(a) + " " + u + " squared")
                resetprog()

        elif form == "circle":
                clogo()
                u = input("Unit type: ")
                r = float(input("Radius: "))
                a = math.pi*(r**2)
                a = round(a,deci)
                print ("Area: " + str(a) + " " + u + " squared")
                resetprog()

        elif form == "trapezoid":
                clogo()
                u = input("Unit type: ")
                b1 = float(input("Base 1: "))
                b2 = float(input("Base 2: "))
                h = float(input("Height: "))
                a = (h*b1*b2)/2
                a = round(a,deci)
                print ("Area: " + str(a) + " " + u + " squared")
                resetprog()

        elif form == "sphere":
                clogo()
                u = input("Unit type: ")
                r = float(input("Radius: "))
                s = 4*math.pi*r**2
                s = round(s,deci)
                print ("Surface Area: " + str(s) + " " + u + " squared")
                resetprog()

        elif form == "square":
                clogo()
                u = input("Unit type: ")
                s = float(input("Side: "))
                a = s**2
                a = round(a,deci)
                print ("Area: " + str(a) + " " + u + " squared")
                resetprog()

        elif form == "rectangle":
                clogo()
                u = input("Unit type: ")
                l = float(input("Length: "))
                w = float(input("Width: "))
                a = l*w
                a = round(a,deci)
                print ("Area: " + str(a) + " " + u + " squared")
                resetprog()

        elif form == "parallelogram":
                clogo()
                u = input("Unit type: ")
                b = float(input("Base: "))
                h = float(input("Height: "))
                a = b*h
                a = round(a,deci)
                print ("Area: " + str(a) + " " + u + " squared")
                resetprog()

        elif form == "cube":
                clogo()
                u = input("Unit type: ")
                s = float(input("Side: "))
                a = 6*(s**2)
                a = round(a,deci)
                print ("Surface area: " + str(a) + " " + u + " squared")
                resetprog()

        elif form == "cylinder":
                clogo()
                u = input("Unit type: ")
                r = float(input("Radius: "))
                h = float(input("Height: "))
                a = 2*(math.pi*r*h)
                a = round(a,deci)
                print ("Surface area: " + str(a) + " " + u + " squared")
                resetprog()

    #volume list

        elif form == "rectangular prism":
                clogo()
                u = input("Unit type: ")
                l = float(input("Length: "))
                w = float(input("Width: " ))
                h = float(input("Height: " ))
                v = l*w*h
                v = round(v,deci)
                print ("Volume: " + str(v) + " " + u + " cubed")
                resetprog()

        elif form == "sqare pyramid":
                clogo()
                u = input("Unit type: ")
                b = float(input("Base: "))
                h = float(input("Height: "))
                v = h*((1/3)*b**2)
                v = round(v,deci)
                print ("Volume: " + str(v) + " " + u + " cubed")
                resetprog()

        elif form == "cone":
                clogo()
                u = input("Unit type: ")
                h = float(input("Height: "))
                r = float(input("Radius: "))
                v = ((math.pi/3)*(r**2))*h
                v = round(v,deci)
                print ("Volume: " + str(v) + " " + u + " cubed")
                resetprog()

        elif form == "vol sphere":
                clogo()
                u = input("Unit type: ")
                r = float(input("Radius: "))
                v = (4/3)*(math.pi*(r**3))
                v = round(v,deci)
                print ("Volume: " + str(v) + " " + u + " cubed")
                resetprog()

        elif form == "vol cube":
                clogo()
                u = input("Unit type: ")
                s = float(input("Side length: "))
                s = s**3
                s = round(s,deci)
                print ("Volume: " + str(s) + " " + u + " cubed")
                resetprog()

        elif form == " vol cylinder":
                clogo()
                u = input("Unit type: ")
                r = float(input("Radius: "))
                h = float(input("Height: "))
                v = h*(math.pi*(r**2))
                v = round(v,deci)
                print ("Volume: " + str(v) + " " + u + " cubed")
                resetprog()

    #visualizer list

        elif form == "369":
                clogo()
                o = float(input("Opposite: "))
                a = float(input("Adjacent: "))
                h = math.sqrt(o**2 + a**2)
                h = round(h,deci)
                prove369()
                resetprog()

        elif form == "449":
                clogo()
                o = float(input("Opposite: "))
                a = float(input("Adjacent: "))
                h = math.sqrt(o**2 + a**2)
                h = round(h,deci)
                prove449()
                resetprog()

        elif form == "ptri":
                clogo()
                ptrilist=["0                               01 ", "1                             1    1", "2                            1  02  1", "3                          1  3    3  1", "4                        1  4   06   4  1", "5                      1  5  10    10  5  1", "6                    1  6  15   20   15  6  1", "7                  1  7  21  35    35  21  7  1", "8                1  8  28  56   70   56  28  8  1", "9             1  9  36  84  126    126  84  36  9  1", "10        1  10  45  120  210  252   210  120  45  10  1", "11     1  11  55  165  330  462    462  330  165  55  11  1", "12  1  12  66  220  495  792   924    792  495  220  66  12  1", ]
                for item in ptrilist[0:ptri]:
                    print(item)
                print("")
                resetprog()

        

    #algebra 2 list

        if form == "multiply powers":
                clogo()
                a = float(input("Base(a): "))
                m = float(input("m: "))
                n = float(input("n: "))
                o = a**(m+n)
                o = round(o,deci)
                print ("Product: %s" % o)
                resetprog()

        if form == "divide powers":
                clogo()
                a = float(input("Base(a): "))
                m = float(input("m: "))
                n = float(input("n: "))
                o = a**(m-n)
                o = round(o,deci)
                print ("Product: %s" % o)
                resetprog()

        if form == "discriminant":
                clogo()
                b = float(input("B: "))
                a = float(input("A: "))
                c = float(input("C: "))
                d = (b**2) - (4*a*c)
                if d > 0:
                    print ("Two distinct real roots.")
                    resetprog()
                elif d == 0:
                    print ("One distinct real root/ two equal real roots")
                elif d < 0:
                    print ("No real roots")

#the infamous quadratic formula(could be simplified i know)

        if form == "quadratic formula":
                clogo()
                b = float(input("B: "))
                a = float(input("A: "))
                c = float(input("C: "))
                x = (math.sqrt((b**2) - (4*a*c)) - b) / (2*a)
                x = round(x,deci)
                negx = math.sqrt((b**2) - (4*a*c))
                negx = (-b - negx) / (2*a)
                negx = round(negx,deci)
                print ("+X: " + str(x))
                print ("-X: " + str(negx))
                resetprog()

    #add a list to sort out a list of numbers
    #maybe do mean, med and mode (iteration)

    #help list

        elif form == "#help":
                clogo()
                print ("#logo  · : Brings up the sick Unicode block logo \n#list  · : Brings up the list of all formulas. \n#salist  : Brings up Surface Area Formula list \n#vollist : Brings up Volume Formula list \n#triglist: Brings up Trig Formula list \n#vislist : Brings up Visualizer list \n#settings: Brings up Settings \n")

        elif form == "#list":
            clogo()
            complist()

        elif form == "#logo":
            clogo()

        elif form == "#info":
            clogo()
            print ("This program will display a list of formulas to complete mathematical operations.\n")

        elif form == "#salist":
            clogo()
            salist()

        elif form == "#vollist":
            clogo()
            vollist()

        elif form == "#triglist":
            clogo()
            triglist()

        elif form == "#al2list":
            clogo()
            al2list()

        elif form == "#vislist":
            clogo()
            vislist()

    #settings list

        elif form == "#settings":
            clogo()
            print("@deci: Configure the amount of decimal places. \n@ptri: Configure the levels of Pascal's Triangle.\n")

        elif form == "@deci":
            clogo()
            while True:
                try:
                    deci = int(input("Amount of decimal places(0 - 13): "))
                    finish()
                    break
                except ValueError:
                    print ("Pick a number from 0 - 13.")

        elif form == "@ptri":
            clogo()
            while True:
                try:
                    ptri = int(input("Levels of Pascal's Triangle(0 - 12): "))
                    ptri = ptri + 1
                    finish()
                    break
                except ValueError:
                    print ("Pick a number from 0 - 12.")
                    

        else:
            print ("Please select from #help or #list.")

#End of the main program, funnily enough none of the past 400 lines would matter
#without a simple OS selection area, it might make more sense to locate this at
#the top of the program but it works as of now so I'm not going to mess with it
#for now :) maybe in the future windows will use "clear" instead of "cls"

# automatic OS selection

if platform == "linux" or platform == "linux2" or platform == "darwin":
    def clear():
        _ = os.system('clear')
    def clogo():
        clear()
        logo()
    clogo()
    print ("Type '#help' for commands.")
    print ("")
    main()

elif platform == "win32":
    def clear():
        _ = os.system('cls')
    def clogo():
        clear()
        logo()
    clogo()
    print ("Type '#help' for commands.")
    print ("")
    main()
