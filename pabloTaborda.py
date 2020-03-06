# for i in range(0,5):# seria como poner for (int i=0; i>5;i++)
#    print(i)
       
# count = 0
# while count<5:
#        print(count)
#        count+=1


#    Una empresa necesita un software que le permita calcular el promedio de edad, peso de un
# número desconocido de personas.
# Deberá determinar cuántas personas son mayores de 30 años, pero menores a 40 años,
# cuántas hay entre 40 y 60 años, cuantas son mayores a 60 años y debe mostrar la cantidad
# de personas encuestadas.
# Si lleva un múltiplo de 5 en cantidad de personas encuestadas, se imprime un mensaje
# donde se muestre que ya se lleva X cantidad de personas y pregunta si desea continuar, de
# ser falso, finaliza el programa y arroja los resultados obtenidos hasta el momento. Si es
# verdadero continúa realizando encuestas.
# Los datos se imprimen solo hasta que el usuario decida terminar de realizar encuestas y se
# debe imprimir promedio de edad, promedio de peso y cantidad de personas encuestadas. 

edad =0
peso = 0
cedad=0
cpeso=0
cpers = 0
aedad=0
apeso=0
apers = 0
promEdad = 0
promPeso = 0
r = True
pregunta=""

while r:
   for i in range(0,5):
      edad= int(input("Digite Edad: "))
      peso= int(input("Digite Peso: "))
      cedad+=1
      cpeso+=1 
      cpers+=1
      aedad = aedad + edad
      apeso= apeso + peso
   print("Personas Encuestadas: "+str(cpers))
   pregunta = input("presione s para continuar o n para salir: ")
   if pregunta=="s":
      r=True
   else:
         r= False
         promEdad=aedad/cedad
         promPeso=apeso/cpeso
         print("Promedio de Edad: "+ " "+str(promEdad)+" "+"Promedio de Peso: "+str(promPeso)+" "+"Personas Encuestadas: "+str(cpers))




