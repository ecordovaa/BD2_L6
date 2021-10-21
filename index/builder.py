# Crea el índice invertido en memoria secundaria
def build_index():
    load = {}
    
    # Itera por cada libro
    for book_id in range(6):
        with open("preprocesamiento/preprocesados/" + str(book_id + 1) + ".txt", 'r') as book:
            temp = {} # No queremos escribir mas de una vez una palabra

            # Lee linea por linea (palabra por palabra)
            for term in book.read().split('\n'):
                if term not in temp:        # O(1) por implementacion de dict
                    if term not in load:    # O(1) por implementacion de dict
                        # Este es el primer libro donde aparece la palabra
                        load[term] = ((book_id + 1),)
                    else:
                        # Añadimos este libro a la lista de ocurrencias de la palabra
                        new_tuple = list(load[term])
                        new_tuple.append(book_id + 1)
                        load[term] = tuple(new_tuple)
                temp[term] = True

    #Sorting
    keys = sorted(load.items(), key=lambda x: len(x[1]), reverse=True)
    keys = keys[:501]   # Recortamos elementos en casos de excedernos en palabras
    keys.sort(key=lambda x: x[0])

    #Escritura
    with open("index/inverted_index.txt", 'w') as index:
        for value in keys[1:]:
            index.write(value[0] + ':')
            books = ''
            for book in value[1]:
                books += str(book) + ','
            index.write(books[:-1] + '\n')