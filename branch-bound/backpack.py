# Construimos una clase auxiliar que representara los atributos de un Objeto (Item) que se puede poner en la mochila
class Item:
    def __init__(self, valor, peso):
        self.peso = peso
        self.valor = valor
        self.costo = valor / peso

# Funcion que utiliza el metodo de Ramificacion y Poda para resolver el Problema de la Mochila
def resolver_mochila(items, capacidad):
    # Ordenamos nuestra lista en base al costo (funcion Heuristica) para determinar que objetos son mejor para colocar en nuestra mochila
    # Utilizamos una funcion Lambda para definir el comparador (Costo) y indicamos que queremos una lista ordenada de manera Descendiente
    items.sort(key=lambda x: x.costo, reverse=True)
    # Definimos n como el numero total de elementos
    n = len(items)
    # Inicializamos nuestra ganancia maxima
    ganancia_maxima = 0
    # Inicializamos una mascara de bit para representar la solucion de la mochila
    mascara_solucion = [0] * n

    # Funcion Interna que realizara el algoritmo de ramificacion y poda
    # Al finalizar el algoritmo las variables ganancia_maxima y solucion contendran los tanto el valor total de la mochila como la lista de objetos
    def rami_y_poda(indice_actual, peso_total, ganancia_actual):
        # Agregamos una referencia a nuestra variable de ganancia_maxima
        nonlocal ganancia_maxima
        #Verificamos si el peso actual excede nuestra capacidad maxima. Si es asi regresamos y excluimos la solucion.
        if peso_total > capacidad:
            return
        # Validamos si la exploracion ya recorrio la lista total de objetos.
        # Si es asi entonces verificaremos que la solucion sea mejor que la que tenemos guardada hasta el momento
        if indice_actual == n:
            # Si nuestra ganancia actual es mayor que la maxima significa que esta solucion es mejor y tenemos que "Almacenarla"
            if ganancia_actual > ganancia_maxima:
                # Actualizamos nuestra ganancia maxima
                ganancia_maxima = ganancia_actual
                # Inicializamos una mascara de bit para representar la solucion de la mochila
                mascara_solucion[:] = [0] * n
                # Iteramos la solucion y actualizamos la mascara en base a si el indice del elemento existe en la solucion.
                for i in range(n):
                    mascara_solucion[i] = 1 if items[i] in solucion else 0
            return
        # En caso de que no hayamos terminado de explorar solucion (rama), tendremos que verificar si el elemento actual puede agregarse o podarse.
        # Agregamos temporalmente nuestro objeto a la solucion.
        solucion.add(items[indice_actual])
        # Llamamos recursivamente al metodo pero con los nuevos valores de ganancia y peso para continuar explorando.
        rami_y_poda(indice_actual + 1, peso_total + items[indice_actual].peso, ganancia_actual + items[indice_actual].valor)
        # Eliminamos temporalmente nuestro objetos de la solucion para explorar la rama donde no se encuentra
        solucion.remove(items[indice_actual])
        # Llamamaos recursivamente al metodo pero con los values actuales de ganancia y peso para continuar explorando
        rami_y_poda(indice_actual + 1, peso_total, ganancia_actual)

    # Inicializamos nuestro conjunto que almacenara la solucion actual durante la exploracion
    solucion = set()
    # Comenzamos a ramificar y podar nuestro problema (indice_actual = 0, peso_total = 0, ganancia_actual = 0)
    rami_y_poda(0, 0, 0)
    # Al finalizar el algoritmo podremos agregar los objetos a nuestra lista (mochila_final) que se regresaran junto con la ganancia maxima
    mochila_final = [items[i] for i, item in enumerate(mascara_solucion) if item == 1]
    return mochila_final, ganancia_maxima

#Funcion Principal
if __name__ == '__main__':
    # Construimos nuestra lista de objetos (Valor, Peso)
    items = [
        Item(79, 85),
        Item(32, 26),
        Item(47, 48),
        Item(18, 21),
        Item(26, 22),
        Item(85, 95),
        Item(33, 43),
        Item(40, 45),
        Item(45, 55),
        Item(59, 52)
    ]
    capacidad_mochila = 101
    mochila, ganancia_maxima = resolver_mochila(items, capacidad_mochila)

    # Imprimimos la solucion del Problema
    print("Peso Maximo de la Mochila:", capacidad_mochila)
    print("Ganancia Maxima de la Mochila:", ganancia_maxima)
    print("Objetos en la Mochila:")
    for item in mochila:
        print("Peso:",item.peso,"Valor:", item.valor)