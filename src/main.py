from matrizAdjacencias import MatrizAdjacencias
from listaAdjacencias import ListaAdjacencias
from file import carregarGrafo
from dijkstra import Dijkstra
from bellman_ford import BellmanFord
from floyd_warshall import FloydWarshall
import info
import os

if __name__ == "__main__":   
    grafos = carregarGrafo("data/toy.txt")

    if grafos is None:
        print("Falha ao carregar o grafo.")
    else:
        GrafoM, GrafoL = grafos

    print("Processando.....")
    Dijkstra(GrafoM, 0, 3)
    Dijkstra(GrafoL, 0, 3)
    BellmanFord(GrafoM, 0, 3)
    BellmanFord(GrafoL, 0, 3)
    FloydWarshall(GrafoM, 0, 3)
    FloydWarshall(GrafoL, 0, 3)