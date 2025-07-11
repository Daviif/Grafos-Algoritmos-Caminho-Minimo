from matrizAdjacencias import MatrizAdjacencias
from listaAdjacencias import ListaAdjacencias
from dijkstra import Dijkstra
import info
import os

if __name__ == "__main__":
    #Variavael para armazenar o número de vértices, arestas e pesos
    linhasValores = []

    try:
        with open("src/grafo.txt", "r") as GD:
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
        Grafo1 = MatrizAdjacencias(numVertices)
        Grafo2 = ListaAdjacencias(numVertices)

        for valores in linhasValores:
            origem, destino, peso = valores
            Grafo1.addAresta(origem, destino, peso)
            Grafo2.addAresta(origem, destino, peso)

    #Exibe as informações dos grafos
    print("Grafo 1 - Matriz de Adjacências:")
    Grafo1.printGrafo()
    print("\nGrafo 2 - Lista de Adjacências:")
    Grafo2.printGrafo()

    print("\n--- Executando Dijkstra para Grafo 1 (Matriz) ---")
    Dijkstra(Grafo1, 0)
    print("\n--- Executando Dijkstra para Grafo 2 (Lista) ---")
    Dijkstra(Grafo2, 0)
        