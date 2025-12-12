def count_by_lenght(text, l=None):
    # Dani Gonzalez
    """Return a dict with lengths and quantities of words with this lenghts"""
    palabras = text.split()
    diccionario ={}
    for p in palabras:
        longitud = len(p)
        if l is None or longitud == 1:
            diccionario[longitud] = diccionario.get(longitud, 0) + 1
    return diccionario

if __name__ == "__main__":
    print(count_by_lenght("Esto es una prueba xD"))