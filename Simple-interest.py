def simple(z):
    print ("your simple interest is", z)
    return z

p = int(input("please enter p "))
r = float(input("please enter r "))
t = int(input("please enter t "))


z = p * r * t
simple(z)