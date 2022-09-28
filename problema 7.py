a=int(input("Dati latura 1: "))
b=int(input("Dati latura 2: "))
c=int(input("Dati latura 3: "))


import math
def mediana(x,y,z):
    if (x+y>z) and (z+x>y) and (y+z>x):
        mx=round(0.5*(math.sqrt((2*(y**2))+(2*(z**2))-(x**2))),3)
        my=round(0.5*(math.sqrt((2*(x**2))+(2*(z**2))-(y**2))),3)
        mz=round(0.5*(math.sqrt((2*(y**2))+(2*(x**2))-(z**2))),3)
        return print("Mediana laturei :",x, "are lungimea:",mx,"; mediana laturei :",b, "are lungimea",my,",mediana laturei :",c, "are lungimea",mz)
    else:
        return print("Laturile date nu pot forma un triunghi")

mediana(a,b,c)
