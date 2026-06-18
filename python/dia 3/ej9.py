def crearmail(nombre, apellido):
    nombre1=(nombre)
    apellido1=(apellido)
    return (apellido1, nombre1)
nombre1=input("ingresa el nombre para tu mail")
apellido1=input("ingresa el apellido para tu mail")
print(f"tu mail es {crearmail}@gmail.com")
print(crearmail(apellido1, nombre1))