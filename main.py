import random
def obtenerDigitos():
    digitosIntentos = int(input("Ingrese el numero de digitos. Note que este sera su numero de intentos. El numero debe estar entre 4 y 9: "))
    if (digitosIntentos < 4 or digitosIntentos > 9):
        print("Error: el numero debe esta entre 4 y 9")
        return -1
    return digitosIntentos

def generarNumero(n):
    numFinal = 0
    cont = 0
    lstNumeros = list(range(10))
    while cont < n:
        num = random.randint(0,len(lstNumeros)-1)
        if cont != 0 or num != 0:
            if lstNumeros[num] != 0:
                numFinal += lstNumeros[num] * (10**cont)
            else:
                numFinal *= 10
            lstNumeros.pop(num)
            cont += 1
    return numFinal

def ingresoDeIntentos(n, nroIntento):
    numJugador = int(input("Intento " + str(nroIntento) + ": "))
    if numJugador < 10 ** (n-1) or numJugador >= 10 ** (n):
        print("Numero invalido. FIN DE LA PARTIDA")
        return -1
    return numJugador

def evaluarNumero(secuencia, num):
    toques = 0
    famas = 0
    if secuencia == num:
        return 1
    else:
        secuenciaStr = str(secuencia)
        numStr = str(num)
        for i in range(len(numStr)):
            if numStr[i] in secuenciaStr:
                if numStr[i] == secuenciaStr[i]:
                    famas += 1
                else:
                    toques += 1
        print("Toques: " + str(toques) + " - Famas: " + str(famas))
        return 0

def jugada(n):
    secuenciaSecreta = generarNumero(n)
    print(secuenciaSecreta)
    gano = False
    intento = 0
    numJugador = ingresoDeIntentos(n, intento+1)
    while not(gano) and intento < n and numJugador != -1:
        estadoPartida = evaluarNumero(secuenciaSecreta, numJugador)
        if estadoPartida == 1:
            gano = True
            print("¡Felicitaciones! Has acertado en " + str(intento+1) + " intentos")
        else:
            intento += 1
            if intento < n:
                numJugador = ingresoDeIntentos(n, intento+1)
    if not(gano) and numJugador != -1:
        print("Fin del juego. La secuencia era " + str(secuenciaSecreta))
    return gano

def iniciarJuego():
    partidasJugadas = 0
    partidasGanadas = 0
    partidasPerdidas = 0
    jugar = True
    digitos = obtenerDigitos()
    while jugar and digitos != -1:
        estadoPartida = jugada(digitos)
        if estadoPartida:
            partidasGanadas += 1
        else:
            partidasPerdidas += 1
        partidasJugadas += 1
        jugar = int(input('Desea jugar nuevamente? Si (1) / No (0): '))
        if jugar:
            digitos = obtenerDigitos()
    print("Jugados: " + str(partidasJugadas) + " - Ganados: " + str(partidasGanadas) + " - Perdidos: " + str(partidasPerdidas))

def main():
    iniciarJuego()


main()

