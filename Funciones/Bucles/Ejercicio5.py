"""Calcular la operación x** n sin utilizar la función pow"""
def potencia(x,n):
    c=n+1
    potencia=0
    for i in range (1,c):
        potencia= x**n
    print("La resultado de la potencia",x,"^",n,"es: ", potencia)
x=int(input ("Digita el número que quieres elevar: "))
n=int(input("Digita la potencia a la que quieres elevar el número: "))
potencia(x,n)