from random import choice


#dicionarios de las palabras por nivel
palabras_facil = ["casa", "perro", "mesa", "sol", "flor", "agua", "gato", "luna", "silla", "árbol"]
palabras_medio=["ventana","montaña","zapato","naranja","estrella","camino","reloj","sombrero","escuela","cuchara"]
palabras_dificil=["murcielago","arquitectura","psicologia","terremoto","laberinto","astronauta","biblioteca","electricidad","fotografia","marioneta"]

# escoge un nivel acorde a la persona
def elegir(nivel):
    if nivel == "1":
        palabras = choice(palabras_facil)
        print("Seleccione palabras de facil")
    elif nivel == "2":
        palabras = choice(palabras_medio)
        print("Seleccione palabras de medio")
    elif nivel == "3":
        palabras = choice(palabras_dificil)
        print("Seleccione palabras de dificil")
    else:
        return None
    return palabras, len(set(palabras))


# adivinar si la letra esta o no esta en la plabra
def letras(letrasauzar):
    abecedario = 'qwertyuiopasdfghjklzxcvbnm'
    while True:
        letra = input("Ingresa una letra: ").lower()
        if letra in abecedario and len(letra) == 1 and letra not in letrasauzar:
            return letra
        print("Letra no válida o ya en uso")

# crear el tablero de juego sin grafico
def tablero(palabras,letras_corretas):
    tabla=[ letra if letra in letras_corretas  else '-' for letra in palabras]
    print((' '.join(tabla)))
# como declarar la derrota
def perder(palabras):
    print("has perdido")
    print(f' la palabra es: {palabras}')
    return True
# declarar el ganador
def ganar(palabras):
    print("has ganado")
    print(f' la palabra es: {palabras}')
    return True

# menu principal
while True:
    print()
    print("Juego de ahorcado")
    print("--------------------")
    print("Seleccione nivel")
    print("--------------------")
    print("1. facil \n2. medio \n3. dificil \n4. salir ")

    opcion = input("nieveles del 1 al 3, 4 para salir: ")

    if opcion =="4":
        print("adios")
        break

    palabras, letras_unicas = elegir(opcion)
    letras_corretas = []
    letras_incorrectas = []
    vidas =6
    aciertos = 0
    juego_terminado = False

#el juego no a terminado se repite asta que se gane o pierda
    while not juego_terminado:
        tablero(palabras,letras_corretas)
        print(f" letrtas incorrectas: {', '.join(letras_incorrectas)}")
        print(f" vidas: {vidas}")

        letra = letras(letras_corretas+ letras_incorrectas)

        if letra in palabras:
            letras_corretas.append(letra)
            aciertos = len(set(letras_corretas))
        else:
            letras_incorrectas.append(letra)
            vidas -= 1

        if vidas == 0:
            juego_terminado = perder(palabras)
        elif vidas == letras_unicas:
            juego_terminado = ganar(palabras)
