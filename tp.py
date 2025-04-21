# defino tablero nxn y pido valores del juego
cantidadCasillas: int = int(input("Ingrese la cantidad de casillas: "))
cantidadDisparos: int = int(input("Ingrese la cantidad de disparos de esta partida: "))
cantidadBarcos: int = int(input("Ingrese la cantidad de barcos a colocar: "))

#poner valores maximos de cada variable

if (cantidadCasillas > 15 or cantidadCasillas <= 6):
    print("Valor no valido")

if (cantidadDisparos > 45 or cantidadDisparos <= 0):
    print("Valor no valido")

if (cantidadBarcos > 15 or cantidadBarcos <= 0):
    print("Valor no valido")

# creo tabla con valores nxn
tablero: list[list[bool]] =
list = cantidadCasillas
print(tablero)
"""
# elegir posicion del barco y tamano de cada uno (falta)
for cantidadBarcos():
    tamanoBarco: int = int(input("Ingrese un tamano para el barco entre 1 y 3: "))
    barco: int = int(input("Ingrese la ubicacion del barco a colocar en X: "))
    barco: int = int(input("Ingrese la ubicacion del barco a colocar en Y: "))
 

#si usuario no elije que sea true es false
for list in range(cantidadCasillas):

    if (hayBarco = True):
        tablero[list][list] = True
    else:
        tablero[list][list] = False


# dos jugadores


# Mostrar cuantos disparos estaban bien y mal y mostrar tablero final

if (disparosQueQuedan === cantidadDisparos):
    print(tablero)
    print("Acertaste " tirosBien "tiros")

"""
