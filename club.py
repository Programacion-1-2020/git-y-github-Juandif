letrasvalidas = ["Q","W","R","T","Y","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
numerosvalidos = ["2","4","6","8"]
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
def validarticket():
  global validaletra
  global validonumero
  e = 0
  for e in range(21):
    if ticketres[1] == letrasvalidas[e]:
      validaletra = True
      e = 21
    elif validaletra == True:
        pass
    else:
      validaletra = False
  e = 0
  for e in range(4):
    if ticketres[0] == numerosvalidos[e]:
      validonumero = True
      e = 4
    elif validonumero == True:
        pass
    else:
      validonumero = False
  return validaletra,validonumero

def aniadirticket():
  global letraactual
  global nonumeros
  global i
  i += 1
  if nonumeros >= 4:
    letraactual += 1
    nonumeros = 0
  newticket = numerosvalidos[nonumeros]+letrasvalidas[letraactual]
  tickets.append(newticket)
  nonumeros += 1
  print(nonumeros)
  return tickets
def personaentrada():
  ticketres = input("Ingrese el ticket de la persona\n>")
  validarticket()
  if (validaletra == True) and (validonumero == True):
    ticketsenuso.append(ticketres)
  elif ticketres in ticketsenuso:
    print("Este ticket ya esta en uso.")
  else:
    print("Ticket invalido, intente de vuelta.")
    return ticketsenuso
def echarpersona():
  ticketechar = input("Ingrese el ticket de la persona que quieres echar\n>")
  e = 0
  for e in range(len(ticketsenuso)):
    if ticketechar == ticketsenuso[e]:
      del (ticketsenuso[e])
      print("Se ha echado esa persona.")
      e = len(ticketsenuso)
    elif e <= len(ticketsenuso):
      e += 1
  e += 1
  if e > len(ticketsenuso)+1:
      print("Ticket no se encontro en uso.")
finfin = False
#aqui empieza -----
ticketres = input("Ingrese su ticket\n>")
validarticket()
ticketsenuso.append(ticketres)
print(validonumero,validaletra)
if validonumero == True and validaletra == True:
    while finfin != True:
      if tiempo < tiempoacerrar:
        pass
      else:
        print("Es tiempo de cerrar el club.")
        fin = True
        finfin = True
      if fin != True:
        opcion = input("Quiere aniadir tickets, dejar entrar personas, echar personas, mostrar cuantas personas hay, mostrar el tiempo, o ya terminar el dia?\n>")
        if opcion == "echar":
          echarpersona()
          tiempo += 30
        if opcion == "entrar":
          if len(ticketsenuso) >= 20:
            print("No pueden entrar mas personas")
          else:
            personaentrada()
          tiempo += 30
        while opcion == "aniadir":
          aniadirticket()
          print(tickets)
          opcion = input("Quiere aniadir mas tickets?\n>")
          tiempo += 30
        if opcion == "mostrar personas":
            print("Los tickets de las personas presentes son:\n",ticketsenuso)
            tiempo += 30
        if opcion == "mostrar tiempo":
            print("El tiempo es",tiempo)
            tiempo += 30
        if opcion == "terminar":
            print("Decidis cerrar el club temprano...")
            tiempo = 2600
else:
    print("Ticket invalido, intente de vuelta.")
