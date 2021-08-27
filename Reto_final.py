import math

def camas_a_mover(camas_actual, ocupacion_actual, ocupacion_esperada = 70) :
    """la funcion toma un valor y busca modificar ese valor para que se el porcentaje dado """
    camas_ocupadas = (camas_actual * ocupacion_actual) / 100
    camas_ocupadas = math.ceil(camas_ocupadas)
    
    camas_total_ocupacion_esperada = (camas_ocupadas * 100) / ocupacion_esperada
    camas_total_ocupacion_esperada = math.ceil(camas_total_ocupacion_esperada)
    camas_a_mover = camas_total_ocupacion_esperada - camas_actual

    return f"las camas de mas que se necesitan son: {camas_a_mover}"

print(camas_a_mover(257, 80.25, 68.5))
print(camas_a_mover(350, 100, 1 ))
print(camas_a_mover(100, 90 ))