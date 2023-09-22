# INF-253 Lenguajes de Programación
# Tarea 1: Python  19 de agosto de 2022

## 1. Pixelart
Un jugador de Minecraft amante del pixelart, un dıa buscando creaciones de otros jugadores, se encontro con un sitio web que aseguraba tener diseños que nunca antes habıa visto, con instrucciones muy detalladas de como construirlos; sin embargo, este sitio no contaba con imagenes para saber como se ven los resultados de seguir esas instrucciones!
<p align="center">Code 1: Ejemplo de instrucciones</p>

~~~
Ancho 8
Color de fondo RGB(13,181,13)
Avanzar Derecha Avanzar 2
Pintar Negro Avanzar
Repetir 2 veces { Pintar Negro Izquierda Avanzar }
Pintar Negro
Derecha Avanzar 3
Pintar Negro Avanzar
Repetir 2 veces { Pintar Negro Derecha Avanzar }
Pintar Negro
Izquierda Avanzar
Repetir 3 veces { Avanzar Pintar Negro }
Derecha Avanzar 3 Derecha
Repetir 3 veces { Pintar Negro Avanzar }
Derecha Avanzar
Repetir 3 veces {
Pintar Negro Avanzar
Pintar Negro Derecha Avanzar
Derecha Avanzar Derecha Derecha
}
~~~

Es por lo anterior que este jugador le pidio a los alumnos de Lenguajes de Programacion que utilicen los contenidos del curso para crear un programa capaz de interpretar las instrucciones del sitio y producir una imagen del resultado.

