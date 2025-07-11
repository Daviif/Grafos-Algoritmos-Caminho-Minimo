from matrizAdjacencias import MatrizAdjacencias
from listaAdjacencias import ListaAdjacencias

def carregarGrafo(nomeArquivo):
    #Variavael para armazenar o número de vértices, arestas e pesos
    numVertices = 0
    linhasValores = []

    try:
        with open(nomeArquivo, "r") as GD:
            #Primeira linha do arquivo contém o número de vértices e arestas
            linhaCabeçalho = next(GD).strip()
            tamanhoGrafo = linhaCabeçalho.split(" ")

            numVertices = int(tamanhoGrafo[0])
            numArestas = int(tamanhoGrafo[1])

            #Apartir da segunda linha, lê o destino, origem e peso
            for linha in GD:
                if linha.strip():
                    # Divide a linha em partes e converte para inteiro
                    quebra = linha.strip().split(" ")
                    origem = int(quebra[0])
                    destino = int(quebra[1])
                    peso = int(quebra[2]) if len(quebra) > 2 else 1
                    # Adiciona os valores à lista de arestas
                    linhasValores.append((origem, destino, peso))
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    # Inicializa os grafos, se houver vértices
    if numVertices > 0:
        GrafoM = MatrizAdjacencias(numVertices)
        GrafoL = ListaAdjacencias(numVertices)
        
        for valores in linhasValores:
            print("Adicionando aresta:", valores)  # debug
            origem, destino, peso = valores
            GrafoM.addAresta(origem, destino, peso)
            GrafoL.addAresta(origem, destino, peso)
        return GrafoM, GrafoL