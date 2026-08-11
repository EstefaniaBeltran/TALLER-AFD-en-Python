# Autómatas Finitos Deterministas (AFD)

## Descripción

Este proyecto consiste en la implementación de un programa en Python para trabajar con Autómatas Finitos Deterministas (AFD).

El programa recibe como parámetros un archivo de configuración y un archivo que contiene las cadenas de prueba. A partir de la configuración, construye la información necesaria del autómata y posteriormente procesa cada cadena para determinar si es aceptada o rechazada.

Se utiliza un solo programa `AFD.py` para realizar las pruebas de los cuatro ejercicios.

## Archivos del proyecto

El proyecto está compuesto por los siguientes archivos:

- `AFD.py`: programa principal que lee la configuración y procesa las cadenas.
- `conf_a.txt`: configuración del ejercicio A.
- `conf_b.txt`: configuración del ejercicio B.
- `conf_c.txt`: configuración del ejercicio C.
- `conf_d.txt`: configuración del ejercicio D.
- `cadena_a.txt`: cadenas de prueba del ejercicio A.
- `cadena_b.txt`: cadenas de prueba del ejercicio B.
- `cadena_c.txt`: cadenas de prueba del ejercicio C.
- `cadena_d.txt`: cadenas de prueba del ejercicio D.

## Requisitos

Para ejecutar el programa se necesita:

- Python 3
- Terminal o consola de comandos

No se utilizan librerías externas.

## Ejecución

El programa recibe dos archivos como parámetros:

1. Archivo de configuración del AFD.
2. Archivo de cadenas que serán evaluadas.

### Ejercicio A

```bash
python3 AFD.py conf_a.txt cadena_a.txt
