
# Autómatas Finitos Deterministas (AFD)
Yeimy Estefanía Beltrán Sandoval - Camilo Andrés Bernal Bernal - Yeisson Stiven Rincón Cubillos

## Descripción

En este trabajo se implementa un programa en Python para configurar y probar Autómatas Finitos Deterministas (AFD).

El programa `AFD.py` recibe como parámetros un archivo de configuración y un archivo de cadenas. A partir de la información de configuración, procesa cada cadena y determina si es aceptada o rechazada por el autómata correspondiente.

Se utiliza un solo programa `AFD.py` para los cuatro ejercicios.

## Organización del proyecto

El trabajo está organizado en cuatro carpetas, una para cada ejercicio:

### PUNTO A

Contiene:

- `conf_a.txt`: archivo de configuración del autómata.
- `cadena_a.txt`: archivo con las cadenas de prueba.
- `Diagrama_estados_a.png`: diagrama de estados.
- `definicion a.png`: definición del ejercicio.
- `resultado_a.png`: captura del resultado de la ejecución.

### PUNTO B

Contiene:

- `conf_b.txt`: archivo de configuración del autómata.
- `cadena_b.txt`: archivo con las cadenas de prueba.
- `Diagrama_estados_b.png`: diagrama de estados.
- `definicion b.png`: definición del ejercicio.
- `resultado_b.png`: captura del resultado de la ejecución.

### PUNTO C

Contiene:

- `conf_c.txt`: archivo de configuración del autómata.
- `cadena_c.txt`: archivo con las cadenas de prueba.
- `Diagrama_estados_c.png`: diagrama de estados.
- `definicion c.png`: definición del ejercicio.
- `resultado_c.png`: captura del resultado de la ejecución.

### PUNTO D

Contiene:

- `conf_d.txt`: archivo de configuración del autómata.
- `cadena_d.txt`: archivo con las cadenas de prueba.
- `Diagrama_estados_d.png`: diagrama de estados.
- `definicion d.png`: definición del ejercicio.
- `resultado_d.png`: captura del resultado de la ejecución.

## Requisitos

Para ejecutar el programa se necesita:

- Python 3
- Una terminal o consola de comandos.

No se utilizan librerías externas.

## Ejecución

El programa recibe dos archivos como parámetros:

1. El archivo de configuración del AFD.
2. El archivo que contiene las cadenas de prueba.

### Punto A

```bash
python3 adf.py conf_a.txt cadena_a.txt

```


### Punto B

```bash
python3 adf.py conf_b.txt cadena_b.txt

```

### Punto C

```bash
python3 adf.py conf_c.txt cadena_c.txt

```

### Punto D

```bash
python3 adf.py conf_d.txt cadena_d.txt

```

## Funcionamiento del programa

El programa realiza los siguientes pasos:

1. Recibe los archivos mediante la terminal.
2. Lee el archivo de configuración.
3. Obtiene los estados del autómata.
4. Obtiene el alfabeto.
5. Identifica el estado inicial.
6. Identifica los estados de aceptación.
7. Lee las transiciones.
8. Lee las cadenas de prueba.
9. Recorre cada cadena carácter por carácter.
10. Realiza las transiciones correspondientes entre estados.
11. Comprueba si la cadena termina en un estado de aceptación.
12. Muestra si la cadena fue `ACEPTADA` o `RECHAZADA`.

El programa también ignora las líneas que comienzan con `#`, utilizadas como comentarios en los archivos.

Las líneas vacías de los archivos de cadenas representan la cadena vacía (ε).

## Resultados

Las pruebas de cada uno de los ejercicios fueron realizadas desde la terminal.

### Punto A

![Resultado Punto A](PUNTO%20A/resultado_a.png)

### Punto B

![Resultado Punto B](PUNTO%20B/resultado_b.png)

### Punto C

![Resultado Punto C](PUNTO%20C/resultado_c.png)

### Punto D

![Resultado Punto D](PUNTO%20D/resultado_d.png)

## Conclusión

La implementación permite utilizar un mismo programa para configurar y evaluar diferentes Autómatas Finitos Deterministas mediante archivos de configuración y archivos de cadenas de prueba.

De esta manera, el programa puede determinar para cada cadena si esta es aceptada o rechazada de acuerdo con las transiciones y estados definidos para cada ejercicio.



