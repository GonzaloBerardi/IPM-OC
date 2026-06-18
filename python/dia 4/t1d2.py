lista_compras = []
for i in range(5):
    try:
        producto = input(f"Ingrese el producto {i + 1}: ")
        lista_compras.append(producto)
        print("Lista de compras:", lista_compras)
    except ValueError:
           print("Tienes que escribir letras no numeros")