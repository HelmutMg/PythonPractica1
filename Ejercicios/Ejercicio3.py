
num_payasos = int(input("Ingrese el número de muñecos payasos vendidos: "))
num_muñecas = int(input("Ingrese el número de muñecas vendidas: "))

gramos_pasayo = 112
gramos_muñeca = 75

peso_total = (num_payasos * gramos_pasayo) + (num_muñecas * gramos_muñeca)


print("El peso total del paquete que será enviado es:", peso_total, "gramos")
