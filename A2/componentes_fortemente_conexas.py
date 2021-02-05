# 1) Componentes Fortemente Conexas
from grafo_dicionario import GrafoDicionario
from math import inf
from copy import deepcopy

# DFS
def dfs(G):
	C = [False for _ in range(G.qtd_vertices())]
	T = [inf for _ in range(G.qtd_vertices())]
	F = [inf for _ in range(G.qtd_vertices())]
	A = [None for _ in range(G.qtd_vertices())]
	tempo = 0
	for u in V:
		if not C[u]:
			tempo = dfs_visit(G, u, C, T, A, F, tempo)
	return C, T, A, F

# DFS-Visit
def dfs_visit(G, v, C, T, A, F, tempo):
	C[v] = True
	tempo += 1
	T[v] = tempo
	for u in G.vizinhos_dir(v):
		if not C[u]:
			A[u] = v
			tempo = dfs_visit(G, u, C, T, A, F, tempo)
	tempo += 1
	F[v] = tempo
	return tempo

# Le o nome do aqruivo e a posicao do vertice inicial
# arquivo = input('Nome do arquivo: ')
arquivo = input('Nome do arquivo: ')
G = GrafoDicionario(arquivo)

# Componentes Fortemente Conexas

# Tornando V global para evitar criar 2 métodos dfs
V = G.grafo.keys()

# Primeira busca
C, T, Al, F = dfs(G)

# Ordenando V, basead em F, para a segunda busca
# Ordenando por index
F = sorted(range(len(F)), key=lambda i: F[i])
F.reverse()
V = F

# Invertendo o grafo
# Baseado na implemntação do Grafo_Dicionario, precisamos alterar
# tanto E_tuple quanto grafo_dir (por conta do método de encontrar vizinhos)
E_tuple_t = []
for u, v, w in G.E_tuple:
	E_tuple_t.append((v, u, w))

G.E_tuple = E_tuple_t

for v in range(G.qtd_vertices()):
	G.grafo_dir[v] = {}
for u, v, w in G.E_tuple:
	G.grafo_dir[u][v] = w

# Segunda busca utilizando novo V e grafo invertido
C_t, T_t, Al_t, F_t = dfs(G)

# Construindo os componentes
componentes = []
for i in range(len(Al_t)):
	# Se for raiz
	if Al_t[i] == None:
		componente = []
		already_visited = {i}
		to_visit = {i}
		# Enquanto ainda temos vértices para visitar
		while to_visit:
			visited = to_visit.pop()
			componente.append(visited)
			for j in range(len(Al_t)):
				# Se o vértice antecessor for igual ao que precisamos visitar
				# e nós ainda não visitamos ele
				if Al_t[j] == visited and j not in already_visited:
					already_visited.add(j)
					to_visit.add(j)
		componentes.append(componente)

# Printando
for c in componentes:
	for i in range(len(c)-1):
		print(c[i]+1, end=',')
	print(c[-1]+1)
