# Busca em largura
from grafo_dicionario import GrafoDicionario
from math import inf

# Le o nome do aqruivo e a posicao do vertice inicial
arquivo = input('Nome do arquivo: ')
posicao_inicial = int(input('Posicao do vertice inicial: '))

# Cria o grafo
grafo = GrafoDicionario(arquivo)
s = posicao_inicial - 1

# Inicializacao
C = [False for _ in range(grafo.qtd_vertices())]
D = [inf for _ in range(grafo.qtd_vertices())]
A = [None for _ in range(grafo.qtd_vertices())]
C[s] = True
D[s] = 0
Q = []
Q.append(s)

# Busca em largura
i = 0
while Q:
    u = Q.pop(0)
    for v in grafo.vizinhos(u).keys():
        if C[v] == False:
            C[v] = True
            D[v] = D[u] + 1
            A[v] = u
            Q.append(v)

# D_aux é uma lista de tuplas no formato, por exemplo,
# [(0, 2), (1, 3), (2, 3), (3, 1), (4, 4), (5, 3), (6, 2), (7, 0)]
# onde o primeiro elemento da tupla é o índice do vértice e o segundo
# elemento é a distância do vértice para o vértice s (vértice inicial)
D_aux = []
for i in range(len(D)):
    D_aux.append((i, D[i]))

# D_aux é ordenado pelo segundo elemento da tupla, agora temos:
# [(7, 0), (3, 1), (0, 2), (6, 2), (1, 3), (2, 3), (5, 3), (4, 4)]
D_aux = sorted(D_aux, key=lambda x: x[1])
inicio_D_aux = D_aux.pop(0)


# Printa as vértices encontrados em cada camada
camada = 1
prev = -inf
print(f'\n0: {inicio_D_aux[0]+1}', end='')
for vertice in D_aux:
    if vertice[1] > prev:
        print(f'\n{camada}:', end=' ')
        prev = vertice[1]
        camada += 1
    print(vertice[0]+1, end=' ')
