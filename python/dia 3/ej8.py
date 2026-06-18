def calcularpreciofinal(precio, descuento):
    pdesc=precio/descuento
    return pdesc
PRESIO=int(input("ingresa el precio del articulo:"))
DESCUENT=int(input("Ingresa el descuento del articulo:"))
print(calcularpreciofinal(PRESIO,DESCUENT))-