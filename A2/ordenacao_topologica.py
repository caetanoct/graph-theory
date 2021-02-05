# 2) Ordenação Topológica
from grafo_dicionario import GrafoDicionario

# Le o nome do aqruivo e a posicao do vertice inicial
# arquivo = input('Nome do arquivo: ')
arquivo = input('Nome do arquivo: ')

# Cria o grafo
grafo = GrafoDicionario(arquivo)

# Inicializacao


# Ordenação Topológica

# DFS
def dfs_visit_ot(v):
	C[v] = True
	for u in grafo.vizinhos_dir(v):
		if not C[u]:
			dfs_visit_ot(u)
	O.insert(0, v)

# DFS-Visit-OT
C = [False for _ in range(grafo.qtd_vertices())]
O = []
for u in grafo.grafo.keys():
	if not C[u]:
		dfs_visit_ot(u)

# Printando
for i in range(len(O)-1):
	print(f'{grafo.rotulo(O[i])} ->', end=' ')
print(f'{grafo.rotulo(O[i+1])}.')
