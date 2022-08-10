letrasvalidas = ["Q","W","R","T","Y","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
numerosvalidos = ["2","4","6","8"]
nonumeros = 0
letraactual = 0
tickets = []
i = 0
validaletra = True
validonumero = True
def validarticket():
  global validaletra
  global validonumero
  e = 0
  for e in range(21):
    if ticketres[1] == letrasvalidas[e]:
      validaletra = True
    else:
      validaletra = False
    e += 1
  e = 0
  for e in range(4):
    if ticketres[0] == numerosvalidos[e]:
      validonumero = True
    else:
      validonumero = False
    e += 1
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
ticketres = input("Ingrese su ticket\n>")
validarticket()
print(validonumero,validaletra)
opcion = input("Quiere aniadir tickets")
while opcion == "s":
  aniadirticket()
  print(tickets)
  opcion = input("Quiere aniadir tickets")
