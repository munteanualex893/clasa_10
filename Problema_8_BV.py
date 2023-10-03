a=int(input("Care este prima cifra:"))
b=int(input("Care este a doua cifra:"))
c=int(input("Care este a treia cifra:"))
n1=100*a+10*b+c
n2=100*b+10*a+c
n3=100*a+10*c+b
n4=100*c+10*b+a
n5=100*c+10*a+b
print('Din aceste 3 cifre sau format urmatoatele numere:',n1,',',n2,',',n3,',',n4,'si',n5,'.')