'''
Date trei numere, să se calculeze toate sumele posibile de câte două numere. Afişarea
să cuprindă şi termenii sumei, nu numai valoarea ei. Exemplu: Date de intrare : 2 13
4 Date de ieşire: 2+13 =15 2+4=6 13+4=17. 
'''
a=int(input("Intruduceti primul numar:"))
b=int(input("Intruduceti al doilea numar:"))
c=int(input("Intruduceti al treilea numar:"))
suma1=a+b
suma2=b+c
suma3=a+c
print("Sumele urmatoarelor numere sunt:",a,'+',b,"=",suma1,',',b,'+',c,"=",suma2,'si',a,'+',c,"=",suma3,'.')