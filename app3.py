def floats():
    x = 3
    y = float(3)
    print(x,y)

def lists():
        values = [1,2.23,5,7,2,30,15]
        print(values)
        for i in values:
            print(i)
        print(values[6])

def string_methods():
    x = "this is a thing"
    y = x.split( )
    z = y[0]
    print(y)
    print(z)

def how_many_words():
    b = input("please put a sentence")
    c = b.split() 
    print(len(c))

def odd_or_even():
    a = 60 % 2
    if a == 0:
        print("even")
    else: 
        print("odd")

def bill():
    m = input("What tip would you like to offer?")
    if m == "0%":
         print("bad")
    elif m == "15%":
        print("okay")
    elif m == "20%":
        print("good")
    elif m == ("25%"):
        print("great")

def factors():
    a = input("please type a number")
    range(1, a + 1)
    for i in a:
        if a % range == 0:
            print ()
def traffic():
    c = input("Can the traffic go?")
    a = "Eastbound Traffic"
    b = "Westbound Traffic"
    if c == a:
        print("yes")
    elif c == b:
        print("yes")
    elif c == a and b:
        print("no")
    else:
        print("no")
traffic()