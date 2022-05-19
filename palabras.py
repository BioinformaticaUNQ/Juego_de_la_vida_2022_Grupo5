#!/usr/bin/env python3
# -*- coding: utf-8 -*-
palabras = {
    'atomo':
		[
		  'Tiene un nucleo', 'Tiene corteza','Parte mas pequeña de un elemento'
		],
	'proton':
		[
		  'Se encuentra en un nucleo','Particula con carga electrica','Elemento del atomo'
		],
	'neutron':
		[
		  'Se encuentra en un nucleo','Particula sin carga electrica','Elemento del atomo'
		],
	'electron':
		[
		  'No se encuentra en el nucleo','Particula con carga electrica','Elemento del atomo'
		],
	'ion':
		[
		  'Particula con carga electrica','Se origina al perder o ganar electrones'
		],
	'ionico':
		[
		  'Tipo de enlace','Tipo de enlace para formar moleculas', 'Enlace efectuado por la atraccion de cargas electricas opuestas'
		],
	'covalente':
		[
		  'Tipo de enlace','Tipo de enlace para formar moleculas', 'Enlace donde se intercambian electrones'
		],
	'aminoacido':
		[
		  'Tipo de molecula', 'Forman cadenas','Se forman en grupo de 3 nucleotidos'
		],
	'amino':
		[
		  'Grupo de un aminoacido'
		],
	'carboxilo':
		[
		  'Grupo de un aminoacido'
		],
	'peptidico':
		[
		  'Tipo de enlace','Tipo de enlace para formar macromoleculas','Enlace de aminoacidos'
		],
	'hidrofobico':
		[
		  'Propiedad de una molecula','Repulsion al agua'
		],
	'hidrofilico':
		[
		  'Propiedad de una molecula','Atraccion al agua'
		],
	'proteina':
		[
		  'Construyen y mantienen en funcionamiento celulas, tejidos y organismos','Se forma por enlaces peptidicos','Cadena de aminoacidos'
		],
	'adn':
		[
		  'Se encuentra en un nucleo','Macromolecula','Tiene la informacion genetica y las instrucciones para crear proteinas'
		],
	'ribosoma':
		[
		  'Se encuentra en el citoplasma','Fabrica proteinas a partir de aminoacidos','Traduce codones'
		],
	'arn':
		[
		  'Macromolecula','Se le dice mensajero','Resultado de la transcripcion del ADN'
		],
	'nucleotido':
		[
		  'Monomero','Forman codones en grupos de a 3','A,C,T,G'
		],
	'eucariota':[
		  'Tiene nucleo','De gran tamaño','Tipo de celula'
		],
	'procariota':[
		  'Sin nucleo','Tiene flagelo','Tipo de celula'
		],
	'gen':[
		  'Unidad de informacion','Fragmento del ADN','Contiene una secuencia de nucleotidos'
		],
	'celula':[
		  'Tiene nucleo','Tiene memebrana','Tiene citoplasma'
		],
	'transcripcion':[
		  'Proceso de convertir ADN en ARN','Se crea un ARN a partir de la secuencia de un gen','Proceso donde un ARN sale del nucleo de la celula al citoplasma'
		],
	'traduccion':[
		  'Proceso de convertir ARN en proteina','Proceso donde un ARN entra a un ribosoma de la celula','De una secuencia de nucleotidos, se traducen aminoacidos que formaran una proteina'
		]
}



