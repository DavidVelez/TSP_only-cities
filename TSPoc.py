#Solucion Travelling salesman problem(TSP)

#Autor: David Felipe Velez Cadavid.
#Fecha: 25 Mayo,2016

	
import sys
import copy

#Para comenzar la solucion del problema se debe de tener una matriz del tamano segun sea la necesidad, en este caso se tiene una matriz de 6x6.
#Esto significa que la matriz contiene 36 costos debido a que son los costos de ir de una ciudad al resto de ciudades, es decir el costo de
#ir de la ciudad 1 a la ciudad(1,2,3,4,5,6), ir de la ciudad 2 a la ciudad(1,2,3,4,5,6), y asi respectivamente con cada ciudad.


#Para los costos de la matriz se tiene una condicion, tal condicion trata de que la diagonal principal de la matriz debe contener solo ceros, porque por ejemplo ir de la ciudad 1 a la ciudad 1 tendra un costo de 0. 
matrix = [
        
		[0, 300, 700, 570, 420, 198 ],
		[450, 0, 800, 50, 530, 160  ],
		[230, 580, 0, 850, 255, 370 ],
		[560, 120, 356, 0, 480, 240 ],
		[311, 414, 250, 669, 0, 418 ],
		[800, 356, 700, 432, 234, 0 ]

	]


data = [1, 2, 3, 4, 5, 6]
"""
Proposito... 
1)crear la matriz
matrix = [

		[0, 2, 9, 10],
		[1, 0, 6, 4 ],
		[15, 7, 0, 8],
		[6, 3, 12, 0]
   	]

2)almacenar en data las ciudades
data = [1, 2, 3, 4]
"""

n = len(data) #Numero de elementos de la matriz almacenados en n.
all_sets = []
g = {}
p = []

#Funcion main: procesa el algoritmo principal, compara costos y almacena en matriz.
def main():
    for x in range(1, n):#Se crea un rango que ira de 1 a n, es decir el numero de elementos de la matriz.
        g[x + 1, ()] = matrix[x][0]

    get_minimum(1,(2,3,4,5,6))

    print('\n\nLa solucion optima para TSP es: \n\nciudad : 1') #Imprime la solucion optima final.
    #Se descartan costos.Mediante comparaciones...
    solution = p.pop()
    print'ciudad :',(solution[1][0])
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print"ciudad :",(solution[1][0])
                break
    print('ciudad : 1')
    return

#Funcion minimos: halla los valores minimos y se depositan en tuplas.
def get_minimum(k, a):
    if (k, a) in g:
        # Se tiene calculado g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a))
        values.append(matrix[k-1][j-1] + result)

    #Teniendo los valores minimos se encuentra una solucion optima.
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


if __name__ == '__main__':
    main()
    sys.exit(0)  

