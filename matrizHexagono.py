import math

def conversion_rot(n=1,k=1):
    pi = math.pi
    valor = ((2*pi*k)/n)
    r1 = math.cos(valor)
    r2 = -math.sin(valor)
    r3 = math.sin(valor)
    r4 = math.cos(valor)

    print("[" , r1 , "|" , r2 , "]" )
    print("[" , r3 , "|" , r4 , "]" )
    print("__________________________________________")

def conversion_ref(n=1,k=1):
    pi = math.pi
    valor = ((2*pi*k)/n)
    r1 = math.cos(valor)
    r2 = math.sin(valor)
    r3 = math.sin(valor)
    r4 = -math.cos(valor)

    print("[" , r1 , "|" , r2 , "]" )
    print("[" , r3 , "|" , r4 , "]" )
    print("__________________________________________")


n = int(input("ingrese cantidad de lados:"))
k = 0

while k < n:
    conversion_ref(n , k)
    k = k + 1
