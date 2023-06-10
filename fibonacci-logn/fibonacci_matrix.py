def calcular_fib(n):
    # Definir Constante Matricial
    F = [[0, 1], [1, 1]]
    #0th Fibonacci es siempre 0
    if(n==0):
        return 0;
    # Al elevar F^(n-1) obtendremos el N-enesimo numero de la Serie dado que la matriz contrendra Fn+1 en sus valores.
    elevar_matriz(F,n-1)
    # Al terminar de elevar F^(n-1) el Elemento F[2,2] representa el estado de Fn+1
    return F[1][1]

def elevar_matriz(F, n):
    #Definir Constante Matricial
    M = [[0, 1], [1, 1]]
    #Realizar n-1 multiplicaciones para optimizar la multiplicacion matricial.
    for i in range(2, n + 1):
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
    #n = int(input("Introduce el n-esimo numero de Fibonacci que quieras visualizar: "))
    # print("El n-enesimo numero de Fibonacci es: ",calcular_fib(n))
    n = 80
    print (calcular_fib(n));