letrasvalidas = ["Q","W","R","T","Y","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
numerosvalidos = ["2","4","6","8"]
nonumeros = 0
letraactual = 0
tickets = [""]
i = 0
def aniadirticket():
  global letraactual
  global nonumeros
  global i
  i += 1
  if nonumeros > 4:
    letraactual += 1
  else:
    tickets[i-1] = numerosvalidos[nonumeros]+letrasvalidas[letraactual]
    return tickets
aniadirticket()
print(tickets)
