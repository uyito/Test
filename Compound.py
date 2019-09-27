def comp(a):
    print ("the Compound interest is ", a)
    return a
p = float(input("please enter principal "))
r = float(input("please enter rate "))
n = float(input("please enter compoundings "))
t = float(input("please enter years "))

A = p * ((1 + r / n) ** (n * r))
round(A, 2)
comp(A)