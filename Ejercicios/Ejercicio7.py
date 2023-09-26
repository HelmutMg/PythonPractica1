while True:
    print("Selecciona una opción de operación:")
    print("1. Mostrar la suma de los dos números")
    print("2. Mostrar la resta de los dos números")
    print("3. Mostrar la multiplicación de los dos números")
    print("4. Exit")
    
    opcion = input("Elije una opción (1-2-3-4): ")
    
    if opcion in ('1', '2', '3', '4'):
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        if opcion == '1':
            resultado = num1 + num2
            print("La suma de", num1, "y", num2, "es:", resultado)
        elif opcion == '2':
            resultado = num1 - num2
            print("La resta de", num1, "y", num2, "es:", resultado)
        elif opcion == '3':
            resultado = num1 * num2
            print("La multiplicación de", num1, "y", num2, "es:", resultado)
        elif opcion == '4':
            print("¡Gracias, hasta pronto!")
            break  
    else:
        print("Seleccione una opcción válida porfavor:(1-2-3-4).")