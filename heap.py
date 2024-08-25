import heapq
import math
import random
import time

def sqrtsort_heap(V):
    n = len(V)
    k = int(math.sqrt(n))
    parts = [V[i:i + k] for i in range(0, n, k)]

    # Transform each part into a heap
    for part in parts:
        heapq.heapify(part)

    result = []
    while parts:
        # Find the minimum element in each part
        min_elements = [(part[0], idx) for idx, part in enumerate(parts) if part]
        min_value, min_index = min(min_elements)

        # Add the minimum element to the result
        result.append(min_value)

        # Remove the minimum element from the corresponding part
        heapq.heappop(parts[min_index])
        if not parts[min_index]:
            parts.pop(min_index)

    return result

# Tamanhos de entrada para teste
tamanhos_entrada = [10**4, 10**5, 10**6, 10**7, 10**8]
num_repeticoes = 1  # Número de repetições para calcular a média

for n in tamanhos_entrada:
    tempos = []
    for i in range(num_repeticoes):
        # Gera lista aleatória de tamanho n
        V = [random.randint(1, 1000000) for _ in range(n)]  

        # Mede o tempo de execução da função
        inicio = time.time()
        sqrtsort_heap(V)
        fim = time.time()
        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)
        print(f"\n  Execução {n}: {tempo_execucao:.11f} segundos") 

    # Calcula a média dos tempos de execução
    #tempo_medio = sum(tempos) / num_repeticoes
    #print(f"\nTamanho da entrada: {n}, Tempo médio de execução: {tempo_medio:.11f} segundos")
