# coding: utf-8
from grafo_dicionario import GrafoDicionario

#infinito
Max = 99999

class tabelaDj():
    def __init__(self,G,vInicial):
        self.G = G
        self.inicio = vInicial
        self.tabela = self.init_tabela(self.G.qtd_vertices())
        self.setDistancia(0,self.inicio-1)


    # Representacao em string
    def __str__(self):
        formatado = []
        formatado.append(f'| V\t| D\t| A\t| C\t|\n')
        i = 0
        for D,A,C in self.tabela:
            formatado.append(f'| {self.G.V[i]}\t| {D}\t| {A}\t| {C}\t|\n')
            i = i + 1
        return "".join(formatado)

    def init_tabela(self,qV):
        tabela = []
        for vertice in range(qV):
            tabela.append([Max,None,False])
        return tabela

    def setDistancia(self,d,v):
        self.tabela[v][0] = d

    def getDistancia(self,v):
        return self.tabela[v][0]

    def setAncestral(self,a,v):
        self.tabela[v][1] = a

    def getAncestral(self,v):
        return self.tabela[v][1]

    def setVisitado(self,v):
        self.tabela[v][2] = True

    def nVisitados(self):
        for D,A,C in self.tabela:
            if C == False:
                return False
        return True

    def getNotVisited(self):
        vertice = [None,Max]
        for i in range(len(self.tabela)):
            if self.tabela[i][2] == False:
                if vertice[1] > self.tabela[i][0]:
                    vertice[1] = self.tabela[i][0]
                    vertice[0] = i
        return vertice[0]

    def Result(self):
        i = 0
        formatado = []
        for D,A,C in self.tabela:
            caminho = []
            ancestral = A
            while(ancestral != None):
                caminho.append(str(ancestral))
                ancestral = self.getAncestral(ancestral-1)
            caminho.reverse()
            caminho.append(str(i+1))
            caminhoFinal = ",".join(caminho)
            formatado.append(f'{self.G.V[i]}: {caminhoFinal}; d={D}\n')
            i = i + 1
        return "".join(formatado)

def djikstra(arquivo,s):

    # Inicialização
    G = GrafoDicionario(arquivo)
    Tab = tabelaDj(G,s)
    while not Tab.nVisitados():
        #selecionar um vertice nao visitado que tenha o menor D
        u = Tab.getNotVisited()
        Tab.setVisitado(u)
        #loop para cada vertice vizinho de u nao visitado
        for vizinho in G.vizinhos(u):
            distAtual = Tab.getDistancia(u)+G.grafo[u][vizinho]
            if Tab.getDistancia(vizinho) > distAtual:
                Tab.setDistancia(distAtual,vizinho)
                Tab.setAncestral(u+1,vizinho)
    #print(Tab)
    return Tab.Result()


if __name__ == '__main__':
    arquivo = input('Nome do arquivo: ')
    posicao_inicial = int(input('Posicao do vertice inicial: '))
    menor_caminho = djikstra(arquivo,posicao_inicial)
    print(menor_caminho)
