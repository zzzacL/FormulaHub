import math

print ("████  ████  ███   ██ ██  █  █  █      ██   █  █  █  █  ███ ")
print ("█     █  █  █  █  █ █ █  █  █  █     █  █  █  █  █  █  █ █ ")
print ("███   █  █  ███   █   █  █  █  █     ████  ████  █  █  █  █")
print ("█     ████  █  █  █   █   ███  ████  █  █  █  █   ███  ███  v0.02")


print ("This program will display a list of formulas to complete mathematical operations.")
print ("Select the name of the formula you require.")
print ("")

def salist():
    print ("Surface Area:")
    print ("traingle · · · · · : A = 1/2bh")
    print ("circle · · · · · · : A = πr^2")
    print ("trapezoid  · · · · : A = 1/2(b1 + b2)h")
    print ("sphere · · · · · · : S = 4πr^2")
    
def vollist():
    print ("Volume Formulas:")
    print ("cube · · · · · · · : V = S^3")
    print ("rectangular prism  : V = lwh")
    print ("square pyramid · · : V = 1/3(b)^2 * h")
    print ("cylinder · · · · · : V = πr^3 * h")
    print ("cone · · · · · · · : V = 1/3πr^2 * h")
    print ("sphere · · · · · · : V = 4/3πr^3")
    
def trilist():
    print ("Trig Formulas:")
    print ("pythagorean theorem: a^2 + b^2 = c^2")
    
def vislist():
    print ("Visualizers:")
    print ("30-60-90 Visualizer: '369'")
    
def complist():
    salist()
    print ("")
    vollist()
    print ("")
    trilist()
    print ("")
    vislist()
    print ("")

def rtri369():
    print ("")
    print (str(o) + " u")
    print ("+ _")
    print ("|60°- _")
    print ("|       - _ " + str(h) + " u")
    print ("|           - _")
    print ("|               - _")
    print ("+ - +               - _")
    print ("|90°|                30°- _")
    print ("+ - + - - - - - - - - - - - - ")
    print ("        " + str(a) + " u")
    print ("")



complist()

print ("Type '#help' for commands.")
print ("")

while True:
    form = input("Input: ")
    form = form.lower()

#trig list
    if form == "pythagorean theorem":
            u = input("Unit type: ")
            a = int(input("Side A: "))
            b = int(input("Side B: "))
            h = (a**2 + b**2)**.5
            h = round(h,4)
            print ("Hypotenuse: " + str(h) + " " + u)

#surface area list
    elif form == "triangle":
            u = input("Unit type: ")
            b = int(input("Base: "))
            h = int(input("Height: "))
            a = (b*h)/2
            a = round(a,4)
            print ("Area: " + str(a) + " " + u + " squared")

    elif form == "circle":
            u = input("Unit type: ")
            r = int(input("Radius: "))
            a = math.pi*r*r
            a = round(a,4)
            print ("Area: " + str(a) + " " + u + " squared")

    elif form == "trapezoid":
            u = input("Unit type: ")
            b1 = int(input("Base 1: "))
            b2 = int(input("Base 2: "))
            h = int(input("Height: "))
            a = (h*b1*b2)/2
            a = round(a,4)
            print ("Area: " + str(a) + " " + u + " squared")

    elif form == "sphere":
            u = input("Unit type: ")
            r = int(input("Radius: "))
            s = (4/3)*math.pi*r**3
            s = round(s,4)
            print ("Surface Area: " + str(s) + " " + u + " squared")
            
#volume list
    elif form == "cube":
            u = input("Unit type: ")
            s = int(input("Side length: "))
            s = s**3
            s = round(s,4)
            print ("Volume: " + str(s) + " " + u + " cubed")

    elif form == "rectangular prism":
            u = input("Unit type: ")
            l = int(input("Length: "))
            w = int(input("Width: " ))
            h = int(input("Height: " ))
            v = l*w*h
            v = round(v,4)
            print ("Volume: " + str(v) + " " + u + " cubed")

    elif form == "sqare pyramid":
            u = input("Unit type: ")
            b = int(input("Base: "))
            h = int(input("Height: "))
            v = h*((1/3)*b**2)
            v = round(v,4)
            print ("Volume: " + str(v) + " " + u + " cubed")
            
    elif form == "cylinder":
            u = input("Unit type: ")
            r = int(input("Radius: "))
            h = int(input("Height: "))
            v = h*(math.pi*(r**2))
            v = round(v,4)
            print ("Volume: " + str(v) + " " + u + " cubed")
            
    elif form == "cone":
            u = input("Unit type: ")
            h = int(input("Height: "))
            r = int(input("Radius: "))
            v = h*(math.pi*(r**3))/3
            v = round(v,4)
            print ("Volume: " + str(v) + " " + u + " cubed")
            
    elif form == "sphere":
            u = input("Unit type: ")
            v = round(v,4)
            print ("Volume: " + str(v) + " " + u + " cubed")

#visuzalizer list
    elif form == "369":
            o = int(input("Opposite: "))
            a = int(input("Adjacent: "))
            h = int(input("Hypotenuse: "))
            rtri369()

#help list
    elif form == "#help":
            print ("")
            print ("#help: Brings up this list.")
            print ("#list: Brings up the list of all formulas.")
            print ("#salist: Brings up Surface Area Formula list")
            print ("#vollist: Brings up Volume Formula list")
            print ("#trilist: Brings up Trig Formula list")
            print ("#vislist: Brings up Visualizer list")
            print ("Press Enter to exit.")
            print ("")

    elif form == "#list":
            complist()

    elif form == "#salist":
            salist()

    elif form == "#vollist":
            vollist()

    elif form == "#trilist":
            trilist()

    elif form == "#vislist":
            vislist()

    else:
        print ("Please select from the #list.")

input("Press Enter to exit.")
