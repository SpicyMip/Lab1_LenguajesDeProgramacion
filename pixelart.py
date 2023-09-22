import re, sys, numpy as np
from PIL import Image

def GenerarMatriz(ancho, fondo):
    '''
    Crea una matriz de ancho x ancho, la cual guarda los valores RBG del fondo.
        Parametros:
                ancho (int): Tamaño de la matriz cuadrada
                fondo (tupla de enteros):  Contiene el codigo RGB que representa al color de fondo
    '''
    if color[0]>255 or color[1]>255 or color[2]>255 or color[0]<0 or color[1]<0 or color[2]<0:
        sys.exit("El color esta fuera de los parametros RGB: ("+str(color[0])+str(color[1])+str(color[2])+")")
    if ancho<1:
        sys.exit("La matriz no puede tener ancho menor a 1") 
    matriz=[]
    for i in range(ancho):
        matriz.append([])
        for j in range(ancho):
            matriz[i].append(fondo)
    return matriz

def MatrizAImagen(matriz, filename='pixelart.png', factor=10):
    '''
    Convierte una matriz de valores RGB en una imagen y la guarda como un archivo png.
    Las imagenes son escaladas por un factor ya que con los ejemplos se producirian imagenes muy pequeñas.
        Parametros:
                matriz (lista de lista de tuplas de enteros): Matriz que representa la imagen en rgb.
                filename (str): Nombre del archivo en que se guardara la imagen.
                factor (int): Factor por el cual se escala el tamaño de las imagenes.
    '''
    matriz = np.array(matriz, dtype=np.uint8)
    np.swapaxes(matriz, 0, -1)

    N = np.shape(matriz)[0]

    img = Image.fromarray(matriz, 'RGB')
    img = img.resize((N*10, N*10), Image.Resampling.BOX)
    img.save(filename)

def PintarPixel(matriz, color, pos):
    '''
    Cambia el valor RGB de la posicion pos[0],pos[1] por el color dado en la matriz
        Parametros:
            matriz (lista de lista de tuplas de enteros): Matriz antes de pintar
            color (tupla de enteros): Color del cual se pintara en la posicion de la matriz
            pos (lista de enteros): Lista que contiene la posicion actual
        Retornos:
            matriz (lista de lista de tuplas de enteros): Matriz Resultante luego de pintar
    '''
    if color[0]>255 or color[1]>255 or color[2]>255 or color[0]<0 or color[1]<0 or color[2]<0:
        sys.exit("El color esta fuera de los parametros RGB: ("+str(color[0])+str(color[1])+str(color[2])+")")
    matriz[pos[0]][pos[1]]=color
    return matriz

def Derecha(pos):
    '''
    Cambia el valor de pos[3], que equivale la direccion para luego avanzar
        Parametros:
            pos (lista de enteros): Contiene la poscicion actual y la direccion donde se esta apuntando
        Retornos:
            pos (lista de enteros): Contiene la poscicion actual y la direccion donde se esta apuntando
    '''
    pos[2]=(pos[2]+1)%4
    return pos

def Izquierda(pos):
    '''
    Cambia el valor de pos[3], que equivale la direccion para luego avanzar
        Parametros:
            pos (lista de enteros): Contiene la poscicion actual y la direccion donde se esta apuntando
        Retornos:
            pos (lista de enteros): Contiene la poscicion actual y la direccion donde se esta apuntando
    '''
    pos[2]=(pos[2]+3)%4
    return pos

def Avanzar(pos, n):
    '''
    Suma o resta n a pos[0] o pos[1] dependiendo de la direccion de pos[3]
        Parametros:
            pos (lista de enteros): lista que tiene la posicion inicial y la direccion
            n (int): cantidad a sumar a la variable
        Retornos
            pos(lista de enteros): lista que tiene la posicion inicial y la direccion
    '''
    if pos[2]==0:
        pos[0]-=n
    elif pos[2]==1:
        pos[1]+=n
    elif pos[2]==2:
        pos[0]+=n
    else:
        pos[1]-=n
    if pos[0]<0 or pos[1]<0:
        sys.exit("La posicion consultada no existe: ("+str(pos[1])+str(pos[0])+")")
    return pos

