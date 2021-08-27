#calculadora de vueltas por minuto.

MINUTO = 60
tiempo_girado = 640 #tener en cuenta que el tiempo girado es dado en segundos
cantidad_vueltas_minuto = 147

tiempo_girado_minutos =  640 / 60 #calculamos cuantos minutos giro el spiner
print("el spiner giro durante ", tiempo_girado_minutos, "minutos\n"  )

cantidad_vueltas_totales =  tiempo_girado_minutos * cantidad_vueltas_minuto #calculamos la vueltas totales que hace el spiner
print("el spiner dio " ,cantidad_vueltas_totales, "vueltas\n")