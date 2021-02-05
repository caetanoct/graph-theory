from math import inf

class GrafoDicionario():

	# Inicializador
	def __init__(self, arquivo):
		self.E, self.V, self.E_set, self.E_tuple = self.ler(arquivo)
		self.n = len(self.V)
		self.m = len(self.E)
		self.m_set = len(self.E_set)
		self.m_tuple = len(self.E_tuple)
		self.grafo = {}
		self.grafo_dir = {}

		# Grafo não direcionado
		for v in range(self.n):
			self.grafo[v] = {}
		for u, v, w in self.E:
			self.grafo[v][u] = w

		# Grafo direcionado
		for v in range(self.n):
			self.grafo_dir[v] = {}
		for u, v, w in self.E_tuple:
			self.grafo_dir[u][v] = w

	# Representacao em string
	def __str__(self):
		formatado = []
		formatado.append(f'Grafo nao direcionado\n')
		formatado.append(f'Vertices: {self.qtd_vertices()}\n')
		formatado.append(f'Arestas: {self.qtd_arestas()}\n')
		i = 0
		for vertice, arestas in self.grafo.items():
			formatado.append(f'"{self.V[i]}" \t {vertice}: {arestas}\n')
			i += 1

		formatado.append(f'\nGrafo direcionado\n')
		formatado.append(f'Vertices: {self.qtd_vertices()}\n')
		formatado.append(f'Arestas: {self.m_tuple}\n')
		i = 0
		for vertice, arestas in self.grafo_dir.items():
			formatado.append(f'"{self.V[i]}" \t {vertice}: {arestas}\n')
			i += 1

		return "".join(formatado)

	# Retorna a quantidade de vertices
	def qtd_vertices(self):
		return self.n

	# Retorna a quantidade de arestas
	def qtd_arestas(self):
		return self.m

	# Retorna a quantidade de arestas da lista de sets
	def qtd_arestas_set(self):
		return self.m_set

	# Extra: Retorna a quantidade de arestas de direcao unica
	def qtd_arestas_uni(self):
		return self.m_uni

	# Retorna o grau do vertice v
	def grau(self, v):
		return len(self.grafo[v])

	# Retorna o rotulo do vertice v
	def rotulo(self, v):
		return self.V[v]

	# Retorna os vizinhos do vertice v
	def vizinhos(self, v):
		return self.grafo[v]

	# Retorna os vizinhos do vertice v do grafo dirigido
	def vizinhos_dir(self, v):
		return self.grafo_dir[v]

	# Se {u, v} pertence a E, retorna verdadeiro; se nao existir, retorna falso
	def haAresta(self, u, v):
		if self.grafo.get(u):
			if self.grafo.get(u).get(v):
				return True
		return False

	# Se {u, v} pertence a E, retorna o peso da aresta {u, v}; se nao existir, retorna um valor infinito positivo
	def peso(self, u, v):
		if self.haAresta(u, v):
			return self.grafo[u][v]
		else:
			return inf # math.inf

	# Deve carregar um grafo a partir de um arquivo no formato especicado aonal deste documento
	def ler(self, arquivo):
		V = []
		E = []
		E_set = []
		E_tuple = []
		with open(arquivo, 'r') as file:
			_, n = file.readline().split()

			for line in file: # Le os verices
				if line[0] == '*':
					break
				nome_dividido = (line.split())
				nome_completo = ' '.join(nome_dividido[1:])
				nome_completo_limpo = nome_completo[1:-1]
				V.append(nome_completo_limpo)

			for line in file: # Le as arestas
				u, v, w = line.split()
				u = int(u)
				v = int(v)
				w = float(w)
				E_set.append({u-1, v-1})
				E_tuple.append((u-1, v-1, w))
				E.append((u-1, v-1, w))
				E.append((v-1, u-1, w))

		return E, V, E_set, E_tuple

### Exemplo de entrada 'graph_test_dic.txt':
# *vertices 5
# 1 "João Luiz Ferreira"
# 2 "Renan Alfarth"
# 3 "Bruno Kartoffel"
# 4 "Carlos Crispim"
# 5 "Daniel Rodolfo"
# *edges
# 1 2 1.0
# 1 2 1.0
# 1 3 1.0
# 1 4 1.0
# 2 5 1.0
# 3 4 1.0

### grafo = GrafoDicionario('graph_test_dic.txt')

### print(grafo) (Desatualizado, agora possuímos 2 grafos internos)
# Vertices: 5
# Arestas: 5
# "JoÃ£o Luiz Ferreira"    0: {1: 1.0, 2: 1.0, 3: 1.0}
# "Renan Alfarth"          1: {0: 1.0, 4: 1.0}
# "Bruno Kartoffel"        2: {0: 1.0, 3: 1.0}
# "Carlos Crispim"         3: {0: 1.0, 2: 1.0}
# "Daniel Rodolfo"         4: {1: 1.0}

### print(grafo.qtd_vertices())
# 5

### print(grafo.qtd_arestas())
# 12

### print(grafo.grau(0))
# 3

### print(grafo.rotulo(0))
# JoÃ£o Luiz Ferreira

### print(grafo.vizinhos(0))
# {1: 1.0, 2: 1.0, 3: 1.0}

### print(grafo.haAresta(0, 1))
# True

### print(grafo.haAresta(0, 4))
# False

### print(grafo.peso(0, 1))
# 1.0

### print(grafo.peso(0, 4))
# inf
