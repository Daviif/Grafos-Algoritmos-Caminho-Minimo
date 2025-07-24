#Implementação do Algoritimo de Dijkstra
import listaAdjacencias
import matrizAdjacencias
import time
import tracemalloc
   
def Dijkstra(grafo, verticeOrigem, verticeDestino):
    tracemalloc.start()
    tempo_inicial = time.time()

    #Verifica se o grafo é uma matriz de adjacências ou uma lista de adjacências
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

    #Dist inicial para o vértice de origem é 0, e o predecessor é o próprio vértice de origem
    dist[verticeOrigem] = 0
    prev[verticeOrigem] = verticeOrigem
    
    #Conjunto de todos os vértices do grafo, os não visitados, e os visitados
    V = set(range(grafo.numVertices))
    O = set(range(grafo.numVertices))
    C = set()

    #Enquanto o conjunto de vértices visitados não for igual ao conjunto de todos os vértices
    while C != V:
        distMin = float('inf') 
        u = None

        # Encontra o vértice com a menor distância no conjunto O, percorrendo todos os vértices não visitados
        for verticeA in O:
            if dist[verticeA] < distMin:
                distMin = dist[verticeA]
                u = verticeA
        if u is None:
            break

        if u == verticeDestino:
            break

        O.remove(u) 
        C.add(u) 

        if time.time() - tempo_inicial > 600:
            print("Dijkstra excedeu o tempo de 10 minutos!")
            return
        if tipo == "Matriz": #Para matriz de adjacências
            # Percorre os vizinhos do vértice u
            for v in grafo.vizinhos(u):
                peso = grafo.matriz[u][v] 
                if v not in C and peso > 0: 
                    if dist[v] > dist[u] + peso: 
                        dist[v] = dist[u] + peso 
                        prev[v] = u 
                        caminho[v] = caminho[u] + [v] 
        elif tipo == "Lista": #Para lista de adjacências
            for v, peso in grafo.vizinhos(u): 
                if v not in C and peso > 0:
                    if dist[v] > dist[u] + peso:
                        dist[v] = dist[u] + peso
                        prev[v] = u
                        caminho[v] = caminho[u] + [v]

    #Reconstrução do caminho mínimo  
    if dist[verticeDestino] == float('inf'):
        print("Não existe caminho entre os vértices.")
    else:                  
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
    print("Algoritmo de Dijkstra")
    print(f"Caminho mínimo: {caminho}")
    print(f"Custo: {custo_total}")
    print(f"Tempo de execução: {tempo_execucao:.3f} s")
    print(f"Memória utilizada: {peak / (1024 * 1024):.4f} MB")