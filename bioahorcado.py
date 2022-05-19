#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from palabras import palabras
from palabras import textos


def elegirPalabra():
	keys = list(palabras.keys())
	palabra = random.choice(keys)
	return palabra.upper()

def jugar(palabra):

	palabraIncompleta = "_" * len(palabra)
	adivino = False
	letrasIntroducidas = []
	intentos = 6
	numPista = 0
	puntos = 0
	terminoPartida = False
	print("\n")
	print("Jueguemos al BioAhorcado! >:3")
	print(dibujarAhorcado(intentos))
	printLetraOculta(palabraIncompleta)
	#print("\n")
	#printPista(palabra)
	print("\n")
	while not adivino and intentos > 0:
		intento = input("Por favor, escribi una letra o palabra: ")
		intento = intento.upper()
		if len(intento) == 1 and intento.isalpha():
			#El usuario introdujo una letra
			if intento in letrasIntroducidas:
			    #La letra ya habia sido elegida antes
				print("\n")
				print("Ya escribiste esta letra antes! <,<")
			elif intento not in palabra:
				#La letra no estaba en la palabra
				print("\n")
				print(intento, "no esta en la palabra :,(")
				intentos -= 1
				letrasIntroducidas.append(intento)
			else:
				#La letra estaba en la palabra
				print("\n")
				print("Bien ahii!!,", intento, "estaba en la palabra :D")
				letrasIntroducidas.append(intento)
				palabraIncompletaList = list(palabraIncompleta)
				indices = [i for i, letra in enumerate(palabra) if letra == intento]
				for index in indices:
					palabraIncompletaList[index] = intento
				palabraIncompleta = "".join(palabraIncompletaList)
				if "_" not in palabraIncompleta:
					adivino = True
					terminoPartida = True
		#El usuario introdujo una palabra
		elif len(intento) > 1 and intento.isalpha():
			if intento != palabra:
				#Le saco todos los intentos por arriesgarse
				intentos = 0
				terminoPartida = True
			else:
				adivino = True
				palabraIncompleta = intento
				terminoPartida = True
		else:
			print("\n")
			print("Lo que ingresaste no es valido >:( ")
		printLetrasIngresadas(letrasIntroducidas)
		print(dibujarAhorcado(intentos))
		printLetraOculta(palabraIncompleta)
		print("\n")
		numPista = printPista(palabra, intentos, numPista, terminoPartida)
		print("\n")
		print("-----------------------------------------------------------------------")
	if adivino:
		print("\n")
		print("Felicidades!! No te ahorcamos :D")
		if len(palabra) <= 3:
			puntos = 5
		elif len(palabra) > 3 and len(palabra) <= 6:
			puntos = 7
		else: 
			puntos = 12
	else:
		print("Uuhhh perdiste, la palabra era: " + palabra + ".")
	print("\n")
	print(textos[palabra.lower()])
	print("\n")
	del palabras[palabra.lower()]	
	return puntos

def printLetrasIngresadas(letras):
	mensaje = 'Letras usadas hasta ahora: '
	for l in letras:
		mensaje = mensaje + l + ' '
	print(mensaje)
		
def printLetraOculta(letra):
	stringParaPrint = ""
	for l in letra:
		stringParaPrint = stringParaPrint + l + " "
	print(stringParaPrint)
	
def printPista(palabra, intentos, numPista, terminoPartida):
	if intentos <= 3 and not terminoPartida:
		pistas = palabras[palabra.lower()]
		if numPista == len(pistas):
			numPista = 0
		#clue = random.choice(pistas)
		clue = pistas[numPista]
		numPista = numPista + 1
		print("\n")
		print("Pista: " + clue)
	return numPista

def dibujarAhorcado(intentos):
	dibujos = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
	return dibujos[intentos]


def main():
	sigue = True
	puntos = 0
	palabra = elegirPalabra()
	puntos = puntos + jugar(palabra)
	while  bool(palabras) and sigue:
			print("Puntos: "+str(puntos))
			if input("Jugar de nuevo BioAhorcadooo? (S/N) ").upper() == "S":
				print("\n")
				palabra = elegirPalabra()
				puntos = puntos + jugar(palabra)
				print("Puntos: "+str(puntos))
			else:
				sigue = False
				print("Vos te lo perdes ;P")
	if not palabras:
		print("Felicidades!!  Terminaste el juego :D")

if __name__ == "__main__":
	main()