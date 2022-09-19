#1
def suma_nr(a,b):
    c=a+b
    return 
    print("Suma numerelor este: ",c)

#2
def produsul_nr(a,b):
    d=a*b
    return 
    print(" Produsul numerelor este: ",d)

#3
def media_aritm(a,b):
    e=(a+b)/2
    return
    print("Media aritmetica acestor numere este: ",e)

#4
def cel_mm_div_com(a,b):
    ad=[]
    bd=[]
    for i in range (1,a+1):
        if (a%i==0):
            ad.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            bd.append(j)
    c=set(ad).intersection(bd)
    l=max(c)
    return 
    print( "Cel mai mare divizor comun al numerelor este: ",l)

#5
def cel_mmic_mult_com(a,b):
    if a>b:
        multiplu=a
    elif b>a:
        multiplu=b
    else:
        multiplu=a
    while True:
        if ((multiplu%a==0)and(multiplu%b==0)):
            cel_mmic=multiplu
            break
        multiplu +=1
    return 
    print(" Cel mai mic multiplu comun al numerelor este: ",cel_mmic)

#6
def minim(a,b):
    if a<b:
        return print(" Numarul minim este: ",a)
    else:
        return print(" Numarul minim este: ",b)

#7
def maxim(a,b):
    if a>b:
        return print(" Numarul maxim este: ",a)
    else:
        return print(" Numarul maxim este: ",b)

#8
def suma_n():
    a= int(input('Dati primul numar: '))
    b= int(input('Dati al doilea numar: '))
    c=a+b
    return print(a," + ",b," = ",c)

#9
def produs_nedef():
    a= int(input('Dati primul numar: '))
    b= int(input('Dati al doilea numar: '))
    c=a*b
    return print(a," * ",b," = ",c)
    