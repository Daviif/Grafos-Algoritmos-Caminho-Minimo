from matrizAdjacencias import MatrizAdjacencias
from listaAdjacencias import ListaAdjacencias
from file import carregarGrafo
from dijkstra import Dijkstra
from bellman_ford import BellmanFord
from floyd_warshall import FloydWarshall
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python main.py <arquivo_grafo> <vertice_origem> <vertice_destino>")
        print("Exemplo: python main.py data/toy.txt 0 3")
        sys.exit(1)

    arquivo = sys.argv[1]
    vertice_origem = int(sys.argv[2])
    vertice_destino = int(sys.argv[3])

    grafos = carregarGrafo(arquivo)

    if grafos is None:
        print("Falha ao carregar o grafo.")
    else:
        GrafoM, GrafoL = grafos

    print("Processando.....")
    Dijkstra(GrafoM, vertice_origem, vertice_destino)
    Dijkstra(GrafoL, vertice_origem, vertice_destino)
    BellmanFord(GrafoM, vertice_origem, vertice_destino)
    BellmanFord(GrafoL, vertice_origem, vertice_destino)
    FloydWarshall(GrafoM, vertice_origem, vertice_destino)
    FloydWarshall(GrafoL, vertice_origem, vertice_destino)