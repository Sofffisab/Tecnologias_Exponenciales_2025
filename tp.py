# defino datos y pido valores del juego
cantidadFilasyColumnas: int = int(input("Ingrese la cantidad de filas y columnas: "))
cantidadCasillas = cantidadFilasyColumnas * cantidadFilasyColumnas
cantidadDisparos: int = int(input("Ingrese la cantidad de disparos de esta partida: "))
cantidadBarcos: int = int(input("Ingrese la cantidad de barcos a colocar: "))

#poner valores maximos de cada variable

if (cantidadCasillas > 225 or cantidadCasillas < 25):
    print("Valor no valido")

if (cantidadDisparos > 50 or cantidadDisparos <= 0 or cantidadDisparos > cantidadCasillas):
    print("Valor no valido")

if (cantidadBarcos > 15 or cantidadBarcos <= 0):
    print("Valor no valido")

# creo tabla con valores nxn

    tablero: list[list[str]] = [["" for _ in range(cantidadFilasyColumnas)] for _ in range(cantidadFilasyColumnas)]

# averiguamos como hacer esto por una recomendacion de gemini y luego, al buscarlo, leyendo documentacion en https://stackoverflow.com/questions/66425508/what-is-the-meaning-of-for-in-range
# Asi crea cantidad de filas y columnas segun el valor dado por la variable cantidadFilasyColumnas repitiendo el "loop" esa cantidad especifica de veces dada

# elegir posicion del barco 

for _ in range(cantidadBarcos):
        tamanobarco: int = int(input("Ingrese el tamano del barco entre 1 y 3: "))
        if (tamanobarco < 1 or tamanobarco > 3):
            print("Valor no valido")
        barcox: int = int(input("Ingrese la columna para el barco: "))
        barcoy: int = int(input("Ingrese la fila para el barco: "))

        tablero[barcoy - 1][barcox - 1] = "B"  # B es barco

        if (tamanobarco >= 2):

            tablero[barcoy][barcox - 1] = "B"

        if (tamanobarco == 3):
            tablero[barcoy + 1][barcox - 1] = "B"

 
# elegir casillas y si hay barco decir que es true
tablerone = [fila[:] for fila in tablero] # Crear una copia independiente del tablero

aciertos = 0 # Inicializar el contador de aciertos


for n in range (cantidadDisparos):
    casillaSeleccionadax: int = int(input("Ingrese la columna de la casilla: "))
    casillaSeleccionaday: int = int(input("Ingrese la fila de la casilla: "))

   if (tablerone [casillaSeleccionadaY - 1][casillaSeleccionadaX - 1] == B):
        tablerone [casillaSeleccionadaY - 1][casillaSeleccionadaX - 1] == True
        aciertos += 1
    else:
        tablerone [casillaSeleccionadaY - 1][casillaSeleccionadaX - 1] == False




# dos jugadores
    # Hay que hacer dos tableros por jugador, uno para los barcos y otro para los disparos (se printea despues)
    


# Mostrar cuantos disparos estaban bien y mal y mostrar tablero final

for i in range (cantidadFilasyColumnas):
    for j in range(cantidadFilasyColumnas):
        if (tablerone[i][j] != True and tablerone[i][j] != False or tablerone[i][j] == B):
            tablerone[i][j] = false


print("\nTablero de resultados de los disparos:")
for fila in tablerone:
    print(fila)

print("\nAcertaste {aciertos} de {cantidadDisparos} tiros.")

# ayuda de google 