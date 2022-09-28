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


def max(x,y,z):
    l=[x,y,z]
    max=0
    for numar in l:
        if numar>max:
            max = numar
    return max

def min(x,y,z):
    l=[x,y,z]
    min=a
    for numar in l:
        if numar<min:
            min = numar
    return min
print ("Сel mai mic nr este :", min(a,b,c) , ",iar cel mai mare nr este :" , max(a,b,c))


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

def mult_com_cm_mici_primii_3(x,y,z):
    c_m_m_m=[]
    if x>y:
        multiplu=x
    elif y>x:
        multiplu=y
    else:
        multiplu=x
    while len(c_m_m_m)<3:
        if ((multiplu%x==0)and(multiplu%y==0)):
            c_m_m_m.append(multiplu)
            multiplu +=1
        else:
            multiplu +=1
    return (c_m_m_m)
print("Primii 3 multipli comuni al numerelor  sunt: ",mult_com_cm_mici_primii_3(a,b,c))


def lat_triunghi(x,y,z):
    #import math#
    if (x+y>z) and (x+z>y) and (y+z>x):
        sp=(x+y+z)/2
        aria=round(math.sqrt(sp*(sp-x)*(sp-y)*(sp-z)),2)
        perimetru=sp*2
        return print("Laturile pot forma un triunghi, astfel aria acestuia va fi: ",aria,", iar perimetrul: ",perimetru)
    else:
        return (lat_triunghi)
print("Laturile date nu pot forma un triunghi!", lat_triunghi(a,b,c))


def ecuatie(x,y,z):
    if x!=0:
        d=(y**2)-(4*x*z)
        if d>0:
            sol1=(-y-(d**0.5))/(2*x)
            sol2=(-y+(d**0.5))/(2*x)
        elif d==0:
            sol1=sol2=(-y)/(2*x)
        else:
            sol1=sol2='Ecuatia data nu are solutii'
    else:
        sol1=sol2='Ecuatia data nu are solutii'

    return sol1,sol2
print(" Ecuatia',a,'x2 +',b,'x +',c,'are solutiile reale ",ecuatie(a,b,c))