textos = {
    'atomo':'El átomo es la unidad más pequeña de la materia que tiene propiedades de un elemento químico. '+ 
            'Cada átomo se compone de un núcleo y uno o más electrones unidos al núcleo.',
            
    'proton':'Se lo conoce como nucleon ya que conforma el núcleo de los átomos junto a los neutrones. '+
        'Es una partícula subatómica de carga eléctrica positiva. '+
        'En un átomo, el número de protones en el núcleo determina las propiedades químicas del átomo y qué elemento químico es.',
        
    'neutron':'Se lo conoce como nucleon ya que conforma el núcleo de los átomos junto a los protones. '+
        'Es una partícula subatómica sin carga eléctrica.',
        
    'electron':'Es una partícula subatómica de carga eléctrica negativa. '+
        'No habitan en el nucleo del atomo, sino que lo ahcen en su corteza.',
    
    'ion':'Un ion es un atomo o molecula que ha perdido o ganado electrones. '+
        'Cuando se pierden electrones, se vuele un atomo de carga positiva, un cation, y si los ganan se vuelve un atomo de carga negativa, un anion.',

    'ionico':'Un enlace ionico se da por la atraccion entre iones de cargas electricas opuestas.',
    
    'covalente':'Un enlace covalente se da cuando 2 atomos se unen e intercambian electrones.',
    
    'aminoacido':'Los aminoácidos son moléculas que se combinan para formar proteínas.',
    
    'amino':'El Grupo Amino es un grupo funcional derivado del amoníaco (NH3) y componente de un aminoacido.',
    
    'carboxilo':'Los ácidos carboxílicos constituyen un grupo de compuestos, caracterizados porque poseen un grupo funcional llamado grupo carboxilo o grupo carboxi (–COOH) y es componente de un aminoacido',
    
    'hidrofobico':'La hidrofobia es un término derivado del griego hydro, que significa agua, y phobos, que significa miedo. Las sustancias hidrofóbicas están compuestas por moléculas no polares que repelen las masas de agua y atraen a otras moléculas neutras y a los disolventes no polares.',
    
    'hidrofilico':'Hidrófilo o hidrofílico (del griego hydros, agua, y philia, amistad) es una sustancia que tiene afinidad por el agua.',
    
    'proteina':'Las proteínas son macromoléculas formadas por cadenas lineales de aminoácidos. '+
        'Las proteínas están formadas por aminoácidos y esta secuencia está determinada por la secuencia de nucleótidos de su gen correspondiente. '+
        'La información genética determina qué proteínas tiene una célula, un tejido y un organismo.​',
        
    'adn':'El ADN, o ácido desoxirribonucleico, es el material que contiene la información hereditaria en los humanos y casi todos los demás organismos. '+
        'Casi todas las células del cuerpo de una persona tienen el mismo ADN. La mayor parte del ADN se encuentra en el núcleo celular.'+
        'La información en el ADN se almacena como un código compuesto por cuatro bases químicas, adenina (A), guanina (G), citosina (C) y timina (T). '+
        'El ADN humano consta de unos 3 mil millones de bases, y más del 99 por ciento de esas bases son iguales en todas las personas. '+
        'Una propiedad importante del ADN es que puede replicarse o hacer copias de sí mismo. Cada hebra de ADN en la doble hélice puede servir como patrón para duplicar la secuencia de bases',
    
    'ribosoma':'Los ribosomas son orgánulos que reciden en el citoplasma de las celulas. Son los centros celulares de traducción que hacen posible la expresión de los genes. Es decir, son los encargados de la síntesis de proteínas a partir de la información contenida en el ADN, que llega transcrita a los ribosomas en forma específicamente de ARN mensajero.',
    
    'arn':'El ARN, o ácido ribonucleico, es un ácido nucleico similar en estructura al ADN pero con algunas diferencias sutiles. La célula utiliza el ARN para una serie de tareas diferentes; una de estas moléculas se llama ARN mensajero o ARNm. Y es la molécula de ácido nucleico cuya traducción transfiere información del genoma a las proteínas. '+
        'el ARN esté formado por una única cadena. Una molécula de ARN tiene un eje formado por grupos fosfato alternantes y el azúcar ribosa, en lugar de la desoxirribosa del ADN. Unida a cada azúcar hay una de cuatro bases: adenina (A), uracilo (U), citosina (C) o guanina (G).',
    
    'nucleotido':'Un nucleótido es la pieza básica de los ácidos nucleicos. El ARN y el ADN son polímeros formados por largas cadenas de nucleótidos. Un nucleótido está formado por una molécula de azúcar (ribosa en el ARN o desoxirribosa en el ADN) unido a un grupo fosfato y una base nitrogenada.',
    
    'eucariota':'Las células eucariotas son aquellas cuyo material hereditario (ADN) se encuentra envuelto por una membrana, la envoltura nuclear, que forma un núcleo celular. Se caracterizan también por presentar citoplasma en el que se encuentran los distintos orgánulos y el núcleo. Existen diferentes tipos de células eucariotas aunque las más destacables són las animales y vegetales.',
    
    'procariota':'Las células procariotas son aquellas que no tienen núcleo diferenciado, de manera que su ADN se encuentra localizado en el citoplasma pero no encerrado en una cubierta membranosa. Todas las células procariotas son organismos unicelulares.',
    
    'gen':'El gen se considera la unidad básica de la herencia. Los genes se transmiten de los progenitores a la descendencia y contienen la información necesaria para especificar los rasgos físicos y biológicos. La mayoría de los genes codifican para proteínas específicas, o segmentos de proteínas, que tienen diferentes funciones en el cuerpo. Los seres humanos tienen aproximadamente 20,000 genes que codifican para proteínas.',
    
    'celula':'Unidad anatómica fundamental de todos los organismos vivos, generalmente microscópica, formada por citoplasma, uno o más núcleos y una membrana que la rodea.',
    
    'transcripcion':'La transcripcion es el proceso de generación de una copia de ARN a partir de una secuencia de ADN de un gen. Esta copia, llamada ARN mensajero (ARNm), es portadora de la información sobre la proteína que el gen tiene codificada en ADN. En los seres humanos y otros organismos complejos, el ARN se desplaza desde el núcleo de la célula al citoplasma de la célula (compartimento acuoso), donde se usa para sintetizar la proteína codificada.',
    
    'traduccion':'La traducción, en lo que se relaciona a la genómica, es el proceso por el cual la información codificada en el ARN mensajero (ARNm) dirige la adición de aminoácidos durante la síntesis proteica. La traducción tiene lugar en los ribosomas en el citoplasma de la célula, donde se lee el ARN se traduce en la formación de cadenas de aminoácidos que generan la proteína sintetizada.',
    
    'peptidico':'El enlace peptídico es un enlace de tipo amida entre el grupo amino (–NH2) de un aminoácido y el grupo carboxilo (–COOH) de otro aminoácido. '+
        'Los peptidos y las proteínas están formados por la unión de aminoácidos mediante enlaces peptídicos. '+
        'El enlace se da, al perder el grupo carboxilo un hidrogeno y un oxigeno y el grupo amino un hidrogeno.'
    
}