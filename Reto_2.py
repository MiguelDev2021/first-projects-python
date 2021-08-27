#calcular el valor del movil sin iva, la telofonia aparece con iva del 21 %
IVA = 21 #se define como constante ya que no varia.
porcentaje_aumento_postventa = 20 / 100 # el aumento despues de la preventa
valor_postventa = 0
iva_porcentaje = 21 / 100 

valor_preventa = 420
print("el valor del movil en preventa es ", valor_preventa, "\n")

valor_preventa = valor_preventa - (valor_preventa * iva_porcentaje) # valor original sin iva
print("el valor del movil en preventa es sin iva es", valor_preventa, "\n")

#ahora se calcula el valor de aumento sin iva al movil

valor_postventa = valor_preventa + (valor_preventa * porcentaje_aumento_postventa) 
print("el valor de postventa sin iva es: ", valor_postventa, "\n")

valor_postventa = valor_postventa + (valor_postventa * iva_porcentaje)
print("el valor total del movil en postventa es: ", valor_postventa, "\n")
