import random 
n1=random.randint(1,999)
n2=random.randint(1,999)
bz=random.randint(2,9)

print("Primul nr:",n1)
print("Al doilea nr:",n2)
print("Baza numerelor:",bz)

def cifra_maxima(n):
    max=0
    while n>0:
        r=n%10
        n//=10
        if r>max:
            max=r
    return max

def verificare_baza(n,b):
    elem=cifra_maxima(n)
    if elem<(b):
        return True
    else:
        return False
    
def baze_necunoscute_in_baza_10(n,b):
        i=0
        s=0
        while n>0:
            r=n%10
            k=r*(b**i)
            n//=10
            s=s+k
            i=i+1
        return s

def suma_2_baze_10(a,v,b):
    k=baze_necunoscute_in_baza_10(a,b)
    l=baze_necunoscute_in_baza_10(v,b)
    c=k+l
    return c

def convertirea_din_baza_10_in_alta_adunarea(a,v,b):
    sum=suma_2_baze_10(a,v,b)
    list=[]
    while sum>0:
        nr=sum//b
        k=sum-(b*nr)
        list.append(k)
        sum=nr
    xx=reversed(list)
    final=''.join(map(str,xx))
    return print("Suma numerelor",n1,"si",n2,"in baza",bz,"este:",final,'.')

def diferenta_2_baze_10(a,v,b):
    k=baze_necunoscute_in_baza_10(a,b)
    l=baze_necunoscute_in_baza_10(v,b)
    if k>l:
        c=k-l
        return c
    elif l>k:
        c=l-k
        return c

def convertirea_din_baza_10_in_alta_scaderea(a,v,b):
    dif=diferenta_2_baze_10(a,v,b)
    list=[]
    while dif>0:
        nr=dif//b
        k=dif-(b*nr)
        list.append(k)
        dif=nr
    xx=reversed(list)
    final=''.join(map(str,xx))
    return print("Diferenta numerelor",n1,"si",n2,"in baza",bz,"este:",final,'.')

def inmultirea_2_baze_10(a,v,b):
    k=baze_necunoscute_in_baza_10(a,b)
    l=baze_necunoscute_in_baza_10(v,b)
    c=k*l
    return c

def convertirea_din_baza_10_in_alta_inmultirea(a,v,b):
    inm=inmultirea_2_baze_10(a,v,b)
    list=[]
    while inm>0:
        nr=inm//b
        k=inm-(b*nr)
        list.append(k)
        inm=nr
    xx=reversed(list)
    final=''.join(map(str,xx))
    return print("Inmultirea numerelor",n1,"si",n2,"in baza",bz,"este:",final,'.')



if (bz>1) and (bz<10):
    print("In sistemul de numeratie a bazei ", bz,"primul numar este scris :",verificare_baza(n1,bz))
    print("In sistemul de numeratie a bazei",bz,"al doilea numar este scris",verificare_baza(n2,bz))
    if verificare_baza(n1,bz) and verificare_baza(n2,bz) :
        convertirea_din_baza_10_in_alta_adunarea(n1,n2,bz)
        convertirea_din_baza_10_in_alta_scaderea(n1,n2,bz)
        convertirea_din_baza_10_in_alta_inmultirea(n1,n2,bz)