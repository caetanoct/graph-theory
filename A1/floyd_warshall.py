import sys
from grafo_matriz import GrafoMatriz

#retorna matriz com menor custo de caminho
def floydwarshall(grafomatriz):
	n = grafomatriz.qtd_vertices()
	for i in range(n):
			for j in range(n):
				if (i != j):
					if(grafomatriz.grafo[i][j]==0):
						grafomatriz.grafo[i][j]=999999999999999
	#print(grafomatriz.grafo)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				grafomatriz.grafo[i][j] = min(grafomatriz.grafo[i][j], (grafomatriz.grafo[i][k]+grafomatriz.grafo[k][j]))
	return grafomatriz


print("Modo de usar o script:\npython3 floyd_warshall.py {nome_arquivo_teste}\n")

G = GrafoMatriz.ler(str(sys.argv[1]))

#print(f'Grafo Antes Algoritmo: {G}')
floydwarshall(G)
#print(f'Grafo Após Algoritmo: {G}')

for x in range(G.qtd_vertices()):
	print(f'{x+1}: ',end='')	
	for y in range(G.qtd_vertices()):		
		print(G.grafo[x][y],end=' ')		
	print()		