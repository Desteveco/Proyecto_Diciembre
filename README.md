# Desteveco Spotify
## Indice

1. [Introducción](#introducción)
2. [Pequeña descripción del proyecto](#pequeña-descripción-del-proyecto)
3. [Pre-requisitos y dependencias](#pre-requisitos-y-dependencias)   
4. [Cómo se instala](#cómo-se-instala) 
5. [Cómo se usa](#instrucciones-de-uso) 
6. [Arquitectura de la aplicación](#arquitectura-de-la-aplicación)   
7. [Tecnologías utilizadas](#tecnologías-utilizadas)
8. [Posibles mejoras y dificultades](#dificultades-y-mejoras)
9. [Menciones Honoríficas](#menciones-honoríficas)

## Introducción 

Este proyecto es un proyecto realizado como metodo de evaluacion del primer trimestre de 1º DAM en la asignatura de Programacion

### Pequeña descripción del proyecto 

El proyecto consiste en la produccion de un codigo en python que reconozca y abra un archivo .xspf, aleatorice las canciones que haya en el y lo abra como una playlist en VLC. Para esto usaremos los recursos dados en clase y facilitados por nuestro profesor [David Gelpi](#)

## Manual

### Pre-requisitos y dependencias                                  
1. python 3.12
2. git 2.43
3. Vs code
4. pip 23.3.1
5. pytest 7.4.3
6. iniconfig 2.0.0
7. colorama 0.4.6
8. pluggy 1.3.0
9. somepackage 1.2.
10. setuptools 65.5.0
11. coverage   7.3.2 
12. packaging  23.2 

### Cómo se instala 

1. Posiciónate en la ubicación donde desees crear la aplicación:

```bash
$ cd C:\Users\nombredeusuario\Escritorio
```
2. Crea un nuevo directorio para la aplicacion:

```bash
$ mkdir DirectorioX
```

3. Cambia la ruta a la del directorio que acabas de crear

```bash
$ cd DirectorioX
```
4. Instala `python`, `pip3` y `git`:

Puedes usar este enlace oficial si no tienes `Python` (https://www.python.org/downloads/). Cuando lo tengas comprueba que te añadio tambien `pip` con el comando:

```bash
$ pip --version
```
En caso de que no lo tengas por defecto:

```bash
$ python -m pip install
```

Ahora instala `git` y comprueba que lo tienes:

```bash
$ pip install git
$ git --version
```

5. clona el proyecto en el directorio

```bash
$ git clone https://github.com/Desteveco/Proyecto_Diciembre.git
```

6. Instala las dependencias requeridas con anterioridad en [Pre-requisitos y dependencias](#pre-requisitos-y-dependencias):

## Instrucciones de uso

Lo primero sera asegurarnos de que tenemos la musica descargada en una carpeta. Seleccionamos la carpeta con la musica y creamos con vlc un archivo .xspf de la carpeta
- Desde el cmd:

1. Dirigete al direcotorio `Proyecto_Diciembre`

```bash
$ cd C:\.. ..\Proyecto_Diciembre
```

2. Ejecuta la app con `python3`

```bash
$ python3 app.py
```

3. Te pedirá la ruta de tu archivo xspf y en el caso de que no tengas el VLC en el directorio por defecto, tambien la ruta al VLC.

4. La app te devolverá mensajes en el caso de que alguna de tus canciones no tengan el formato establecido (`.mp3`)

## [Arquitectura de la aplicacion](./Diagrama_de_Componentes.jpg)

## Tecnologuías utilizadas

- Lenguaje de Programación:
* `Python`
* Librerías de `Python`:
+ random: Para la aleatorización del orden de las canciones.
+ Subprocess: Para abrir `VLC` y pasarle las rutas de las canciones.
+ os: Para comprobar las rutas y los archivos del sistema
- Manipulación de Archivos:
- Reproducción de Música:
* `VLC`: Reproductor multimedia.
* `XSPF` (XML Shareable Playlist Format): Formato de archivo utilizado para definir listas de reproducción.

## Dificultades y mejoras

1. `Conventional Commits`:

- Considero que necesitaba mas soltura a la hora de lanzarme a un proyecto con esta herramienta sin saber utilizarla bien y ha sido todo un desafio constante.

2. `Codigo en general`:

- Los nombres de las variables y el codigo son muy mejorables y esta a la espera de una segunda version en la que se unifiquen las variables entre distintos modulos para hacerlo mas manejable y y facilitar la comprension

3. `git`:

- Al igual que con los commits, necesito mas soltura con esta herramienta ya que entre versiones he perdido muchos commits, que estaba creando en otras ramas sin saberlo, y la forma de solucionarlo fue eliminando todas. Por esa razon no hay en este proyecto un desarrollo del modelo de ramas de git ni versionado, aunque si existia.


## Menciones Honorificas
- Referencias a todo aquel que influyó en la creacion del proyecto
1. [dfleta](https://github.com/dfleta/kata_tdd_pytest)
2. [Samuel H Altman y Elon Musk](https://openai.com/)
4. [programing5393](https://www.youtube.com/@programming5393)