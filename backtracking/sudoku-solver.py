#Funcion Auxiliar para Imprimir el Tablero de Sodoku de manera Legible:
def imprimir_tablero(tablero):
    #Iteramos por cada Fila del Tablero
    for i in range(len(tablero)):
        #Si la fila es divisible entre 3, imprimimos una linea para separar los cuadros
        if i % 3 == 0 and i != 0:
            print("------------------------")
        #Iteramos por cada columna de la fila
        for j in range(len(tablero[0])):
            #Si la columna es divisible entre 3, imprimimos un separador para delimitar la zona de 3x3
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            #S no encontramos en el ultimo elemento no imprimimos separador
            if j == 8:
                #Verificamos si el valor en el Arreglo es 0, si es asi imprimimos un espacio.
                if tablero[i][j] == 0:
                    print(" ")
                else:
                    print(tablero[i][j])
            #Si no nos encontramos en la ultima fila entonces imprimimos el valor con espacio
            else:
                #Si el valor es 0 imprimimos un espacio.
                if tablero[i][j] == 0:
                    print("  ",end="")
                else:
                    print(str(tablero[i][j]) + " ",end="")

#Funcion auxiliar que itera el tablero para ubicar el siguiente espacio vacio disponible (Casilla con valor 0)
#La funcion retorna la fila y columna del siguiente espacio vacio.
def siguiente_vacio(tablero): 
    #Iteramos en fila y columna del tablero
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:
                return fila, col
    # Si no existen espacios vacios en el tablero regresamos "None" (inexistente)
    return None, None

#Funcion Auxiliar que verifica que el intento cumpla con las reglas del Sudoku:
#   1) Mismo valor no presente en la fila
#   2) Mismo valor no presente en la columna
#   3) Mismo valor no presente en su tablero de 3x3
def movimiento_valido(tablero,intento,fila,col):
    #Verificamos si el valor se repite en la fila
    fila_actual = tablero[fila]
    #Si es asi regresamos falso, ya que es un movimiento invalido
    if intento in fila_actual:
        return False
    #Verificamos si el valor se repite en la columna
    columna_actual = [tablero[i][col] for i in range(9)]
    #Si es asi regresamos falso, ya que es un movimiento invalido
    if intento in columna_actual:
        return False

    #Verificamos el tablero de 3x3 Correspondiente
    #Utilizamos la division entera para que nos regrese valores base que multiplicados por 3 nos devolvera la fila/columna de la cual comenzar
    fila_inicio = (fila // 3) * 3
    col_inicio = (col // 3) * 3
    #Exploramos el tablero de 3x3 correspondiente buscando el valor.
    for f in range(fila_inicio, fila_inicio + 3):
        for c in range(col_inicio, col_inicio + 3):
            #Si es asi regresamos falso, ya que es un movimiento invalido
            if tablero[f][c] == intento:
                return False
    #Si todas las condiciones se cumplen regresamos True ya que es un movimiento valido.
    return True

# Funcion para resolver un Sudoku utilizando el algoritmo Backtracking
# Si existe una solucion para el tablero la funcion regresara True o False para caso contrario
# El tablero continuara mutando para almacenar la solucion final (si una solucion existe)
def resolver_sudoku(tablero):
    #Comenzamos ubicando el siguiente espacio vacio en el tablero
    fila, col = siguiente_vacio(tablero)
    #Si la funcion siguiente_vacio retorna None significa que el tablero ha sido completado y podemos retornar True
    #Si al contrario recibimos valores significa que debemos continuar iterando el tablero
    if fila is None:
        return True 
    #Probaremos cada posible valor del 1 al 9 en la casilla vacia
    for intento in range(1, 10):
        #Validamos que el valor en la casilla cumpla con las reglas del Sudoku
        if movimiento_valido(tablero, intento, fila, col):
            #Si es asi asignamos el valor a la casilla
            tablero[fila][col] = intento
            #Seguimos iterando el tablero recursivamente para encontrar una solucion
            if resolver_sudoku(tablero):
                #solucion ha sido encontrada.
                return True
        #si no hay solucion reiniciamos la casilla a 0 para probar otra solucion
        tablero[fila][col] = 0
    #Llegar a este punto de la funcion significa que el tablero no tiene solucion
    return False

#Metodo que procesa un archivo de entrada y resuelve cada sudoku que se encuentre.
def resolver_sudokus():
    with open("sudoku.txt") as f:
        linea = f.readline()
        if not linea:
            print("ERROR: Archivo de Entrada se encuentra Vacio")
        else:
            total_tableros = int(linea)
            for tablero_actual in range(total_tableros):
                tablero = []
                for i in range(9):
                    fila = f.readline().strip().split(",")
                    fila = [int(i) for i in fila]
                    tablero.append(fila)
                print("Tablero Sodoku", "------------------------", sep = "\n")
                imprimir_tablero(tablero)
                if resolver_sudoku(tablero):
                    print("***TABLERO TIENE SOLUCION***", "------------------------", sep = "\n")
                    imprimir_tablero(tablero)
                else:
                    print("***TABLERO NO TIENE SOLUCION***")

#Funcion Principal
if __name__ == '__main__':
    resolver_sudokus()