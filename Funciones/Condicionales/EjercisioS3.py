#Un obrero necesita calcular su salario semanal
a = float(input("ingrese horas trabajadas: "))
def obrero(b):
    c = b - 40
    d = (40 * 2600) + (c * 5000)
    e = b * 2600
    if b > 40:
        return("su salario es: ", d)
    elif b < 40:
        return("su salario es: ", e)
print(obrero(a))