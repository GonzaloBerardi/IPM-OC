
saldo = 1000
pin_correcto = "1234" 

def verificar_pin(pin_usuario):
    return pin_usuario == pin_correcto

def retirar(monto):
    global saldo
    
    if monto <= 0:
        print("Error: El monto a retirar debe ser mayor a 0.")
    elif monto > saldo:
        print("Error: Fondos insuficientes. Su saldo actual es:", saldo)
    else:
        saldo -= monto
        print("Retiro exitoso. Su nuevo saldo es:", saldo)

print("🏦 Bienvenido al Banco Python")

input_pin = input("Ingrese su PIN: ")

if verificar_pin(input_pin):
    print("Acceso concedido. Saldo actual:", saldo)
    
    try:
        monto_str = input("¿Cuánto desea retirar? ")
        monto = int(monto_str)
        retirar(monto)
        
    except ValueError:
        print("Error: Ingrese un número válido.")
else:
    print("PIN Incorrecto. Policía en camino.")
