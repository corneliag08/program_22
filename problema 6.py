import math


def triunghiuri(a,b,c,d):
    if ((a+b>c) and (b+c>a) and (a+c>b)):
        p=a+b+c
        sp=(a+b+c)/2
        aria=math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
        return print(a,',',b,',',c, "pot forma un triunghi și perimetrul acestuia este: ",p,", iar aria este: ",aria)
    if ((a+b>d) and (b+d>a)  and (a+d>b)):
        p=a+b+d
        sp=(a+b+d)/2
        aria=math.sqrt(sp*(sp-a)*(sp-b)*(sp-d))
        return print(a,',',b,',',d, "pot forma un triunghi și perimetrul acestuia este: ",p,", iar aria este: ",aria)
    if ((c+b>d) and (c+d>b) and (d+b>c)):
        p=b+c+d
        sp=(b+c+d)/2
        aria=math.sqrt(sp*(sp-c)*(sp-b)*(sp-d))
        return print(b,',',c,',',d, "pot forma un triunghi și perimetrul acestuia este: ",p,", iar aria este: ",aria)
    if (c+a>d) and (c+d>a) and (a+d>c):
        p=a+c+d
        sp=(a+c+d)/2
        aria=round(math.sqrt(sp*(sp-c)*(sp-a)*(sp-d)),3)
        return print(a,',',c,',',d, "pot forma un triunghi și perimetrul acestuia este: ",p,", iar aria este: ",aria)
    else:
        print("Numerele date nu pot fi laturi ale unui triunghi")

x=int(input("Dati I-ul nr: "))
y=int(input("Dati II-a nr: "))
z=int(input("Dati III-a nr: "))
q=int(input("Dati IV-a nr: "))


(triunghiuri(x,y,z,q))
