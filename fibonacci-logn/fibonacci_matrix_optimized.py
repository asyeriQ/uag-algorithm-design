def calcular_fib(n):
    # Definir Constante Matricial
    F = [[0, 1], [1, 1]]
    #0th Fibonacci es siempre 0
    if(n==0):
        return 0;
    # Al elevar F^(n-1) obtendremos el N-enesimo numero de la Serie dado que la matriz contrendra Fn+1 en sus valores.
    elevar_matriz_opt(F,n-1)
    # Al terminar de elevar F^(n-1) el Elemento F[2,2] representa el estado de Fn+1
    return F[1][1]

def elevar_matriz_opt(F, n):
    # Dado que F0 y F1 se encuentran directamente en la Contante matricial no hay necesidad de realizar la operacion.
    if(n == 0 or n == 1):
        return
    # Definir constante Matricial
    M = [[1, 1],[1, 0]]
    # Sin importar que n sea par o Impar el resultado de (n//2) Nos regresara el valor piso de la division
    elevar_matriz_opt(F, n // 2)
    # Obtenemos el valor de F^2 necesario para el producto de la potencia.
    producto_matriz(F, F)
    # Si el modulo de n/2 es diferente a Cero significa que n es impar por lo que tendremos que multiplicar el estado actual
    # de F por la constante Matricial (en este caso definida como M)
    if (n % 2 != 0):
        producto_matriz(F, M)

def producto_matriz(F, M):
    #Determinar cada valor de la multiplicacion matricial
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])
    #Asignar resultados a F
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


if __name__ == "__main__":
    n = int(input("Introduce el n-esimo numero de Fibonacci que quieras visualizar: "))
    print("El n-enesimo numero de Fibonacci es: ",calcular_fib(n))