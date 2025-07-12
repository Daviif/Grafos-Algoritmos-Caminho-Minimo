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
    for k in range (0, len(V)):
        atualizou = False
        for u in V:
            if tipo == "Matriz":
                for v in grafo.vizinhos(u):
                    peso = grafo.matriz[u][v]
                    if dist[v] > dist[u] + peso:
                        dist[v] = dist[u] + peso
                        prev[v] = u
                        atualizou = True
                        caminho[v] = caminho[u] + [v]
            elif tipo == "Lista":
                for v, peso in grafo.vizinhos(u):
                    if v not in dist:
                        print(f"ERRO: Vértice inválido encontrado: {v} (vindo de {u})")
                    if dist[v] > dist[u] + peso:
                        dist[v] = dist[u] + peso
                        prev[v] = u
                        atualizou = True
                        caminho[v] = caminho[u] + [v]
                
        if atualizou == False:
            k = V

    #Reconstrução do caminho mínimo                    
    caminho = []
    atual = verticeDestino
    while atual != verticeOrigem:
        caminho.append(atual)
        atual = prev[atual]

    caminho.append(verticeOrigem)
    caminho.reverse()

    custo_total = dist[verticeDestino]

    # Marca o tempo final da execução e calcula o uso de memória
    tempo_final = time.time()
    current, peak = tracemalloc.get_traced_memory()
    
    tracemalloc.stop()
    tempo_execucao = tempo_final - tempo_inicial
    
    # Exibe o caminho mínimo, custo total, tempo de execução e uso de memória
    print("-------------------------------------")
    print("Algoritmo de Bellman-Ford")
    print(f"Caminho mínimo: {caminho}")
    print(f"Custo: {custo_total}")
    print(f"Tempo de execução: {tempo_execucao:.4f} s")
    print(f"Memória utilizada: {peak / (1024 * 1024):.4f} MB")