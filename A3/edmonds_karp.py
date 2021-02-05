import sys, queue, math
from grafo_matriz_dir import GrafoMatriz
# a rede residual mapeia os fluxos - grafo Gf (V,Af,Cf) ; Af = arcos da rede ; Cf = residuo/capacidade residual -> se existe em A = c-f senao f
# Cf((u,v)) =  C((u,v)) - f((u,v)) se u,v pertence aos arcos de G
# Cf((u,v)) = f((u,v)) se (u,v) nao pertence a A
# para todo (u,v) pertencente a A, existem (u,v) pertencente a Af e (v,u) pertencente a Af
# s = vertice fonte ; t = vertice sorvedouro; Gf = rede residual
def edmonds_karp(G,s,t,Gf):
	#fluxos = [[0 for i in range(G.qtd_vertices())] for j in range(G.qtd_vertices())]	
	capacidades = []
	caminho = busca_edmonds_karp(G,s,t,Gf)	
	while caminho != None:		
		capacidadecaminho = capacidade_caminho(caminho,G)		
		capacidades.append(capacidadecaminho)
		#print(Gf)	
		#para cada arco no caminho Gf u,v aumenta e Gf v,u diminui
		for i in range(len(caminho)):
			if i+1 == len(caminho):
				break
			else:
				u = caminho[i]
				v = caminho[i+1]				
				Gf.grafo[u][v] = Gf.grafo[u][v] - capacidadecaminho
				Gf.grafo[v][u] = Gf.grafo[v][u] + capacidadecaminho		
		#print(Gf)
		caminho = busca_edmonds_karp(G,s,t,Gf)
	print(sum(capacidades))

def busca_edmonds_karp(G,s,t,Gf):
	s = s - 1
	t = t - 1
	C = [False for x in range(G.qtd_vertices())]
	A = [None for x in range(G.qtd_vertices())]
	C[s] = True
	Q = queue.Queue()
	Q.put(s)
	while Q.empty() == False:		
		u = Q.get()	
		for v in G.vizinhos(u):			
			# nao visitado e cf > 0 cf = c(u,v) - f(u,v)
			if C[v] == False and Gf.grafo[u][v] > 0:
				C[v] = True
				A[v] = u
				#sorvedouro encontrado, cria caminho aumentante (caminho que respeita restricoes de fluxo)
				if v == t:					
					p = [t]
					w = t
					while w != s:
						w = A[w]
						p.insert(0,w)
					return p
				Q.put(v)
	return None

def capacidade_caminho(caminho, G):
	minimo = math.inf
	anterior =  caminho[0]
	for v in caminho:		
		if (v == caminho[0]):			
			pass
		else:			
			if G.grafo[anterior][v] <= minimo:
				minimo = G.grafo[anterior][v]
			anterior =  v
	return minimo
print("Modo de usar o script:\npython3 edmonds_karp.py {nome_arquivo_teste}")
G = GrafoMatriz.ler(str(sys.argv[1]))
print("\nGrafo:\n-=-=-=-=-=-")
print(G.grafo)
print("-=-=-=-=-=-\n")
Gf  = G
print("Valor do fluxo máximo:")
edmonds_karp(G,1,5,Gf)