import math
a=int(input("Primul nr: "))
b=int(input("Al 2 nr: "))
c=int(input("Al 3 nr: "))
d=int(input("Al 4 nr: "))

def triun():

    if (a+b>c) or (a+c>b) or (b+c>a):
        p=a+b+c
        sp=p/2
        aria=math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
        return p,aria 
    if (x+y>q) or (x+q>y) or (q+y>x):
        p=x+y+q
        sp=p(x,y,q)/2
        aria=math.sqrt(sp*(sp-x)*(sp-y)*(sp-q))
        return p,aria
    if (y+z>q) or (y+q>z) or (q+z>y):
        p=y+z+q
        sp=p(y,z,q)/2    
        aria=math.sqrt(sp*(sp-y)*(sp-z)*(sp-q))
        return p,aria
    if (x+z>q) or (x+q>z) or (z+q>x):
        p=x+z+q
        sp=p(x,y,z)/2    
        aria=math.sqrt(sp*(sp-x)*(sp-z)*(sp-q))
        return p,aria
    else:
        return "Nu pot forma un triunghi "

print (triun())
