pathologies = {
    "Respiratory system": [
        {
            "id": 1,
            "name": "Cystic Fibrosis",
            "price": 300 	
        },
        {
            "id": 2,
            "name": "Emphysema",
            "price": 500
        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],
    "Nervous system": [
        {
            "id": 4,
            "name": "Parkinson",
            "price": 800 	
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],
    "Endocrine system": [
        {
            "id": 6,
            "name": "Diabetes",
            "price": 350 	
        },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700
        },
        {
            "id": 8,
            "name": "Hashimoto’s thyroiditis",
            "price": 900
        }
    ],   
}


datos_pacientes=[]

while True:

 print("""Bienvenido/a a la clínica, selecciona el número de la opción a la que desees acceder: 

 1-Registros y pagos.
 2-Ver pacientes.
 3-Salir.



 """)

 seleccion=input("Ingrese el número:")

 while seleccion !="1" and seleccion!="2" and seleccion!="3":
       print("Ingreso inválido, por favor selecciona un número del 1 al 3")
       seleccion=input("Ingrese el número:")
      
         
     

 if seleccion==("1"):      
     name=input("Ingrese su nombre:")
     apellido=input("Ingrese su apellido:")
     ci=input("Ingrese su cédula de identidad:")

     print(f"{pathologies}");id=input("Ingrese el id de la patología que padece:")

     datos_pacientes.append(name),datos_pacientes.append(apellido), datos_pacientes.append(ci), datos_pacientes.append(id)

     print(F"""FACTURA
     
     
     ------------------------

     Nombre:{name}
     Apellido:{apellido}
     Cédula de identidad:{ci}

     Patología que padece: {pathologies}

     MONTO A PAGAR:

     
     
     
     
     """) 




 








 

 if seleccion==("2"):
     print("Sobre qué patología desea consultar? ")
     pato=input("Ingrese la inicial de la patología:")
    


 if seleccion==("3"):
     break


 else:
        break

print("Soy de eléctrica, por favor compasión")