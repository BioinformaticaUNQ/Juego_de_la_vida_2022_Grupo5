# El juego de la vida

# DESAFIO I: Enumerá las diferencias que existen entre una célula procariota y eucariota.**

Eucariotas:
1. Células de las plantas, animales y hongos
2. Es más grande que las Procariotas y más compleja
3. Tiene organelas en el citoplasma
4. El ADN está separado del citoplasma por una membrana nuclear
5. Se divide en célula animal y vegetal

Procariotas
1. Células de las bacterias
2. Más simple y pequeña
3. Delimitada por una membrana plasmática con pliegues hacia el interior (laminillas y mesosoma)
4. Por fuera tiene pared celular
5. El ADN está en una zona del citoplasma que se llama nucleoide
6. Tiene ribosomas
7. Se trasladan con un flagelo


# DESAFIO II: Crea un script en Python que tome como argumento una secuencia proteica e imprima una cadena de ARN codificante.
# Podés usar de ejemplo el siguiente péptido (cadena corta de aminoácidos):

Sec1: ‘ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA'

**Aclaracion: Este codigo elige un codon de forma aleatoria para un aminoacido pudiendo no ser el correcto**
**Y el resultado puede no tener sentido biologico**

#!/usr/bin/env python3
import argparse
import random

parser = argparse.ArgumentParser(description='Destranscribe una secuencia de una proteina a codones')
parser.add_argument('-s', '--secuencia', type=str, help='secuencia', required=True)

args = parser.parse_args()

aminoacidos = {
    "V":["GUU","GUC","GUA","GUG"],
    "L":["CUU","CUC","CUA","CUG"],
	"T":["ACU","ACC","ACA","ACG"],
	"K":["AAA","AAG"],
	"W":["UGG"],
	"H":["CAU","CAC"],
	"F":["UUU","UUC"],
	"I":["AUU", "AUC", "AUA"],
	"R":["AGA", "AGG", "CGU", "CGC", "CGA", "CGG"],
    "M":["AUG"],
	"A":["GCU", "GCC", "GCA", "GCG"],
	"P":["CCA", "CCU", "CCG", "CCC"],
	"G":["GGU", "GGC", "GGA", "GGG"],
	"S":["UCU","UCC","UCA","UCG","AGU","AGC"],
	"C":["UGU","UGC"],
	"N":["AAU","AAC"],
	"Q":["CAG","CAA"],
	"Y":["UAU","UAC"],
	"D":["GAU","GAC"],
	"E":["CAA","CAG"]
}

arn = ""

for a in args.secuencia:
    arn = arn + random.choice(aminoacidos[a])
	

print(arn)


# DESAFIO III: Creá un script en Python que, tomando como input un archivo con una secuencia de ADN, permita 
# identificar las regiones promotoras de un gen, considerando que tal región comienza y termina con la caja TATA.

#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Toma una secuencia de ADN e identifica los promotores TATA')
parser.add_argument('-s', '--secuencia', type=str, help='secuencia', required=True)

args = parser.parse_args()

genes = (args.secuencia).split('TATA')

print(genes)

