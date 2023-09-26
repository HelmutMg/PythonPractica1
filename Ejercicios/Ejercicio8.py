hora = input("Ingresar la hora en formato HH:MM: ")

try:
    horas, minutos = map(float, hora.split(":"))
except ValueError:
    print("Formato incorrecto. Debe ser HH:MM.")
    exit()

rang_desayuno = range(7, 9) 
rang_almuerzo = range(12, 14)  
rang_cena = range(18, 20)  

if horas in rang_desayuno:
    print("Ya es hora de desayunar.")
elif horas in rang_almuerzo:
    print("Ya es hora de almorzar.")
elif horas in rang_cena:
    print("Ya es hora de cenar.")
else:
    print("No es hora de comer.")