from grafo_dicionario import GrafoDicionario

def ciclo_euleriano(arquivo):

    def buscarSubcicloEuleriano(G, v, C):
        # Marca início do ciclo
        ciclo = [v]
        t = v
        while True:
            # Só prossegue se existir uma aresta não-visitada conectada a Ciclo
            for u in G.vizinhos(v).keys():
                if {u, v} in C or {v, u} in C:
                    break
            else:
                return None

            # Prosseguindo, marca a aresta como visitada, isto é, remove-la de C
            C.remove({v, u})
            # Adiciona o vértice v ao final do ciclo
            v = u
            ciclo.append(v)
            # Ciclo encontrado
            if v == t:
                break

        # Para todo vértice x no ciclo que tenha uma aresta adjacente não visitada
        for i in range(len(ciclo)):
            c = ciclo[i]
            for u in G.vizinhos(c).keys():
                # Se há uma aresta no ciclo que possui aresta não visitadas
                if {u, c} in C or {c, u} in C:
                    novo_ciclo = buscarSubcicloEuleriano(G, c, C)
                    if not novo_ciclo:
                        return None
                    # Inclui o novo ciclo no ciclo anterior
                    ciclo.pop(i)
                    for v in novo_ciclo[::-1]:
                        ciclo.insert(i, v)
        return ciclo

    # Inicialização
    G = GrafoDicionario(arquivo)
    C = G.E_set
    v = 0 # Altere aqui o indice

    return buscarSubcicloEuleriano(G, v, C)

if __name__ == '__main__':
    arquivo = input('Nome do arquivo: ')
    ciclo = ciclo_euleriano(arquivo)
    if ciclo:
        [print(v+1, end=',') for v in ciclo]
    else:
        print('0')
