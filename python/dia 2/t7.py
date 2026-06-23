sumatot=0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    sumatot += num
print("La suma total es:", sumatot)