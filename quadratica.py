import math
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def sqrtsort_quadratic(V):
    n = len(V)
    k = int(math.sqrt(n))
    parts = [V[i:i + k] for i in range(0, n, k)]

    # Sort each part using insertion sort
    for part in parts:
        insertion_sort(part)

    # Find the smallest element in each part
    min_indexes = [0 for _ in range(len(parts))] 

    result = []
    while len(result) < n:
        min_value = float('inf')
        min_part_index = -1

        # Find the part with the smallest element
        for i, part in enumerate(parts):
            if min_indexes[i] < len(part) and part[min_indexes[i]] < min_value:
                min_value = part[min_indexes[i]]
                min_part_index = i

        result.append(min_value)
        min_indexes[min_part_index] += 1

        # If a part is empty, remove it
        if min_indexes[min_part_index] == len(parts[min_part_index]):
            parts.pop(min_part_index)
            min_indexes.pop(min_part_index) 

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
        sqrtsort_quadratic(V)
        fim = time.time()
        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)
        print(f"\n  Execução {n}: {tempo_execucao:.11f} segundos") 

    # Calcula a média dos tempos de execução
    #tempo_medio = sum(tempos) / num_repeticoes
    #print(f"\nTamanho da entrada: {n}, Tempo médio de execução: {tempo_medio:.11f} segundos")