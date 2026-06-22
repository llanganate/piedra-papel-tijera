import random

# Opciones del juego
opciones = ["piedra", "papel", "tijera"]

# Variables globales
ganadas = 0
perdidas = 0
empates = 0
historial = []


# Mostrar menú principal
def mostrar_menu():
    print("\n===== PIEDRA, PAPEL O TIJERA =====")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Ver historial")
    print("5. Ver marcador")
    print("6. Salir")


# Convertir opción numérica en jugada
def obtener_jugada(opcion):
    if opcion == "1":
        return "piedra"
    elif opcion == "2":
        return "papel"
    elif opcion == "3":
        return "tijera"
    return None


# Determinar ganador
def determinar_resultado(jugador, cpu):
    if jugador == cpu:
        return "Empate"

    elif (jugador == "piedra" and cpu == "tijera") or \
         (jugador == "papel" and cpu == "piedra") or \
         (jugador == "tijera" and cpu == "papel"):
        return "Ganaste"

    return "Perdiste"


# Mostrar historial
def mostrar_historial():
    print("\n===== HISTORIAL =====")

    if len(historial) == 0:
        print("No existen partidas registradas.")
    else:
        for partida in historial:
            print(partida)


# Mostrar marcador
def mostrar_marcador():
    print("\n===== MARCADOR =====")
    print("Ganadas:", ganadas)
    print("Perdidas:", perdidas)
    print("Empates:", empates)


# Programa principal
while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "6":
        print("Gracias por jugar.")
        break

    elif opcion == "4":
        mostrar_historial()

    elif opcion == "5":
        mostrar_marcador()

    elif opcion in ["1", "2", "3"]:

        jugador = obtener_jugada(opcion)
        cpu = random.choice(opciones)

        resultado = determinar_resultado(jugador, cpu)

        print("\nTu jugada:", jugador)
        print("CPU:", cpu)
        print("Resultado:", resultado)

        if resultado == "Ganaste":
            ganadas += 1

        elif resultado == "Perdiste":
            perdidas += 1

        else:
            empates += 1

        historial.append(
            f"Jugador: {jugador} | CPU: {cpu} | Resultado: {resultado}"
        )

    else:
        print("Opción incorrecta.")