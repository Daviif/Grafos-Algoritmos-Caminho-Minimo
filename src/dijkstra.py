#Implementação do Algoritimo de Dijkstra
import listaAdjacencias
import matrizAdjacencias

def Dijkstra(grafo, verticeOrigem):
    if isinstance(grafo, matrizAdjacencias.MatrizAdjacencias):
        tipo = "Matriz"
        dist = [float('inf')] * grafo.numVertices
        prev = [None] * grafo.numVertices
        O = set(range(grafo.numVertices))  # Conjunto de vértices não visitados
    elif isinstance(grafo, listaAdjacencias.ListaAdjacencias):
        tipo = "Lista"
        dist = {V:float('inf') for V in grafo.numVertices}
        prev = {V: None for V in grafo.numVertices}
        O = set(range(len(grafo)))  # Conjunto de vértices não visitados

   
    dist[verticeOrigem] = 0
    prev[verticeOrigem] = verticeOrigem

    C = set()

    while C != range(grafo.numVertices):
        u = verticeOrigem
        O.remove(u)
        C.add(u)

        if tipo == "Matriz":
            v = grafo.vizinhos(u)
            for v in range(grafo.numVertices):
                if v not in C:
                    peso = grafo.matriz[u][v]
                    if dist[v] > dist[u] + peso:
                        dist[v] = dist[u] + peso
                        prev[v] = u
    return dist