#Solicite al usuario una cantidad numérica que expresa segundos (medida detiempo). Exprésela (conviértala) en horas minutos y segundos. Según el caso
def tiempo(t):
    m = t / 60
    h = m / 60
    return("horas: ", h), ("minutos: ", m), ("segundos: ", t)

t = int(input("ingrese el valor en segundos: "))
print(tiempo(t))

