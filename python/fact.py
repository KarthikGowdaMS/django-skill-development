# write a factorial function for a and b

a=5
b=5
# print(a)
# print(b)

def fact(a):
    if a==1:
        return 1

    else:
        return a*fact(a-1)
print(fact(a))
print(fact(b))

