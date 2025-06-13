while True:
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Ingrese una opcion: "))
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    
    if opcion == 1:
        resultado = num1 + num2
        print(resultado)
    elif opcion == 5:
        break
