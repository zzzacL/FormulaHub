import math
import os

def logo():
    print ("""
████  ████  ███   ██ ██  █  █  █      ██   █  █  █  █  ███
█     █  █  █  █  █ █ █  █  █  █     █  █  █  █  █  █  █ █
███   █  █  ███   █   █  █  █  █     ████  ████  █  █  █  █
█     ████  █  █  █   █   ███  ████  █  █  █  █   ███  ███  v0.08.5
""")

logo()

def salist():
    print ("""Surface Area:
traingle · · · · · : A = 1/2bh
circle · · · · · · : A = πr^2
trapezoid  · · · · : A = 1/2(b1 + b2)h
sphere · · · · · · : S = 4πr^2
""")
    
def vollist():
    print ("""Volume Formulas:
cube · · · · · · · : V = S^3
rectangular prism  : V = lwh
square pyramid · · : V = 1/3(b)^2 * h
cylinder · · · · · : V = πr^3 * h
cone · · · · · · · : V = 1/3πr^2 * h
vol sphere · · · · : V = 4/3πr^3
""")
    
def trilist():
    print ("""Trig Formulas:
pythagorean theorem: a^2 + b^2 = c^2
""")
    
def vislist():
    print ("""Visualizers:
30-60-90 Visualizer: '369'
45-45-90 Visualizer: '449'
""")
    
def complist():
    salist()
    vollist()
    trilist()
    vislist()

def resetprog():
    input("Press enter to continue")
    clear()
    logo()
    complist()

def entirething():
    complist()
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
                h = round(h,4)
                print ("Hypotenuse: " + str(h) + " " + u)
                resetprog()

    #surface area list
        elif form == "triangle":
                clogo()
                u = input("Unit type: ")
                b = int(input("Base: "))
                h = int(input("Height: "))
                a = (b*h)/2
                a = round(a,4)
                print ("Area: " + str(a) + " " + u + " squared")
                resetprog()

        elif form == "circle":
                clogo()
                u = input("Unit type: ")
                r = int(input("Radius: "))
                a = math.pi*r*r
                a = round(a,4)
                print ("Area: " + str(a) + " " + u + " squared")
                resetprog()

        elif form == "trapezoid":
                clogo()
                u = input("Unit type: ")
                b1 = int(input("Base 1: "))
                b2 = int(input("Base 2: "))
                h = int(input("Height: "))
                a = (h*b1*b2)/2
                a = round(a,4)
                print ("Area: " + str(a) + " " + u + " squared")
                resetprog()

        elif form == "sphere":
                clogo()
                u = input("Unit type: ")
                r = int(input("Radius: "))
                s = 4*math.pi*r**2
                s = round(s,4)
                print ("Surface Area: " + str(s) + " " + u + " squared")
                resetprog()
                
    #volume list
        elif form == "cube":
                clogo()
                u = input("Unit type: ")
                s = int(input("Side length: "))
                s = s**3
                s = round(s,4)
                print ("Volume: " + str(s) + " " + u + " cubed")
                resetprog()

        elif form == "rectangular prism":
                clogo()
                u = input("Unit type: ")
                l = int(input("Length: "))
                w = int(input("Width: " ))
                h = int(input("Height: " ))
                v = l*w*h
                v = round(v,4)
                print ("Volume: " + str(v) + " " + u + " cubed")
                resetprog()

        elif form == "sqare pyramid":
                clogo()
                u = input("Unit type: ")
                b = int(input("Base: "))
                h = int(input("Height: "))
                v = h*((1/3)*b**2)
                v = round(v,4)
                print ("Volume: " + str(v) + " " + u + " cubed")
                resetprog()
                
        elif form == "cylinder":
                clogo()
                u = input("Unit type: ")
                r = int(input("Radius: "))
                h = int(input("Height: "))
                v = h*(math.pi*(r**2))
                v = round(v,4)
                print ("Volume: " + str(v) + " " + u + " cubed")
                resetprog()
                
        elif form == "cone":
                clogo()
                u = input("Unit type: ")
                h = int(input("Height: "))
                r = int(input("Radius: "))
                v = h*(math.pi*(r**3))/3
                v = round(v,4)
                print ("Volume: " + str(v) + " " + u + " cubed")
                resetprog()
                
        elif form == "vol sphere":
                clogo()
                u = input("Unit type: ")
                r = float(input("Radius: "))
                v = (4/3)*(math.pi*(r**3))
                v = round(v,4)
                print ("Volume: " + str(v) + " " + u + " cubed")
                resetprog()

    #visualizer list
        elif form == "369":
                clogo()
                o = float(input("Opposite: "))
                a = float(input("Adjacent: "))
                h = math.sqrt(o**2 + a**2)
                h = round(h,4)
                prove369()
                resetprog()

        elif form == "449":
                clogo()
                o = float(input("Opposite: "))
                a = float(input("Adjacent: "))
                h = math.sqrt(o**2 + a**2)
                h = round(h,4)
                prove449()
                resetprog()

    #help list
        elif form == "#help":
                clogo()
                print ("""#help: Brings up this list.
#logo: brings up the sick Unicode block logo
#list: Brings up the list of all formulas.
#salist: Brings up Surface Area Formula list
#vollist: Brings up Volume Formula list
#trilist: Brings up Trig Formula list
#vislist: Brings up Visualizer list
""")

        elif form == "#list":
            clogo()
            complist()

        elif form == "#logo":
            clogo()

        elif form == "#info":
            clogo()
            print ("""This program will display a list of formulas to complete mathematical operations.")
Select the name of the formula you require.")
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

        else:
            print ("Please select from #help or #list.")


while True:
    opsys = input("Win/Lin/Mac: ")
    opsys = opsys.lower()

    if opsys == "win":
        def clear():
            _ = os.system('cls')
        def clogo():
            clear()
            logo()
        clogo()
        print ("Type '#help' for commands.")
        print ("")
        entirething()
    elif opsys == "lin":
        def clear():
            _ = os.system('clear')
        def clogo():
            clear()
            logo()
        clogo()
        print ("Type '#help' for commands.")
        print ("")
        entirething()
    elif opsys == "mac":
        def clear():
            _ = os.system('clear')
        def clogo():
            clear()
            logo()
        clogo()
        print ("Type '#help' for commands.")
        print ("")
        entirething()
    else:
        print ("Pick a proper OS my dude.")
