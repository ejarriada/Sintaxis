import TadMedicamento
from TadMedicamento import *

#Crea y carga el primer medicamento
m1=crearMed()
ng=input("Ingrese el Nombre Genérico del medicamento")
nc=input("Ingrese el Nombre Comercail del Medicamento")
lab=input("Ingrese el Laboratorio")
pre=float(input("Ingrese el precio del Medicamento")
cargarMed(m1, ng, nc, lab, pre)

#Crea y carga el segundo medicamento
m2=crearMed()
ng=input("Ingrese el Nombre Genérico del medicamento")
nc=input("Ingrese el Nombre Comercail del Medicamento")
lab=input("Ingrese el Laboratorio")
pre=float(input("Ingrese el precio del Medicamento")
cargarMed(m2, ng, nc, lab, pre)


if (verPrecio(m1)>verPrecio(m2)):
	print("El medicamento mas caro es: ")
	print verNomCom(m1)
	
elif (verPrecio(m1)<verPrecio(m2)):
	print("El medicamento mas caro es: ")
	print verNomCom(m2)
	
else:
	print ("Los medicamentos tienen el mismo precio")
