
def gonza(n1, n2, n3):

    if n1>n2 and n1>n3:
     return n1
    if n2>n1 and n2>n3:
     return n2
    if n3>n1 and n3>n2:
      return n3

num1=int(input("Ingrese su primer numero"))
num2=int(input("Ingrese su segundo numero"))
num3=int(input("Ingrese su tercer numero"))
print(gonza(num1, num2, num3))