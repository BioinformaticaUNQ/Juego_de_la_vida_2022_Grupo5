#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from palabras import palabras


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
		#El usuario introdujo una palabra
		elif len(intento) > 1 and intento.isalpha():
			if intento != palabra:
				#Le saco todos los intentos por arriesgarse
				intentos = 0
			else:
				adivino = True
				palabraIncompleta = intento
		else:
			print("\n")
			print("Lo que ingresaste no es valido >:( ")
		printLetrasIngresadas(letrasIntroducidas)
		print(dibujarAhorcado(intentos))
		printLetraOculta(palabraIncompleta)
		print("\n")
		numPista = printPista(palabra, intentos, numPista)
		print("\n")
		print("-----------------------------------------------------------------------")
	if adivino:
		print("\n")
		print("Felicidades!! No te ahorcamos :D")
	else:
		print("Uuhhh perdiste, la palabra era: " + palabra + ".")
	del palabras[palabra.lower()]		

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
	
def printPista(palabra, intentos, numPista):
	if intentos <= 3:
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
	palabra = elegirPalabra()
	jugar(palabra)
	while input("Jugar de nuevo BioAhorcadooo? (S/N) ").upper() == "S":
		if not palabras:
			print("Felicidades!!  Terminaste el juego :D")
		else:
			print("\n")
			palabra = elegirPalabra()
			jugar(palabra)
	print("Vos te lo perdes ;P")

if __name__ == "__main__":
	main()