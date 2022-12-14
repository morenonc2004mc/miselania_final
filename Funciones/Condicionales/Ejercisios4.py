
def telefono(a):
    c = (a * 50) + 200
    if a < 3:
        return("su llamada cuesta 200 pesos")
    elif a > 4:
        return("su llamada cuesta: ", c)
a = float(input("ingrese los minutos de la llamada: "))
print(telefono(a))