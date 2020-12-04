
print("______________________________________") 
ntrabajadores = int (input(" INGRESA EL NUMERO DE TRABAJADORES: "))
print("______________________________________")  
print()     

retencion = [10,13,16,23,30] 

i = 1  
while i <= ntrabajadores:  
 print("______________________________________")  
 salario = int(input("Salario diario del trabajador {}: ".format(i)) ) 
 print("______________________________________")  
 nomina = int(salario)  
 print() 


 if nomina <= 5000:  
     descuento = (nomina * retencion[0])/100  
     nom = nomina - descuento 
     print("____________________________________________") 
     print("    Al empleado {} se le desconto el 10%".format(i)) 
     print("    Su nomina del mes es de $ {}".format(nom)) 
     print("____________________________________________") 
     print() 
 if nomina >= 5001 and nomina <= 10000:
     descuento = (nomina * retencion[1]) / 100 
     nom = nomina - descuento
     print("____________________________________________") 
     print("   Al empleado {} se le desconto el 13%".format(i))
     print("   Su nomina del mes es de $ {}".format(nom))
     print("____________________________________________") 
     print()
 if nomina >= 10001 and nomina <= 14500:
     descuento = (nomina * retencion[2]) / 100 
     nom = nomina - descuento 
     print("____________________________________________") 
     print("   Al empleado {} se le desconto el 16%".format(i)) 
     print("   Su nomina del mes es de $ {}".format(nom)) 
     print("____________________________________________")  
     print()  
 if nomina >= 14501 and nomina <= 21700: 
     descuento = (nomina * retencion[3]) / 100
     nom = nomina - descuento 
     print("_____________________________________________") 
     print("   Al empleado {} se le desconto el 23%".format(i)) 
     print("   Su nomina del mes es de $ {}".format(nom)) 
     print("_____________________________________________") 
     print()  
 if nomina > 21701: 
     descuento = (nomina * retencion[4]) / 100 
     nom = nomina - descuento 
     print("_____________________________________________") 
     print("   Al empleado {} se le desconto el 30%".format(i)) 
     print("   Su nomina del mes es de $ {}".format(nom)) 
     print("_____________________________________________") 
     print() 

 i +=1 
print("Asi quedaron los calculos ") 
