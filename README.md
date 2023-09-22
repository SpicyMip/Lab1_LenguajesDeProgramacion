# INF-253 Lenguajes de Programación



Tarea 1: Python  19 de agosto de 2022
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
- Ancho N : Indica que la imagen ser´a de tama˜no N × N.
- Color de fondo Color: Indica el color de fondo que tendr´a la imagen, es decir, si un bloque no es pintado entonces sera de este color. El formato que sigue Color se indica mas adelante.

Posterior a estos habra una lınea en blanco y luego seguiran las instrucciones, las cuales pueden ser cualquier combinacion de las siguientes:
- Izquierda: El jugador debe girar en 90° a la izquierda.
- Derecha: El jugador debe girar en 90° a la derecha.
- Avanzar N : El jugador debe avanzar N cuadros en la direccion en la que esta mirando. En caso de que no se entregue un numero, el jugador debera avanzar 1 bloque.
- Pintar Color: El jugador debe pintar el bloque en el que se encuentra de color Color. El formato que sigue Color se indica mas adelante.
- Repetir N veces { Instrucciones }: El jugador debe repetir las instrucciones indicadas en Instrucciones N veces. Las instrucciones pueden ser cualquiera de las anteriormente nombradas a excepcion de Ancho y Color de fondo. Esto significa que pueden haber instrucciones de Repetir anidadas.

Cuando un comando requiera de un Color como parametro, este podra recibir uno de los siguientes valores:

- Rojo: Deber´a pintar de color rojo, escribiendo en la matriz de memoria la tupla (255,0,0).
- Verde: Deber´a pintar de color verde, escribiendo en la matriz de memoria la tupla (0,255,0).
- Azul: Deber´a pintar de color azul, escribiendo en la matriz de memoria la tupla (0,0,255).
- Negro: Deber´a pintar de color negro, escribiendo en la matriz de memoria la tupla (0,0,0).
- Blanco: Deber´a pintar de color blanco, escribiendo en la matriz de memoria la tupla (255,255,255).
- RGB(R,G,B): Deber´a pintar del color indicado, escribiendo en la matriz de memoria la tupla (R,G,B).
  
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

Cada estudiante debe crear un programa el cual permita recibir una cantidad indefinida de lıneas en un archivo codigo.txt, en donde la primera l´ınea siempre indicara el tama˜no de la matriz que se utilizar´a, la segunda el color de fondo, la tercera ser´a una l´ınea en blanco y luego cada l´ınea siguiente corresponder´a a una serie de instrucciones.

Su programa debe ser capaz interpretar el c´odigo, detectar errores de sintaxis, y detectar errores de ejecuci´on. Sintaxis: a partir del archivo codigo.txt, su programa debe generar un archivo errores.txt, donde se encontrar´an todas las l´ıneas que tengan una sintaxis incorrecta, indicando el numero de l´ınea en la cual se encuentra el error, en el caso que no hayan errores el archivo deber´a contener la frase “No hay errores!”. Int´erprete: debe producir pixelart.png y mostrar por consola los valores de la matriz RGB en caso de que la ejecuci´on y la revisi´on de sintaxis sea exitosa. Si durante la ejecuci´on las instrucciones causaran que el jugador salga del ´area que cubre la matriz, se debe indicar por consola la l´ınea que produjo este error y terminar la ejecuci´on.

Para producir las im´agenes pueden utilizar el c´odigo del siguiente GitHub Gist:

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
Code 4: errores.txt
~~~
1 No hay errores!
~~~
Figura 1: pixelart.png

3.1.2. Ejemplo 2
Code 5: Ejemplo 2
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
Code 6: errores.txt
~~~
1 No hay errores!
~~~
Figura 2: pixelart.png

3.1.3. Ejemplo 3
Code 7: Ejemplo 3
~~~
1 Ancho 3
2 Color de fondo Negro
3
4 Repetir 2 {
5 Pintar RGB(255,0,0) Avanzar Derecha 1 Avanzar
6 }
7 Pintar RGB(255,0,0)
~~~
Code 8: errores.txt
~~~
1 4 Repetir 2 {
2 5 Pintar RGB(255,0,0) Avanzar Derecha 1 Avanzar
~~~

## 4. Sobre Entrega

Se deber´a entregar un programa llamado pixelart.py. Los ayudantes correctores pueden realizar descuentos en caso de que el c´odigo se encuentre muy desordenado. Las funciones implementadas deben ser comentadas de la siguiente forma. SE HARAN DESCUENTOS POR FUNCION NO COMENTADA
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
Se debe trabajar de forma individual obligatoriamente.
La entrega debe realizarse en .tar.gz y debe llevar el nombre:
Tarea1LP RolAlumno.tar.gz
El archivo README.txt debe contener nombre y rol del alumno e instrucciones detalladas para la correcta utilizaci´on de su programa. De no incluir
README se realizara un descuento.
La entrega ser´a v´ıa aula y el plazo m´aximo de entrega es hasta el 7 de septiembre.
Por cada d´ıa de atraso se descontar´an 24 pts (-1 pt por cada hora de atraso).
Las copias ser´an evaluadas con nota 0 y se informar´an a las respectivas autoridades.
Solo se contestaran dudas realizadas en AULA y que se realicen al menos 48
horas antes de la fecha de entrega original.
5. Calificaci´on
5.1. Entrega
Uso correcto de expresiones regulares (20 pts)
1. No usa expresiones regulares. Utiliza otros m´etodos que no son los pedidos para la
tarea, por ejemplo split e . (0 pts)
2. Usa una gran y ´unica expresi´on regular. Provocando as´ı una falta de modularizaci´on
de las expresiones. (MAX 12 pts)
3. Crea diferentes expresiones y las utiliza de manera correcta, aprovechandos´e de la
modularizaci´on generada. (MAX 20 pts)
Detecci´on de errores (20 pts)
1. No detecta correctamente ning´un tipo de error (0 pts)
6
2. Permite tan solo detectar errores simples, ya sea en la ejecuci´on como en la revisi´on
de sintaxis. (MAX 5 pts)
3. Permite detectar errores de mayor dificultad, pero falla en instrucciones recursivas o
no detecta errores durante la ejecuci´on (MAX 15 pts)
4. Detecta todo tipo de error probado, siendo no solo errores simples de sintaxis, si no
que tambi´en errores de anidaci´on de comandos o secuencias incorrectas (MAX 20
pts)
Ejecuci´on de comandos (60 pts)
1. Ancho + Color de fondo 5 pts.
2. Izquierda + Derecha 10 pts.
3. Avanzar 10 pts.
4. Pintar color 15 pts.
5. Repetir veces 20 pts.
Se asignara puntaje parcial por funcionamiento parcialmente correcto.
5.2. Descuentos
Falta de comentarios (-10 pts c/u MAX 30 pts)
Falta de README (-20 pts)
Falta de alguna informaci´on obligatoria en el README (-5 pts c/u)
Falta de orden (entre -5 y -20 pts dependiendo de que tan desordenado)
D´ıa de atraso (-1 pt por cada hora de atraso)
Mal nombre en alg´un archivo entregado (-5 pts c/u)

Nombre: Martin Pino Cornejo
Rol: 202073528-k
Instrucciones: El archivo pixekart.py debe estar en la misma carpeta que codigos.txt
