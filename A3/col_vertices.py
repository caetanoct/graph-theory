# coding: utf-8
from grafo_dicionario import GrafoDicionario

#infinito
from math import inf


class Lawler():
    
    def __init__(self,G):
        self.G = G
        self.v = self.G.qtd_vertices()
        self.i = (2 ** self.G.qtd_vertices())
        self.X = [inf] * self.i
        self.X[0] = 0
        self.powersets = self.get_subconjuntos(self.G.getVertices())

    def get_subconjuntos(self,s):
        power_set=[[]]
        for elem in s:
            for sub_set in power_set:
                power_set=power_set+[list(sub_set)+[elem]]
        return power_set

    def subGrafo(self,Pset):
        arestas = []
        arestas_set = []
        for vertice in Pset:
            vizinhos = list((self.G.vizinhos(vertice)).keys())
            for vizinho in vizinhos:
                if vizinho in Pset:
                    arestas.append((int(vertice), int(vizinho), float(0.0)))
                    arestas_set.append({int(vertice), int(vizinho)})
        subG = GrafoDicionario(None,False,Pset,arestas,arestas_set)
        #print(subG)
        return subG

    def independentesMaximais(self,subG):
        #se dois vértices quaisquer de S nunca são adjacentes entre si.
        listaIndependentes = []
        adds = []

        vertices = subG.getVertices()
        #print(vertices)

        #testar para ver se tem apenas um vertice
        if len(vertices) > 1:
            for vertice in vertices:
                vizinhos = list((subG.vizinhos(vertice)).keys())
                for v in vertices:
                    if (v not in vizinhos) and (v != vertice):
                        if ([v,vertice] not in listaIndependentes) and (v not in adds):
                            adds.append(v)
                            adds.append(vertice)
                            listaIndependentes.append([vertice,v])
                    if (v in vizinhos) and (v != vertice):
                        if ([v] not in listaIndependentes) and (v not in adds):
                            adds.append(v)
                            listaIndependentes.append([v])
        else:
            #retornar somente um conjunto
            for v in vertices:
                listaIndependentes.append([v])
        
        return listaIndependentes

    def printTab(self):
        print(f'|{"S":^15}|{"X":^15}|')
        for subset, x in zip(self.powersets,self.X):
            print('|{:^15}|{:^15}|'.format("["+','.join(map(str, subset))+"]",x))

    def consultaTab(self,conj):
        for linha,valor in zip(self.powersets,self.X):
            if conj == linha:
                return valor

    def preencheTab(self,conj,val):
        for linha, i in zip(self.powersets,range(self.i)):
            if conj == linha:
                self.X[i] = val
                break
    
    def retIDlista(self,lista,valor):
        for i, v in zip(range(len(lista)),lista):
            if valor == v:
                return i
        return None

    def executar(self):
        indMax = []
        for pset in self.powersets:
            Glin = self.subGrafo(pset)
        #    Glin = self.subGrafo(self.powersets[31])
            #print(Glin)
            vertices = Glin.getVertices()
            conjuntos = self.independentesMaximais(Glin)
            indMax = conjuntos
            #self.printTab()
            if len(conjuntos) > 0:
                #print(conjuntos)
                for conjunto in conjuntos:
                    #print(conjunto)
                    ids = []
                    cVertices = vertices.copy()
                    #subtraio do meu Glin o conjunto atual
                    for c in conjunto:
                        cVertices.pop(self.retIDlista(cVertices,c))
                    cVertices.sort()
                    #busco o valor do que sobrou na tabela e somo +1 e salvo para ver se algum conjunto consegue menor valor
                    val = self.consultaTab(cVertices) + 1
                    valAtual = self.consultaTab(vertices)
                    if val < valAtual:
                        self.preencheTab(vertices,val)   
        self.printTab()
        return self.X[self.i-1]


if __name__ == '__main__':
    
    arquivo = input('Nome do arquivo: ')
    grafo = Lawler(GrafoDicionario(arquivo,True))
    cores = grafo.executar()
    print("Minimo necessário de cores: ",cores)