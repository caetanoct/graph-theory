# coding: utf-8
from grafo_dicionario import GrafoDicionario

#infinito
from math import inf

class Hop():

    def __init__(self,G):
        self.G = G
        self.Vertices = self.G.getVertices()
        self.numE = self.G.qtd_vertices()
        #numero de itens em X e Y
        self.x , self.y = self.G.get_xy()
        self.mate = [None] * self.numE
        self.D = [inf] * (self.numE+1)
        self.X = [] #vertices em X
        for i in range(self.x):
            self.X.append(self.Vertices[i])
        self.cont = 0

    def DFS(self,G,mate,x,D):
        if x != None:
            for y in list((G.vizinhos(x)).keys()):
                if mate[y] == None:
                    mate[y] = x
                    mate[x] = y
                    return True
                if D[mate[y]] == D[x] + 1:
                    if self.DFS(G,mate,mate[y],D):
                        mate[y] = x
                        mate[x] = y
                        return True
            D[x] = inf
            return False
        return True


    def BFS(self,G,mate,D):
        Q = []
        for x in self.X:
            #print(x)
            if mate[x] == None: #ele ainda nao é casado
                D[x] = 0
                Q.append(x)
            else:
                D[x] = inf
        
        D[self.numE] = inf

        while len(Q) > 0:
            vertice = Q.pop(0)
            if D[vertice] < D[self.numE]:
                for vertice2 in list((G.vizinhos(vertice)).keys()):
                    if (mate[vertice2] == None):
                        D[self.numE] = D[vertice] + 1
                    elif D[mate[vertice2]] == inf:
                        D[mate[vertice2]] = D[vertice] + 1
                        Q.append(mate[vertice2])
        return D[self.numE] != inf
    
    def retMatchs(self):
        mt = []
        for vt1,vt2 in zip(self.X,self.mate):
            #print("[",vt1,",",vt2,"]")
            mt.append([vt1,vt2])
        return mt


    def executar(self): # Parece OK
        m = 0
        while self.BFS(self.G,self.mate, self.D) == True:
            for x in self.X:
                if self.mate[x] == None:
                    if self.DFS(self.G,self.mate,x,self.D):
                        m = m + 1
        return m,self.retMatchs()



if __name__ == '__main__':
    
    #arquivo = input('Nome do arquivo: ')
    arquivo = "teste_hop2.txt"
    G = GrafoDicionario(arquivo,True)
    hop = Hop(G)
    nMatch, matchs = hop.executar()
    print("Numero de Matchs: ",nMatch)
    print("Matchs: ",matchs)