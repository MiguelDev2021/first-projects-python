
#declara la variables de la fiesta
numero_invitados = 56
numero_cajas_refrescos = 9 #numero de cajas
resfrescos_caja = 24       #numero de refrescos por caja
refrescos_tomados_persona = 0
refrescos_sobrantes = 0
#calculamos la cantidad total de frescos en la fiesta.
cantidad_total_refrescos =  numero_cajas_refrescos * resfrescos_caja
print("Hay un total de ", cantidad_total_refrescos, "refrescos\n" )

#calculamos cuantos refrescos se toma cada persona
refrescos_tomados_persona = cantidad_total_refrescos // numero_invitados
print("cada inivitado puede tomar ", refrescos_tomados_persona, "refrescos\n")

#calculamos cuantos refrescos sobran
refrescos_sobrantes = cantidad_total_refrescos % numero_invitados
print("sobran ", refrescos_sobrantes, "refrescos\n")


