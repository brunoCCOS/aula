'''string'''
a="leozao"
print(a[1]) #strings,tuplas e listas sao estruturas de 
            #dados parecidos por isso os mesmos recursos funcionam
"""listas"""
c=["alemao","jesus","judeu"]
b=list(c)     #passa por valor
b[2]="acertou"
print(b[1:3]) #Fatiamento do elemento de indice 1 ate o elemento de indice 3(o 4 é excluido)
b=c           #Cria um laço entre as duas listas (qulquer mudança em c muda em b) passa por referencia
b=c[:]        #Faz uma copia por valor
print(c[1][3])#Faz print do elemento do indice X do elemento Y da lista
print(c[:])

matriz=[[1 , 2 , 3],[3 , [3,4,5], 4]] #listas com mais de mais de uma dimensão
print(matriz)
matriz3x3=[[1,2,3],[4,5,6],[7,8,9]]
'''função'''
def alcance(a,b,c=1):
    lista=list()
    while a<b:
        lista.append(a)
        a=a+c
    return(lista)#return é uma função que retorna pro programa aquilo que é passado como arg
def Leozao(a=0):#o '=' define um valor padrão para aquela variavel caso não seja passada como arg
    lista=list()
    for i in alcance(0,a):
        lista.append(a)
    return(lista)
def soma(*arg):#* usado para usar um numero indefinido de arg(cria uma tupla com todos os arg)
    aux=0
    for i in arg:#i assume,um de cada vez, os valores da list apos o in
        aux=aux+i
    return(aux)
print(soma(3,4,5))

print(Leozao(7))


