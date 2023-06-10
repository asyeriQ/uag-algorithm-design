#Metodo de Construccion de Grafo desde Archivo
def construir_grafo(imprimir_matriz = False):
    #Inicializando Matriz de Adyacencia vacia
    grafo = dict()
    #Abriendo archivo con definicion del Grafo
    with open('graph.txt') as f:
        linea = f.readline()
        if not linea:
            print("ERROR: Archivo de Definicion se encuentra Vacio")
        else:
            if linea.strip() == "Nodes:":
                linea_nodos = f.readline()
                #Obtengo lista de Nodos para inicializar el grafo.
                lista_nodos = linea_nodos.strip().split(", ")
                for nombre_nodo in lista_nodos:
                    #Inicializo cada nodo con su Lista de adjacencia (vecinos)
                    grafo[nombre_nodo] = []
                linea = f.readline()
                if linea.strip() == "Edges:":
                    #Continuamos leyendo el archivo para agregar cada vertice en la lista de adjacencia
                    while True:
                        linea_vertice = f.readline()
                        if not linea_vertice:
                            break
                        else:
                            vertice = linea_vertice.strip().split(", ")
                            #Como es un grafo no dirigido debemos de agregar la adjacencia de ambos lados
                            grafo[vertice[0]].append(vertice[1])
                            grafo[vertice[1]].append(vertice[0])
                else:
                    print("ERROR: Archivo de Definicion mal formado")
            else:
                print("ERROR: Archivo de Definicion mal formado")
    if imprimir_matriz:
        print("Lista de Adjacencia del Grafo Construido")
        for key in grafo.keys():
            print(key,": ",grafo[key])
    return grafo

#Metodo que realiza una Busqueda en Profundidad (DFS) en todos los nodos del Grafo
def dfsAll(grafo):
    #Inicializamos nuestro conjunto de nodos visitados
    nodos_visitados = set()
    print("Subgrafos Detectados utilizando Busqueda en Profundidad:")
    #Iteramos nodo por nodo de nuestra Lista de Adjacencia
    for nodo in grafo.keys():
        #Inicializamos nuestra lista traversal cada vez que exploramos un Nodo.
        lista_traversal = []
        #Verificamos si el nodo actual no fue ya visitado
        if (nodo not in nodos_visitados):
            #Si el nodo no fue visitado entonces comenzamos una Busqueda en Profundidad utilizando ese nodo como punto de partida.
            dfs(nodos_visitados,lista_traversal,grafo, nodo)
            print ("Subgrafo: ",lista_traversal)


#Algoritmo de Busqueda en Profundidad
def dfs(nodos_visitados,lista_traversal,grafo, nodo_actual):
    #Dado que este algoritmo utiliza recursidad es importante verificar que no hayamos visitado ya el nodo anteriormente
    if nodo_actual not in nodos_visitados:
        #Agregamos el nodo a nuestra lista traversal (o Camino) para definir el subgrafo
        lista_traversal.append(nodo_actual)
        #Agregamos el nodo a nuestro conjunto de nodos visitados para la recursividad
        nodos_visitados.add(nodo_actual)
        #Comenzamos a explorar los vecinos de nuestro nodo actual.
        for vecino in grafo[nodo_actual]:
            #Mediante recursividad repetimos el proceso para cada vecino del nodo.
            dfs(nodos_visitados, lista_traversal, grafo, vecino)

#Funcion Principal
if __name__ == "__main__":
    #Comenzamos construccion del Grafo (Imprimimos la lista de Adjacencia del Grafo)
    grafo = construir_grafo(True)
    #Comenzamos la exploracion del Grafo
    dfsAll(grafo)