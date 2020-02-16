"""PROGRAMA PARA DESCOBRIR PRIMOS"""
import math
import matplotlib.pyplot as plt

def cousin(a):  
    if a%2==0:
        return(0)
    b=math.floor(a/2)
    for d in range(3,b,1):
        if a%d==0:
            return(0)
    return(1)

def nprimos(k):
    nvar=0
    for j in range(2,k,1):
        p=cousin(j)
        if p==1:
            nvar+=1
    return(nvar)

lista=[]
for n in range(0,101,1):
    lista.append(n)
lista2=[]
for elemento in lista:
    lista2.append(nprimos(elemento))
plt.plot(lista, lista2)
plt.show()