 #Calcular la suma de todos los enteros desde 1 hasta N
try:
    N = int(input("Ingrese un entero positivo: "))
    if N <= 0:
        print("Por favor, ingrese un entero positivo.")
    else:
        suma = 0

        
        for i in range(1, N + 1):
            suma += i

        # Resultado
        print("La suma de todos los enteros desde 1 hasta", N, "es:", suma)
except ValueError:
    print("Debe ingresar un entero positivo válido.")