Para esta tarea se debe utilizar Python 3 y los siguientes paquetes:
- [RegEx](https://docs.python.org/3/library/re.html) para las expresiones regulares de la tarea. **Tareas que no utilicen RegEx no seran revisadas**.
- [NumPy](https://numpy.org) y [Pillow](https://python-pillow.org) para convertir los resultados a imagenes. El codigo para este proceso se les sera entregado.

## 2. Lenguaje PixelArt (LPA)

#### 2.1. Acerca de LPA

El Lenguaje PixelArt es un nuevo lenguaje interactivo que permite a un jugador, mediante una secuencia de instrucciones, producir uno de los pixelarts del sitio. Siempre se asume que el jugador comienza en la esquina superior izquierda apuntando hacia la derecha. El objetivo es simular el procedimiento que seguira un jugador y guardar el resultado como una matriz (lista de listas en Python) de valores RGB (tupla de 3 valores entre 0 y 255 en Python).

#### 2.2. Matriz

La matriz sera de tamaño n × n, siendo n un valor que se especificara mas adelante, donde inicialmente todos los valores parten en un mismo color.

#### 2.3. Comandos

Todo archivo siempre comienza con los siguientes comandos en este orden:
- Ancho N : Indica que la imagen sera de tama˜no N × N.
- Color de fondo Color: Indica el color de fondo que tendra la imagen, es decir, si un bloque no es pintado entonces sera de este color. El formato que sigue Color se indica mas adelante.

Posterior a estos habra una lınea en blanco y luego seguiran las instrucciones, las cuales pueden ser cualquier combinacion de las siguientes:
- Izquierda: El jugador debe girar en 90° a la izquierda.
- Derecha: El jugador debe girar en 90° a la derecha.
- Avanzar N : El jugador debe avanzar N cuadros en la direccion en la que esta mirando. En caso de que no se entregue un numero, el jugador debera avanzar 1 bloque.
- Pintar Color: El jugador debe pintar el bloque en el que se encuentra de color Color. El formato que sigue Color se indica mas adelante.
- Repetir N veces { Instrucciones }: El jugador debe repetir las instrucciones indicadas en Instrucciones N veces. Las instrucciones pueden ser cualquiera de las anteriormente nombradas a excepcion de Ancho y Color de fondo. Esto significa que pueden haber instrucciones de Repetir anidadas.

Cuando un comando requiera de un Color como parametro, este podra recibir uno de los siguientes valores:

- Rojo: Debera pintar de color rojo, escribiendo en la matriz de memoria la tupla (255,0,0).
- Verde: Debera pintar de color verde, escribiendo en la matriz de memoria la tupla (0,255,0).
- Azul: Debera pintar de color azul, escribiendo en la matriz de memoria la tupla (0,0,255).
- Negro: Debera pintar de color negro, escribiendo en la matriz de memoria la tupla (0,0,0).
- Blanco: Debera pintar de color blanco, escribiendo en la matriz de memoria la tupla (255,255,255).
- RGB(R,G,B): Debera pintar del color indicado, escribiendo en la matriz de memoria la tupla (R,G,B).
  
A continuacion se presenta un EBNF que describe formalmente la sintaxis que siguen las instrucciones de un programa:

<p align="center">Code 2: EBNF</p>

~~~
instruccion ::= ’Izquierda’ | ’Derecha’
    | ’Avanzar’ [numero] | ’Pintar’ color
    | ’Repetir’ numero ’veces’ ’{’ {instruccion} ’}’

numero ::= 0 | no_zero {’0’ | no_zero}

no_zero ::= ’1’ | ’2’ | ’3’ | ’4’ | ’5’ | ’6’ | ’7’ | ’8’ | ’9’

color ::= ’Rojo’ | ’Verde’ | ’Azul’ | ’Negro’ | ’Blanco’
    | ’RGB(’ numero ’,’ numero ’,’ numero ’)’

~~~

Pueden haber multiples instrucciones en una lınea. Adicionalmente las instrucciones de tipo Repetir pueden abarcar multiples lineas.

#### 2.4. Orden de operaciones

Las instrucciones siempre se ejecutan de izquierda a derecha.

## 3. Objetivo de la tarea

Cada estudiante debe crear un programa el cual permita recibir una cantidad indefinida de lıneas en un archivo codigo.txt, en donde la primera lınea siempre indicara el tama˜no de la matriz que se utilizara, la segunda el color de fondo, la tercera sera una lınea en blanco y luego cada lınea siguiente correspondera a una serie de instrucciones.

Su programa debe ser capaz interpretar el codigo, detectar errores de sintaxis, y detectar errores de ejecucion. Sintaxis: a partir del archivo codigo.txt, su programa debe generar un archivo errores.txt, donde se encontraran todas las lıneas que tengan una sintaxis incorrecta, indicando el numero de lınea en la cual se encuentra el error, en el caso que no hayan errores el archivo debera contener la frase “No hay errores!”. Interprete: debe producir pixelart.png y mostrar por consola los valores de la matriz RGB en caso de que la ejecucion y la revision de sintaxis sea exitosa. Si durante la ejecucion las instrucciones causaran que el jugador salga del area que cubre la matriz, se debe indicar por consola la lınea que produjo este error y terminar la ejecucion.

Para producir las imagenes pueden utilizar el codigo del siguiente GitHub Gist:

<https://gist.github.com/HectorxH/13f2c125ffbbfde381aede4a8ddbadeb>

#### 3.1. Ejemplos

#### 3.1.1. Ejemplo 1

<p align="center">Code 3: Ejemplo 1</p>

~~~
Ancho 10
Color de fondo Blanco

Avanzar Derecha Avanzar
Repetir 4 veces {
Repetir 8 veces { Pintar Negro Avanzar }
Derecha Derecha Avanzar Derecha
}
~~~
<p align="center">Code 4: errores.txt</p>


~~~
1 No hay errores!
~~~
<p align="center">Figura 1: pixelart.png</p>


#### 3.1.2. Ejemplo 2

<p align="center">Code 5: Ejemplo 2</p>


~~~
1 Ancho 3
2 Color de fondo RGB(0,0,0)
3
4 Pintar Rojo Avanzar 2 Derecha
5 Pintar Verde Avanzar 2 Derecha
6 Pintar Azul Avanzar 2 Derecha
7 Pintar Blanco Avanzar Derecha Avanzar
8 Pintar RGB(0,255,255)
~~~
<p align="center">Code 6: errores.txt</p>


~~~
1 No hay errores!
~~~
<p align="center">Figura 2: pixelart.png</p>


#### 3.1.3. Ejemplo 3
<p align="center">Code 7: Ejemplo 3</p>


~~~
1 Ancho 3
2 Color de fondo Negro
3
4 Repetir 2 {
5 Pintar RGB(255,0,0) Avanzar Derecha 1 Avanzar
6 }
7 Pintar RGB(255,0,0)
~~~
<p align="center">Code 8: errores.txt</p>


~~~
1 4 Repetir 2 {
2 5 Pintar RGB(255,0,0) Avanzar Derecha 1 Avanzar
~~~

## 4. Sobre Entrega

Se debera entregar un programa llamado pixelart.py. Los ayudantes correctores pueden realizar descuentos en caso de que el codigo se encuentre muy desordenado. Las funciones implementadas deben ser comentadas de la siguiente forma. SE HARAN DESCUENTOS POR FUNCION NO COMENTADA
~~~
’’’
Descripcion de la funcion

Parametros:
a (int): Descripcion del parametro a
b (int): Descripcion del parametro b

Retorno:
c (str): Descripcion del parametro c
’’’
~~~
Se debe trabajar de forma individual obligatoriamente. La entrega sera vıa aula y el plazo maximo de entrega es hasta el 7 de septiembre. Por cada dıa de atraso se descontaran 24 pts (-1 pt por cada hora de atraso).

Las copias seran evaluadas con nota 0 y se informaran a las respectivas autoridades.

Solo se contestaran dudas realizadas en AULA y que se realicen al menos 48 horas antes de la fecha de entrega original.

## 5. Calificacion
#### 5.1. Entrega
- Uso correcto de expresiones regulares (20 pts)
  1. No usa expresiones regulares. Utiliza otros metodos que no son los pedidos para la tarea, por ejemplo split e . (0 pts)
  2. Usa una gran y unica expresion regular. Provocando ası una falta de modularizacion de las expresiones. (MAX 12 pts)
  3. Crea diferentes expresiones y las utiliza de manera correcta, aprovechandose de la modularizacion generada. (MAX 20 pts)
- Deteccion de errores (20 pts)
  1. No detecta correctamente ningun tipo de error (0 pts)
  2. Permite tan solo detectar errores simples, ya sea en la ejecucion como en la revision de sintaxis. (MAX 5 pts)
  3. Permite detectar errores de mayor dificultad, pero falla en instrucciones recursivas o no detecta errores durante la ejecucion (MAX 15 pts)
  4. Detecta todo tipo de error probado, siendo no solo errores simples de sintaxis, si no que tambien errores de anidacion de comandos o secuencias incorrectas (MAX 20 pts)
- Ejecucion de comandos (60 pts)
  1. Ancho + Color de fondo 5 pts.
  2. Izquierda + Derecha 10 pts.
  3. Avanzar 10 pts.
  4. Pintar color 15 pts.
  5. Repetir veces 20 pts.
Se asignara puntaje parcial por funcionamiento parcialmente correcto.
#### 5.2. Descuentos
- Falta de comentarios (-10 pts c/u MAX 30 pts)
- Falta de orden (entre -5 y -20 pts dependiendo de que tan desordenado)
- Dıa de atraso (-1 pt por cada hora de atraso)
- Mal nombre en algun archivo entregado (-5 pts c/u)

Nombre: Martin Pino Cornejo
Rol: 202073528-k
Instrucciones: El archivo pixelart.py debe estar en la misma carpeta que codigos.txt

