a=int(input('Introduceti primul nr: '))
b=int(input('Introduceti al doilea nr: '))
def suma(x,y):
    i=(x+y)
    return (i)
print("Suma acestor numere este :",suma(a,b))

def produs_nr(x,y):
    i=(x*y)
    return (i)
print("Produsul acestor numere este :",produs_nr(a,b))

def media_aritm(x,y):
    i=(x+y)/2
    return (i)
print("Media aritmetica a acestor numere este :",media_aritm(a,b))

def cel_mm_div_com(x,y):
    m=[]
    n=[]
    for i in range (1,x+1):
        if (x%i==0):
            m.append(i)
    for j in range (1,y+1):
        if (y%j==0):
            n.append(j)
    c=set(m).intersection(n)
    l=max(c)
    return (l)
print( "Cel mai mare divizor comun al numerelor este: ",cel_mm_div_com(a,b))


def cel_mmic_mult_com(x,y):
    if x>y:
        multiplu=x
    elif b>a:
        multiplu=y
    else:
        multiplu=x
    while True:
        if ((multiplu%x==0)and(multiplu%x==0)):
            cel_mmic=multiplu
            break
        multiplu +=1
    return (multiplu)
print(" Cel mai mic multiplu comun al numerelor este: ",cel_mmic_mult_com(a,b))

def minim(x,y):
    return min([x,y])
print ("Numarul minim este:",minim(a,b))
def maxim(x,y):
    return max([x,y])
print ("Numarul minim este:",maxim(a,b))


   
def suma_n(x,y):
    a= int(input('Dati primul numar: '))
    b= int(input('Dati al doilea numar: '))
    c=a+b
    return (c)
print("Suma nr :", suma_n(a,b))


def produs_n(x,y):
    a= int(input('Dati primul numar: '))
    b= int(input('Dati al doilea numar: '))
    c=a*b
    return (c)
print("Produs nr :", produs_n(a,b))


def divizorii_comuni(x,y):
    m=[]
    n=[]
    for i in range (1,x+1):
        if (x%i==0):
            m.append(i)
    for j in range (1,y+1):
        if (y%j==0):
            n.append(j)
    c=set(m).intersection(n)
    br=list(c)
    return (br)
print("Toti divizorii comuni ai numerelor sunt :" , divizorii_comuni(a,b))


def cinci_multipli_comuni(x,y):
    c_m_m_m=[]
    if x>y:
        multiplu=x
    elif y>x:
        multiplu=y
    else:
        multiplu=x
    while len(c_m_m_m)<5:
        if ((multiplu%x==0)and(multiplu%y==0)):
            c_m_m_m.append(multiplu)
            multiplu +=1
        else:
            multiplu +=1
    return (c_m_m_m)
print("Cinci multipli comuni al numerelor sunt: ", cinci_multipli_comuni(a,b))


def comun(x,y):
    return list (set(str(x)).intersection(set(str(y))))
print("Cifrele care se contin in ambele numere :",comun(a,b))


def cifre_specifice(x,y):
    return list(set(str(a)).difference(set(str(b))))
print("Cifrele specifice primul numar si care nu sunt in al doilea:", cifre_specifice(a,b))



def prietenie(x,y):
    if len([i for i in range(1,x+1) if x%i==0])==len([i for i in range(1,y+1) if y%i==0]):
        return 'PRIETENIE'
print("Sunt prietene:",prietenie(a,b))