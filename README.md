# BioAhorcado

**¿ De que trata ?**

El bioahorcado es un juego creado en python para jugar desde consola con el proposito de enseñar los pasos y los participantes de la
expresion genica al usuario.
Es un juego interactivo en donde el usuario debe ir eligiendo letras para descubrir la palabra oculta.
La palabra oculta es una palabra que tiene relacion con la bioinformatica y el programa la elije de un monton de palabras
ya cargadas previamente.
Cada vez que el usuario elije una letra, la aplicacion ve si es parte de la palabra oculta, de lo contrario restara un intento e ira 
dibujando al hombre en la ahorca.
Si el participante adivina la palabra o se le agotan todos los intentos, abajo se le mostrara informacion con respecto a la palabra para
asegurar el aprendizaje.
Cuando se llega a la mitad de los intentos, el programa comenzara a mostrar pistas, de muy genericas a mas obvias y asi el usuario 
tendra mas chances de acertar y ganar.
El usuario tambien podra arriesgarlo todo y elegir una palabra para ver si acierta de una.

**Como instalarlo**

Debera tener en su sistema operativo (windows o linux) instalado python para ejecutar por consola:
https://www.python.org/downloads/ (Debera elegir la opcion de agregar al PATH si esta en windos)

En una misma carpeta, debera dejar ambos archivos (bioahorcado.py y palabras.py), abrir una consola y 
ejecutar el comando "python bioahorcado.py".

La aplicación lo saludara con un "Jueguemos al BioAhorcado! >:3" y el usuario podra comenzar a escribir letras por turno.

**Como jugarlo**

Al correr el juego en la consola, recibira un saludo inicial y la aplicacion le solicitara inmediatamente que ingrese una letra o palabra.
A demas de esto, el juego mostrara la imagen de una ahorca vacia, la cual se ira completando a medida que el jugador se queda 
sin intentos.
Por debajo del dibujo, se mostrara con guiones la cantidad de letras que tiene la palabra.
````
Jueguemos al BioAhorcado! >:3

                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -

_ _ _ _ _ _ _ _ _ _ _ _ _


Por favor, escribi una letra o palabra:
````
**Configuracion**

Si alguien quisiera modificar el juego, agregar una nueva palabra es muy sencillo y acontinuacion te contamos como.
En el modulo palabras.py tendremos las palabras que se usaran para el juego.
Contaremos con 2 diccionarios, uno llamado "palabras" cuyas claves van a ser las palabras que se usaran para adivinar
en el juego, y cuyo valor va a ser una lista donde contendran pistas acerca de la palabra que tienen como clave.
El otro diccionario tendra el nombre de "textos" y como claves van a ser las mismas palabras que en el diccionario "palabras" pero 
esta vez como valor van a tener un texto informativo que se usara para enseñar al jugador, tras haber ganado o perdido una partida.

De querer agregar una nueva palabra al juego, solo debera agregarla a ambos dicionarios y cargarles una lista de pistas y un 
texto informativo.

A continuacion dejamos un ejemplo de como se deben agregar, notese que cada elemento esta separado por una coma:
````
palabras = {
    'atomo':
		[
		  'Tiene un nucleo', 'Tiene corteza','Parte mas pequeña de un elemento'
		],
	'adn':
		[
		  'Se encuentra en un nucleo','Macromolecula','Tiene la informacion genetica y las instrucciones para crear proteinas'
		]
}

textos = {
    'atomo':'El átomo es la unidad más pequeña de la materia que tiene propiedades de un elemento químico. '+ 
            'Cada átomo se compone de un núcleo y uno o más electrones unidos al núcleo.',

    'adn':'El ADN, o ácido desoxirribonucleico, es el material que contiene la información hereditaria en los humanos y casi todos los demás organismos. '+
        'Casi todas las células del cuerpo de una persona tienen el mismo ADN. La mayor parte del ADN se encuentra en el núcleo celular.'+
        'La información en el ADN se almacena como un código compuesto por cuatro bases químicas, adenina (A), guanina (G), citosina (C) y timina (T). '+
        'El ADN humano consta de unos 3 mil millones de bases, y más del 99 por ciento de esas bases son iguales en todas las personas. '+
        'Una propiedad importante del ADN es que puede replicarse o hacer copias de sí mismo. Cada hebra de ADN en la doble hélice puede servir como patrón para duplicar la secuencia de bases'

}
````
