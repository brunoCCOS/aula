"""a="bruno"
b="leozinho"
c="fabinho"
print(f'{a} {b} {c}')
d=("leozinho", "bruno","fabinho")
d=tuple("54")
print(d)
e=["leozinho", "bruno","fabinho"]
print(e)
e.append("leozao")
print(e)
e.pop(1)
print(e)
print(len(e))
e=['a','b','c']
print(e)
e=list("24")
print(e)
f=[5,4,2,1,0]
print(f)
f.insert(2,3)
print(f)
f[2]="pausa técninca"
print(f)
f[0]=2.3
print(f)
g=(1,2,3,4,5)
print(g)
f.insert(6,"um")
print(f)"""
A=int(input("Insira um número:"))
B=int(input("Insira outro número:"))
if B>A:
    caixa=B
    B=A
    A=caixa
C=int(input("Insira seu ultimo número:"))
if C>A:
    caixa=C
    C=A
    A=caixa
print(A,B,C)
if A>=B+C:
    print("NAO E TRIANGULO")
if A**2==B**2+C**2:
    print("TRIANGULO RETANGULO")
if A**2>B**2+C**2:
    print("TRIANGULO OBTUSANGULO")
if A**2<B**2+C**2:
    print("TRIANGULO ACUTANGULO")
if A == B and B == C:
    print("TRIANGULO EQUI")
if (A == B and B != C) or (B == C and B != A) or (C == A and C != B):
    print("TRIANGULO ISOSCELES")            




