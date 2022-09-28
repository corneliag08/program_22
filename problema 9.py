import math
a=int(input("Dati latura 1: "))
b=int(input("Dati latura 2: "))
c=int(input("Dati latura 3: "))



def inaltime(x,y,z):
    if ((x+y>z) and (x+z>y) and (z+y>x)):
        p=x+y+z
        sp=p/2
        aria=round(math.sqrt(sp*(sp-x)*(sp-y)*(sp-z)),3)
        hx=round((2*aria)/x,3)
        hy=round((2*aria)/y,3)
        hz=round((2*aria)/z,3)
        return print("Inaltimea triunghiului pe latura cu lungimea",a,"are lungimea:",hx, ".Inaltimea triunghiului pe latura cu lungimea",y,"are lungimea",hy,".Inaltimea triunghiului pe latura cu lungimea",z,"are lungimea",hz)
    else:
        return print("Laturile date nu pot forma un triunghi")

(inaltime(a,b,c))