#Determinar si un numero es o no es primo
def primo(n,x,c):
    n = int(input("Ingrese un numero: "))
    x = 1
    c = 0
    while x <= n:
        if n % x == 0:
            c = c + 1
    x = x + 1
    if c == 2:
        print("El numero ",n," es primo")
    else:
        print("El numero ",n," no es primo")
primo(n,x,c)