def Procesar(codigo, matriz, pos, colores, error, i, codigo_backup):
    '''
    A partir de los tokens creados se analiza cada linea y se realizan los cambios pertinentes, en el caso de que el token sea el de repetir
    se hace un slide en el string y se llama recursivamente la funcion
        Parametros:
            codigo (str): String a analizar que contiene las instrucciones a realizar
            matriz (lista de listas de tuplas de enteros): Matriz RGB que se le haran cambios dependiendo de los tokens encontrados
            pos (lista de enteros): Posicion a efectuar cambios en la matriz
            colores (diccionario de strings con tuplas): Diccionario que contiene los colores junto sus valores RGB
            error (bool): Originalmente es False, pero si encuentra algun error de sintaxis se vuelve True
            i (int): indice de la lista
            codigo_backup (lista de strings): Lista con todas las instrucciones originales
        Retorno:
            error (bool): Retorna True si encuentra algun error de sintaxis
    '''
    flag=True
    while flag:
        if codigo!="":
            izquierda_1=re.compile(r'^Izquierda ').findall(codigo)
            derecha_1=re.compile(r'^Derecha ').findall(codigo)
            avanzar_1=re.compile(r'^Avanzar \d+ |^Avanzar ').findall(codigo)
            pintar_1=re.compile(r'^Pintar Rojo |^Pintar Verde |^Pintar Azul |^Pintar Negro |^Pintar Blanco |^Pintar RGB\(\d+,\d+,\d+\) ').findall(codigo)
            repetir_1=re.compile(r'^Repetir \d+ veces \{.+\} ').findall(codigo)
            if izquierda_1:
                pos=Izquierda(pos)
                codigo=codigo[(re.compile(r'^Izquierda ').search(codigo).span())[1]:]
            elif derecha_1:
                pos=Derecha(pos)
                codigo=codigo[(re.compile(r'^Derecha ').search(codigo).span())[1]:]
            elif avanzar_1:
                n=1
                match=re.compile(r"\d+ ").findall(avanzar_1[0])
                if match:
                    n=int(match[0])
                    codigo=codigo[(re.compile(r'^Avanzar \d+ ').search(codigo).span())[1]:]
                else:
                    codigo=codigo[(re.compile(r'^Avanzar ').search(codigo).span())[1]:]
                pos=Avanzar(pos, n)
            elif pintar_1:
                color=re.compile(r'Rojo|Verde|Azul|Negro|Blanco|RGB\(\d+,\d+,\d+\) ').findall(pintar_1[0])[0]
                if color not in colores:
                    color=re.compile(r"\d+").findall(color)
                    color=(int(color[0]),int(color[1]),int(color[2]))
                else:
                    color=colores[color]   
                matriz=PintarPixel(matriz, color, pos)
                codigo=codigo[(re.compile(r'^Pintar Rojo |^Pintar Verde |^Pintar Azul |^Pintar Negro |^Pintar Blanco |^Pintar RGB\(\d+,\d+,\d+\) ').search(codigo).span())[1]:]
            elif repetir_1:
                n=int(re.compile(r'\d+').findall(repetir_1[0])[0])
                matches=re.compile(r'}').finditer(codigo)
                for match in matches:
                    l=match.span()
                codigo_1=codigo[(re.compile(r'^Repetir \d+ veces \{\s*').search(codigo).span())[1]:l[0]]
                for i in range(n):
                    Procesar(codigo_1, matriz, pos, colores, error, i, codigo_backup)
                codigo=codigo[(re.compile(r'^Repetir \d+ veces \{.+\} ').search(codigo).span())[1]:]
            else:
                error=True
                flag=False
                errores.write(str(i+4)+" "+codigo_backup[i+3]+"\n")
        else:
            flag=False
    return error
def Repetir(codigo):
    '''
    Se revisa el token de repetir, si lo encuentra, ve si estan todas las instrucciones en la misma linea
    si no es asi buscará hasta encontrarlas, las sumara a la misma linea y eliminara de la lista los componentes sumados
        Parametros:
            codigo (listas de strings): Lista de string que contiene cada linea de texto en un lugar de la lista
        Retornos:
            codigo (listas de strings): Lista de string ya cambiados
    '''
    x=re.compile(r'^Repetir \d+ veces \{')
    eliminar=[]
    for i in range(len(codigo)):
        match=x.findall(codigo[i])
        if match:
            abierto=re.compile(r'{').findall(codigo[i]).count("{")
            cerrado=re.compile(r'}').findall(codigo[i]).count("}")
            if abierto!=cerrado:
                j=i
                while codigo[j]!='} ':
                    codigo[i]+=codigo[j+1]
                    eliminar.append(j+1)
                    j+=1
    eliminar.reverse()
    for i in eliminar:
        codigo.pop(i)
    return codigo

posicion=[0,0,1]
colores={"Rojo": (255, 0,0), "Verde":(0,255,0),"Azul":(0,0,255),"Negro":(0,0,0),"Blanco":(255,255,255)}
texto=open("codigos.txt", "r")
errores=open("errores.txt", "w")
codigo=[]
codigo_backup=[]
error=False
for linea in texto:
    codigo.append(linea.strip()+" ")
    codigo_backup.append(linea.strip()+" ")
texto.close()

#inicio
inicio=re.compile(r'^Ancho \d+ $')
matches=inicio.findall(codigo[0])
if matches:
    ancho=int(re.compile(r'\d+').findall(codigo[0])[0])
else:
    errores.write("1 "+codigo[0])
    error=True

#color fondo
color=re.compile(r"^Color de fondo Rojo |^Color de fondo Verde |^Color de fondo Azul |^Color de fondo Negro |^Color de fondo Blanco |^Color de fondo RGB\(\d+,\d+,\d+\) |")
matches=color.findall(codigo[1])
if matches:
    color=re.compile(r'Rojo|Verde|Azul|Negro|Blanco|RGB\(\d+,\d+,\d+\) ').findall(codigo[1])
    if color:
        color=color[0]
        if color not in colores:
            color=re.compile(r"\d+").findall(color)
            color=(int(color[0]),int(color[1]),int(color[2]))
        else:
            color=colores[color]  
    else:
        error=True
        errores.write("2"+codigo[1])
else:
    error=True
    errores.write("2 "+codigo[1])
if codigo[2]==' ':
    matriz=GenerarMatriz(ancho, color)
else:
    error=True
    errores.write()
codigo=Repetir(codigo[3:])
for i in range(len(codigo)):
    error=Procesar(codigo[i],matriz, posicion, colores, error, i, codigo_backup)
if not error:
    MatrizAImagen(matriz)
    print(matriz)
    errores.write("No hay errores!")
errores.close()