a=int(input('Introduceti primul nr: '))
b=int(input('Introduceti al doilea nr: '))
c=int(input('Introduceti al treilea nr :'))
def cel_mm_div_com(x,y,z):
    m=[]
    n=[]
    q=[]
    for i in range (1,x+1):
        if (x%i==0):
            m.append(i)
    for j in range (1,y+1):
        if (y%j==0):
            n.append(j)
    for k in range (1,z+1):
        if (y%k==0):
            q.append(k)        
    h=set(m).intersection(n)
    d=set(h).intersection(q)
    l=max(d)
    return (l)
print( "Cel mai mare divizor comun al numerelor este: ",cel_mm_div_com(a,b,c))


def cel_mmic_mult_com(x,y,z):
    if x>y and x>z:
        multiplu=x
    elif b>a and b>c:
        multiplu=y
    elif z>x and z>y:
        multiplu=z
    
    while True:
        if ((multiplu%x==0)and(multiplu%y==0)and (multiplu%z==0)):
            cel_mmic=multiplu
            break
        multiplu +=1
    return (multiplu)
print(" Cel mai mic multiplu comun al numerelor este: ",cel_mmic_mult_com(a,b,c))


def minim(x,y,z):
    return min([x,y,z])
print ("Numarul minim este:",minim(a,b,c))


def maxim(x,y,z):
    return max([x,y,z])
print ("Numarul minim este:",maxim(a,b,c))

def divizorii_comuni(x,y,z):
    m=[]
    n=[]
    q=[]
    for i in range (1,x+1):
        if (x%i==0):
            m.append(i)
    for j in range (1,y+1):
        if (y%j==0):
            n.append(j)
    for k in range (1,z+1):
        if (z%k==0):
            q.append(i)
    h=set(m).intersection(n)
    l=set(h).intersection(q)
    br=list(l)
    return (br)
print("Toti divizorii comuni ai numerelor sunt :" , divizorii_comuni(a,b,c))
