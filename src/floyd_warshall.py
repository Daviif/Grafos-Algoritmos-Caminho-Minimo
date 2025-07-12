#Implementação do Algoritimo de Floyd-Warshall
import listaAdjacencias
import matrizAdjacencias
import time
import tracemalloc

def FloydWarshall(grafo, verticeOrigem, verticeDestino):
    tracemalloc.start()
    tempo_inicial = time.time()

    dist = [[float('inf')] * grafo.numVertices for i in range(grafo.numVertices)]
    prev = [[None] * grafo.numVertices for i in range(grafo.numVertices)]

    if isinstance(grafo, matrizAdjacencias.MatrizAdjacencias):
        tipo = "Matriz"
    elif isinstance(grafo, listaAdjacencias.ListaAdjacencias):
        tipo = "Lista"
    

    V = set(range(grafo.numVertices))
    A = set(range(grafo.numVertices))

    for i in V:
        for j in V:
            if tipo == "Matriz":
                peso = grafo.matriz[i][j]
                if i == j:
                    dist[i][j] = 0
                    prev[i][j] = i
                elif grafo.possuiAresta(i, j):
                    dist[i][j] = peso
                    prev[i][j] = i
                else:
                    dist[i][j] = float('inf')
                    prev[i][j] = None
            elif tipo == "Lista":
                if i == j:
                    dist[i][j] = 0
                    prev[i][j] = i
                elif grafo.possuiAresta(i, j):
                    for v, peso in grafo.vizinhos(i):
                        if v == j:
                            dist[i][j] = peso
                            prev[i][j] = i
                            break
                else:
                    dist[i][j] = float('inf')
                    prev[i][j] = None
            

    for k in V:
        for i in V:
            for j in V:
                if time.time() - tempo_inicial > 600:
                    print("⏱️ Floyd-Warshall excedeu o tempo de 10 minutos!")
                    return
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = k
    
    #Reconstrução do caminho mínimo
    caminho = []                
    if prev[verticeOrigem][verticeDestino] is None:
        print("Não há caminho entre os vértices especificados.")
    else:
        pilha = [(verticeOrigem, verticeDestino)]
        while pilha:
            i, j = pilha.pop()
            k = prev[i][j]
            if k == i:
                caminho.append(i)
                if i != j:
                    caminho.append(j)
            else:
                pilha.append((k, j))
                pilha.append((i, k))
                
        caminho_corrigido = [caminho[0]]
        for v in caminho[1:]:
            if v != caminho_corrigido[-1]:
                caminho_corrigido.append(v)
        caminho = caminho_corrigido

    custo_total = dist[verticeOrigem][verticeDestino]

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
    print(f"Tempo de execução: {tempo_execucao:.3f} s")
    print(f"Memória utilizada: {peak / (1024 * 1024):.4f} MB")
                
