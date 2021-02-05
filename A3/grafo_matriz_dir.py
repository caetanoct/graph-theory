class Vertice():

    # Inicializador
    def __init__(self, data):
        pass

class GrafoMatriz():

    # Inicializador
    def __init__(self, V, E, w,we_array,rotulos_array):
        n = len(V)
        self.vertices=V
        self.edges=E
        self.funcaopeso=w
        self.rotulos=rotulos_array
        # aresta + peso => exemplo: (1,2,3) aresta de vertice 1 para 2 tem peso 3
        self.weighted_edges=we_array

        self.grafo = [[0 for x in range(n)] for x in range(n)]        
        if len(self.weighted_edges) > 0:
            for (u,v,w) in self.weighted_edges:
                self.grafo[u][v] = w
        else:
            for u, v in self.edges:
                self.grafo[u][v] = w(u, v)
                self.grafo[v][u] = w(u, v)

    def __str__(self):
        return str(self.grafo)

    # Retorna a quantidade de vertices
    def qtd_vertices(self):
        return len(self.grafo)

    # Retorna a quantidade de arestas
    def qtd_arestas(self):
        return len(self.edges)

    # Retorna o grau do vertice v
    def grau(self, v):
        grau = 0
        for x in self.grafo[v]:
            if (x>0):
                grau += 1
        return grau

    # Retorna o rotulo do vertice v
    def rotulo(self, v):
        return self.vertices[v]

    # Retorna os Indices dos vizinhos do vertice V
    def vizinhos(self,v):
        vizinhos=[]
        iterador=0
        for x in self.grafo[v]:
            if x>0:
                vizinhos.append(iterador)
            iterador+=1
        return vizinhos

    # Se {u, v} pertence a E, retorna verdadeiro; se nao existir, retorna falso
    def haAresta(self, u, v):
        return (u,v) in self.edges


    # Se {u, v} pertence a E, retorna o peso da aresta {u, v}; se nao existir, retorna um valor infinito positivo
    def peso(self, u, v):
        if (u,v) or (v,u) in E:
            if (self.grafo[u][v] == 0):
                return float('inf')
            return self.grafo[u][v]

    # Deve carregar um grafo a partir de um arquivo no formato especicado aonal deste documento
    def ler(file_name):
        file = open(file_name, 'r')
        linhas = file.readlines()
        linhas_novas = []
        for linha in linhas:
            if(linha[-1]=="\n"):
                linhas_novas.append(linha[:-1])
        linhas = linhas_novas

        pattern1 = "*vertices"
        pattern2 = "*arcs"

        read_vertices=False
        read_edges=False

        vertices_i=[]
        rotulos_i=[]
        edges_i=[]
        weighted_edges_i=[]

        for linha in linhas:
            if read_vertices:
            	if not (pattern2 in linha):
                    array_vr = linha.split()
                    vertices_i.append(int(array_vr[0])-1)                    
                    rotulos_i.append(array_vr[1])
            if read_edges:
                array_uvw = linha.split()
                tupla = (int(array_uvw[0])-1,int(array_uvw[1])-1)
                tupla_3 = (int(array_uvw[0])-1,int(array_uvw[1])-1,float(array_uvw[2]))
                edges_i.append(tupla)
                weighted_edges_i.append(tupla_3)
            if pattern1 in linha:
                read_vertices=True
            if pattern2 in linha:
                read_vertices=False
                read_edges=True

        return GrafoMatriz(vertices_i,edges_i,peso,weighted_edges_i,rotulos_i)

# Funcao arbitraria para o peso das arestas
def peso(v, u):
    return v + u

if __name__ == '__main__':
    #Rotulos dos vertices
    Va = ['A', 'B', 'C', 'D']
    Ea = [(0, 1), (0, 3), (1, 3), (2, 3)]
    wa = peso
    G = GrafoMatriz.ler('graph_test.txt')
    print(f'Grafo: {G}')
    print(f'Quantidade de vertices: {G.qtd_vertices()}')
    print(f'Quantidade de arestas: {G.qtd_arestas()}')

    #testa gray de todos vertices
    for x in range(len(G.vertices)):
        print(f'Grau de V={x}: {G.grau(x)}')
    #testa rotulo de todos vertices
    for x in range(len(G.vertices)):
        print(f'rótulo de V={x}: {G.rotulo(x)}')
    #testa vizinhos de todos vertices
    for x in range(len(G.vertices)):
        print(f'Vizinhos de V={x}: {G.vizinhos(x)}')
    #testa todas arestas
    for x in range(len(G.vertices)):
        for y in range(len(G.vertices)):
            print(f'Existe aresta ({x},{y})?: {G.haAresta(x,y)}')

    #testa todas arestas
    for x in range(len(G.vertices)):
        for y in range(len(G.vertices)):
            print(f'peso aresta ({x},{y})?: {G.peso(x,y)}')
