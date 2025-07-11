from matrizAdjacencias import MatrizAdjacencias
from listaAdjacencias import ListaAdjacencias
from dijkstra import Dijkstra
from file import carregarGrafo
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
        