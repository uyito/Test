print ("hi my name is aghasomwan osahumen")
print ("Enter 1 for Simple Interest")
print ("Enter 2 for Compound Interest ")
print ("Enter 3 for Effective rate ")

num = int(input("enter the number of the one you wish to calculate "))

if num == 1:
    import Simple
    z = 0
    print (Simple.simple(z))
elif num == 2:
    import Compound
    A = 0
    print (Compound.comp(A))
#elif num == 3: