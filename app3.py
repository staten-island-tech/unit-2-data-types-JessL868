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

def factors(p):
    print("what are the factors of" ,p,)
    for i in range(1, p + 1):
        if p % i == 0:
            print(i)

def GCF(a, b):
    print("what is the GCF of" ,a, "and" ,b,)
    for i in range(1, a + 1):
        for p in range(1, b + 1):
            if a % i == 0:
                if b % p == 0:
                    if i == p:
                        print(i)
GCF(20, 40)

def truthy(x, y):
    x = True
    y = True
    if type(x) != bool or type(y) != bool:
            print("Error")
    else:
        if x == y:
            print("False")
        elif x != y:
            print("True")
