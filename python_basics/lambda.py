
z=lambda y:y*y
print(z(3))

def func(val):
    va=lambda y,q,w,e:y*q*w+val*e*e
    return va

name=func(10)

print(name(10,10,10,10))