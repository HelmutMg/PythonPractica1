edad = int(input("Ingrese su edad: "))

if edad < 4:
    costo = 0 
elif edad <= 18:
    costo = 5  
else:
    costo = 10  

print(f"El costo de la entrada es: ${costo}")
