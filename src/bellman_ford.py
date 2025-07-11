#Implementação do Algoritimo de Bellman-Ford
import listaAdjacencias
import matrizAdjacencias
import time
import tracemalloc

def BellmanFord(grafo, verticeOrigem, verticeDestino):
    tracemalloc.start()
    tempo_inicial = time.time()

    if isinstance(grafo, matrizAdjacencias.MatrizAdjacencias):
        tipo = "Matriz"
        dist = [float('inf')] * grafo.numVertices
        prev = [None] * grafo.numVertices
    elif isinstance(grafo, listaAdjacencias.ListaAdjacencias):
        tipo = "Lista"
        dist = {V:float('inf') for V in range(grafo.numVertices)}
        prev = {V: None for V in range(grafo.numVertices)}

    #Caminhos, para reconstruir o caminho mínimo
    caminho = [[] for i in range(grafo.numVertices)]
    caminho[verticeOrigem] = [verticeOrigem]

    dist[verticeOrigem] = 0
    prev[verticeOrigem] = verticeOrigem

    V = set(range(grafo.numVertices))
    k = 0
    for k in V - 1:
        atualizou = False
        for u in V:
            for v in grafo.vizinhos(u):
                peso = grafo.matriz[u][v] 
                if dist[v] > dist[u] + peso:
                    dist[v] = dist[u] + peso
                    prev[v] = u
                    atualizou = True
                    caminho[v] = caminho[u] + [v]

        if atualizou == False:
            k = V