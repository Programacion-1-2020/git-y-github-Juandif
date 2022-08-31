LETRAS_VALIDAS = ["Q", "W", "R", "T", "Y", "P", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N",
                  "M"]
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
def validarticket(ticket):
    numero_valido = ticket[0] in NUMEROS_VALIDOS
    letra_valida = ticket[1] in LETRAS_VALIDAS
    return numero_valido, letra_valida

def personaentrada():
    ticketres = input("Ingrese el ticket de la persona\n>")
    validarticket(ticketres)
    if ticketres in ticketsenuso:
        print("Este ticket ya esta en uso.")
    elif (validaletra == True) and (validonumero == True):
        ticketsenuso.append(ticketres)
    else:
        print("Ticket invalido, intente de vuelta.")
    return ticketsenuso


def echarpersona():
    ticketechar = input("Ingrese el ticket de la persona que quieres echar\n>")
    e = 0
    # Este for sirve para saber que ticket eliminar de la lista de tickets en uso
    for e in range(len(ticketsenuso)):
        if ticketechar == ticketsenuso[e]:
            del (ticketsenuso[e])
            print("Se ha echado esa persona.")
            e = len(ticketsenuso)
        elif e <= len(ticketsenuso):
            e += 1
    e += 1
    if e > len(ticketsenuso) + 1:
        print("Ticket no se encontro en uso.")
