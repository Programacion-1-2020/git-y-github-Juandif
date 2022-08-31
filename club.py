LETRAS_VALIDAS = ["Q", "W", "R", "T", "Y", "P", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
NUMEROS_VALIDOS = ["2", "4", "6", "8"]
nonumeros = 0
letraactual = 0
tickets = []
opcion = ""
fin = False
i = 0
tiempo = 1400
tiempoacerrar = 2600
ticketsenuso = []
validaletra = False
validonumero = False
# no entiendo porque no me deja importar desde funciones.py
import validarticket from funciones



finfin = False
# aqui empieza -----
ticketres = input("Ingrese su ticket\n>")
validarticket(ticketres)
ticketsenuso.append(ticketres)
print(validonumero, validaletra)
if validonumero == True and validaletra == True:
    while finfin != True:
        if tiempo < tiempoacerrar:
            pass
        else:
            print("Es tiempo de cerrar el club.")
            fin = True
            finfin = True
        if fin != True:
            opcion = input("Opciones:\n"
                           "1. Entrar personas\n"
                           "2. Echar personas\n"
                           "3. Mostrar personas\n"
                           "4. Mostrar tiempo\n"
                           "5. Terminar el dia")
            if opcion == "2":
                echarpersona()
                tiempo += 30
            if opcion == "1":
                if len(ticketsenuso) >= 20:
                    print("No pueden entrar mas personas")
                else:
                    personaentrada()
                tiempo += 30
            if opcion == "3":
                print("Los tickets de las personas presentes son:\n", ticketsenuso)
                tiempo += 30
            if opcion == "4":
                print("El tiempo es", tiempo)
                tiempo += 30
            if opcion == "5":
                print("Decidis cerrar el club temprano...")
                tiempo = 2600
else:
    print("Ticket invalido, intente de vuelta.")
