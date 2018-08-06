#!/usr/bin/env python3

import math
import os
from sys import platform


def logo():
    print ("""
████  ████  ███   ██ ██  █  █  █      ██   █  █  █  █  ███
█     █  █  █  █  █ █ █  █  █  █     █  █  █  █  █  █  █ █
███   █  █  ███   █   █  █  █  █     ████  ████  █  █  █  █
█     ████  █  █  █   █   ███  ████  █  █  █  █   ███  ███  v0.09
""")

logo()

def salist():
    print ("""Area/ Surface Area:
Traingle · · · · · : A = 1/2b * h
Circle · · · · · · : A = πr^2
Trapezoid  · · · · : A = 1/2(b1 + b2) * h
Sphere · · · · · · : A = 4πr^2
Square · · · · · · : A = s^2
Rectangle  · · · · : A = l * w
Parallelogram  · · : A = b * h
""")
    
def vollist():
    print ("""Volume Formulas:
Cube · · · · · · · : V = S^3
Rectangular Prism  : V = l * w * h
Square Pyramid · · : V = 1/3(b)^2 * h
Cylinder · · · · · : V = πr^3 * h
Cone · · · · · · · : V = 1/3πr^2 * h
Vol Sphere · · · · : V = 4/3πr^3
""")
    
def triglist():
    print ("""Trig Formulas:
Pythagorean Theorem: c^2 = a^2 + b^2
Slope              : M = y2 - y1 / x2 - x1
Point Distance     : d = sqrt([x2 - x1]^2 + [y2 - y1]^2)

""")
    
def vislist():
    print ("""Visualizers:
30-60-90 Visualizer: '369'
45-45-90 Visualizer: '449'
""")
    
def complist():
    salist()
    vollist()
    triglist()
    vislist()

def resetprog():
    input("Press enter to continue")
    clear()
    logo()
    complist()

def entirething():
    complist()
    deci = 4
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

        def prove449():
            if a == o:
                rtri449()
            else:
                print ("That is not a 45° 45° 90° triangle.")
        
        
        
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
                a = math.pi*r*r
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

    #volume list
        elif form == "cube":
                clogo()
                u = input("Unit type: ")
                s = float(input("Side length: "))
                s = s**3
                s = round(s,deci)
                print ("Volume: " + str(s) + " " + u + " cubed")
                resetprog()

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
                
        elif form == "cylinder":
                clogo()
                u = input("Unit type: ")
                r = float(input("Radius: "))
                h = float(input("Height: "))
                v = h*(math.pi*(r**2))
                v = round(v,deci)
                print ("Volume: " + str(v) + " " + u + " cubed")
                resetprog()
                
        elif form == "cone":
                clogo()
                u = input("Unit type: ")
                h = float(input("Height: "))
                r = float(input("Radius: "))
                v = h*(math.pi*(r**3))/3
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

    #help list
        elif form == "#help":
                clogo()
                print ("""#help: Brings up this list.
#logo  · : Brings up the sick Unicode block logo
#list  · : Brings up the list of all formulas.
#salist  : Brings up Surface Area Formula list
#vollist : Brings up Volume Formula list
#triglist: Brings up Trig Formula list
#vislist : Brings up Visualizer list
#settings: Brings up Settings
""")

        elif form == "#list":
            clogo()
            complist()

        elif form == "#logo":
            clogo()

        elif form == "#info":
            clogo()
            print ("""This program will display a list of formulas to complete mathematical operations.")
Select the name of the formula you require. Default is 4 decimal places, go to #settings to change.")
""")
            
        elif form == "#salist":
            clogo()
            salist()

        elif form == "#vollist":
            clogo()
            vollist()

        elif form == "#trilist":
            clogo()
            trilist()

        elif form == "#vislist":
            clogo()
            vislist()
    #settings list
        elif form == "#settings":
            clogo()
            print("""@deci: Configure the amount of decimal places.
""")

        elif form == "@deci":
            clogo()
            while True:
                try:
                    deci = int(input("Amount of decimal places: "))
                    clogo()
                    complist()
                    break
                except ValueError:
                    print ("Pick an number from 0 - 13.")

        else:
            print ("Please select from #help or #list.")

# automatic OS selection

if platform == "linux" or platform == "linux2":
    def clear():
        _ = os.system('clear')
    def clogo():
        clear()
        logo()
    clogo()
    print ("Type '#help' for commands.")
    print ("")
    entirething()
    
elif platform == "darwin":
    def clear():
        _ = os.system('clear')
    def clogo():
        clear()
        logo()
    clogo()
    print ("Type '#help' for commands.")
    print ("")
    entirething()
    
elif platform == "win32":
    def clear():
        _ = os.system('cls')
    def clogo():
        clear()
        logo()
    clogo()
    print ("Type '#help' for commands.")
    print ("")
    entirething()

