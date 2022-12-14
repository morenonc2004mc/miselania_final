def positivonegativo(numero):
    if numero == 0:
        return("cero")
    elif numero < 0:
        return("negativo")
    else:
        return("positivo")
numero_digitado = float(input("escribe un numero: "))
print(positivonegativo(numero_digitado))
