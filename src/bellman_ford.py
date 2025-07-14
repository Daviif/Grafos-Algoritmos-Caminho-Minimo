#Implementação do Algoritimo de Bellman-Ford
import listaAdjacencias
import matrizAdjacencias
import time
import tracemalloc

def BellmanFord(grafo, verticeOrigem, verticeDestino):
    tracemalloc.start()
    tempo_inicial = time.time()

    V = range(grafo.numVertices)

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

  

    dist[verticeOrigem] = 0
    prev[verticeOrigem] = verticeOrigem
   
    for k in range(len(V) - 1):
        atualizou = False
        for u in V:
            if time.time() - tempo_inicial > 600:
                print("Bellman-Ford excedeu o tempo de 10 minutos!")
                return
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
                    if dist[v] > dist[u] + peso:
                        dist[v] = dist[u] + peso
                        prev[v] = u
                        atualizou = True
                        caminho[v] = caminho[u] + [v]
                
        if atualizou == False:
            break; #k = V

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
    print("Algoritmo de Bellman-Ford")
    print(f"Caminho mínimo: {caminho}")
    print(f"Custo: {custo_total}")
    print(f"Tempo de execução: {tempo_execucao:.3f} s")
    print(f"Memória utilizada: {peak / (1024 * 1024):.4f} MB")