# 📝 Analizador de Texto Básico

Text Analyzer es una herramienta sencilla escrita en Python que permite obtener métricas básicas sobre cualquier texto introducido por el usuario. El proyecto se centra en el procesamiento elemental de cadenas y en el uso de listas, sets y diccionarios para extraer información relevante.

Este proyecto está pensado como un ejemplo práctico para quienes comienzan a trabajar con manipulación de texto y estructuras de datos en Python.

## ✨ Características principales

A partir de un texto introducido por el usuario, el analizador genera las siguientes métricas:

### ✔️ Lista de palabras

El texto se divide en palabras mediante un proceso simple de tokenización.
Esta lista conserva el orden original y contiene todas las palabras, incluidas las repetidas.

### ✔️ Conjunto de palabras únicas

A partir de la lista generada, se crea un set que incluye únicamente una ocurrencia de cada palabra.
Esto permite identificar el vocabulario único utilizado en el texto.

### ✔️ Diccionario de frecuencias

El sistema genera un diccionario donde:

Clave: palabra

Valor: número de apariciones

Esto permite analizar la distribución del lenguaje, identificar los términos más usados y detectar patrones.

### ✔️ Palabra más larga y más corta

El analizador calcula:

La palabra con mayor longitud

La palabra con menor longitud

Ambas se devuelven como una tupla:

(larga, corta)


Estas métricas son útiles para estudiar la variabilidad léxica y la composición del texto.

### 📈 Métricas generadas

Además de las estructuras anteriores, el proyecto puede mostrar:

Número total de palabras

Número total de palabras únicas

Longitud media de las palabras

Top 5 palabras más frecuentes

Relación entre palabras repetidas y únicas

(Estas métricas forman parte del diseño del proyecto y pueden extenderse fácilmente.)

### 🚀 Ejecución del programa

El usuario simplemente ejecuta el script y proporciona el texto cuando se le solicita.
El programa devolverá en pantalla todas las métricas organizadas de forma clara.

### 🔧 Tecnologías utilizadas

Python 3.x

Estructuras estándar: list, set, dict, tuple

No requiere dependencias externas

### 📦 Objetivo del proyecto

El propósito de Text Analyzer es servir como una herramienta educativa y a la vez un ejemplo concreto de cómo procesar texto y trabajar con distintas estructuras de datos en Python.
Es ligero, fácil de extender y perfecto para proyectos introductorios de análisis textual.