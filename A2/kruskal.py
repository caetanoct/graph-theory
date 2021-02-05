import sys
from grafo_matriz import GrafoMatriz

#retorna lista de arestas ordenadas por ordem crescente de peso
def ordenar(edges_list):	
	ordem = []
	for (x,y,z) in edges_list:		
		ordem.append((x,y,z))		
	return sorted(ordem, key=lambda x: x[2])

def kruskal(grafomatriz):
	S = []
	A = set()
	E_ord = ordenar(grafomatriz.weighted_edges)		
	for i in range(grafomatriz.qtd_vertices()):
		S.append(set([i]))	
	for (u,v,z) in E_ord:
		if (S[u] != S[v]):						
			uv = frozenset([u,v])
			A.add(uv)
			x = S[u].union(S[v])
			for y in x:
				S[y] = x
	return A

def somapeso(arvore, grafo):
	soma = 0
	for (x,y) in arvore:
		soma += grafo.peso(x,y)
	return soma
print("Modo de usar o script:\npython3 kruskal.py {nome_arquivo_teste}")
print("para funcionar o arquivo de teste deve ter uma linha a mais no final do arquivo como no arquivo teste.net\n")
G = GrafoMatriz.ler(str(sys.argv[1]))
arvore = kruskal(G)

print(somapeso(arvore,G))
for (x,y) in arvore:
	print(f'{x+1}-{y+1}',end=' ')
print()
