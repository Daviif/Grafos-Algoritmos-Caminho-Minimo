#Implementação do Algoritimo de Floyd-Warshall
import listaAdjacencias
import matrizAdjacencias
import time
import tracemalloc

def FloydWarshall(grafo, verticeOrigem, verticeDestino):
    tracemalloc.start()
    tempo_inicial = time.time()

    if isinstance(grafo, matrizAdjacencias.MatrizAdjacencias):
        tipo = "Matriz"
        dist = [[float('inf')] * grafo.numVertices for i in range(grafo.numVertices)]
        prev = [[None] * grafo.numVertices for i in range(grafo.numVertices)]

    elif isinstance(grafo, listaAdjacencias.ListaAdjacencias):
        tipo = "Lista"
        dist = {V:float('inf') for V in range(grafo.numVertices)}
        prev = {V: None for V in range(grafo.numVertices)}
    
    #Caminhos, para reconstruir o caminho mínimo
    caminho = [[] for i in range(grafo.numVertices)]
    caminho[verticeOrigem] = [verticeOrigem]

    dist[verticeOrigem] = 0
    V = set(range(grafo.numVertices))
    A = set(range(grafo.numVertices))

    for i in V:
        for j in V:
            if tipo == "Matriz":
                peso = grafo.matriz[i][j]
                if i == j:
                    dist[i][j] = 0
                    prev[i][j] = i
                elif (i, j) in A:
                    dist[i][j] = peso
                    prev[i][j] = i
                else:
                    dist[i][j] = float('inf')
                    prev[i][j] = None
            

    for k in V:
        for i in V:
            for j in V:
                if tipo == "Matriz":
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        prev[i][j] = k
                        caminho[j] = caminho[i] + [j]
                elif tipo == "Lista":
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        prev[i][j] = k
                        caminho[j] = caminho[i] + [j]
    
     #Reconstrução do caminho mínimo                    
    caminho = []
    atual = verticeDestino
    while atual != verticeOrigem:
        caminho.append(atual)
        atual = prev[atual]

    caminho.append(verticeOrigem)
    caminho.reverse()

    caminho_str = '-'.join(str(v) for v in caminho)
    custo_total = dist[verticeDestino]

    # Marca o tempo final da execução e calcula o uso de memória
    tempo_final = time.time()
    current, peak = tracemalloc.get_traced_memory()
    
    tracemalloc.stop()
    tempo_execucao = tempo_final - tempo_inicial
    
    # Exibe o caminho mínimo, custo total, tempo de execução e uso de memória
    print("-------------------------------------")
    print("Algoritmo de Floyd-Warshall")
    print(f"Caminho mínimo: {caminho}")
    print(f"Custo: {custo_total}")
    print(f"Tempo de execução: {tempo_execucao:.4f} s")
    print(f"Memória utilizada: {peak / (1024 * 1024):.4f} MB")
                
