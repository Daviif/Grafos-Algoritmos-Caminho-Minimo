#Implementação do Algoritimo de Dijkstra
import listaAdjacencias
import matrizAdjacencias
import time
import tracemalloc
   
def Dijkstra(grafo, verticeOrigem):
    tracemalloc.start() #Tracemalloc é usado para medir o uso de memória
    tempo_inicial = time.time() # Marca o tempo inicial da execução

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
    caminho[verticeOrigem] = [verticeOrigem]
    caminho = [[] for _ in range(grafo.numVertices)]

    #Dist inicial para o vértice de origem é 0, e o predecessor é o próprio vértice de origem
    dist[verticeOrigem] = 0
    prev[verticeOrigem] = verticeOrigem
    
    #Conjunto de todos os vértices do grafo
    V = set(range(grafo.numVertices))

    # Conjunto de vértices não visitados (abertos)
    O = set(range(grafo.numVertices))

    # Conjunto de vértices visitados (fechados)
    C = set()

    #Enquanto o conjunto de vértices visitados não for igual ao conjunto de todos os vértices
    while C != V:
        distMin = float('inf') # Inicializa a distância mínima como infinito
        u = None # Inicializa o vértice u como None(nulo)

        # Encontra o vértice com a menor distância no conjunto O, percorrendo todos os vértices não visitados
        for verticeA in O:
            if dist[verticeA] < distMin:
                distMin = dist[verticeA]
                u = verticeA

        O.remove(u) #remove o vértice u do conjunto de não visitados
        C.add(u) #adiciona o vértice u ao conjunto de visitados

        if tipo == "Matriz": #Para matriz de adjacências
            # Percorre os vizinhos do vértice u
            for v in grafo.vizinhos(u):
                peso = grafo.matriz[u][v] # Peso da aresta entre u e v
                if v not in C and peso > 0: # verifica se v não foi visitado e se o peso é positivo
                    if dist[v] > dist[u] + peso: # verifica se a distância atual para v é maior que a distância de u mais o peso da aresta
                        dist[v] = dist[u] + peso # Atualiza a distância para v
                        prev[v] = u # Atualiza o predecessor de v
                        caminho[v] = caminho[u] + [v]   # adiciona o caminho até v
        elif tipo == "Lista": #Para lista de adjacências
            for v, peso in grafo.vizinhos(u): 
                if v not in C and peso > 0:
                    if dist[v] > dist[u] + peso:
                        dist[v] = dist[u] + peso
                        prev[v] = u
                        caminho[v] = caminho[u] + [v]

    #Reconstrução do caminho mínimo                    
    destino = grafo.numVertices - 1
    caminho = []
    atual = destino
    while atual != verticeOrigem:
        caminho.append(atual)
        atual = prev[atual]

    caminho.append(verticeOrigem)
    caminho.reverse()

    caminho_str = '-'.join(str(v) for v in caminho)
    custo_total = dist[destino]

    # Marca o tempo final da execução e calcula o uso de memória
    tempo_final = time.time()
    current, peak = tracemalloc.get_traced_memory()
    
    tracemalloc.stop()
    tempo_execucao = tempo_final - tempo_inicial
    
    # Exibe o caminho mínimo, custo total, tempo de execução e uso de memória
    print(f"Caminho mínimo de 0 até {grafo.numVertices - 1}: {caminho}")
    print(f"Custo total: {custo_total}")
    print(f"Tempo de execução: {tempo_execucao:.6f} s")
    print(f"Memória: {peak / (1024 * 1024):.6f} MB; {peak / 1024:.6f} KB")
    
    return caminho_str, custo_total