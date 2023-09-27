#exercicio1

#def ordenar_por_selecao(vetor):
#    tamanho = len(vetor)

#    for i in range(tamanho):
#        indice_minimo = i
#        for j in range(i + 1, tamanho):
#            if vetor[j] < vetor[indice_minimo]:
#                indice_minimo = j

#        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

#vetor = [64, 34, 25, 12, 22, 11, 90]
#print("Vetor original:", vetor)

#ordenar_por_selecao(vetor)
#print("Vetor ordenado:", vetor)



#exercicio2

#def ordenar_vetor(vetor, ordem='crescente'):
#    if ordem == 'crescente':
#        vetor.sort()
#    elif ordem == 'decrescente':
#        vetor.sort(reverse=True)
#    else:
#        print("Opção de ordem inválida. Use 'crescente' ou 'decrescente'.")

#vetor = [64, 34, 25, 12, 22, 11, 90]
#print("Vetor original:", vetor)

#ordenar_vetor(vetor, ordem='crescente')
#print("Vetor ordenado em ordem crescente:", vetor)

#ordenar_vetor(vetor, ordem='decrescente')
#print("Vetor ordenado em ordem decrescente:", vetor)



#exercicio3

#def encontrar_maximo(vetor):
#    if not vetor:
#        return None
#    maximo = vetor[0]
#    for elemento in vetor:
#        if elemento > maximo:
#            maximo = elemento
#    return maximo

#def encontrar_minimo(vetor):
#    if not vetor:
#        return None
#    minimo = vetor[0]
#    for elemento in vetor:
#        if elemento < minimo:
#            minimo = elemento
#    return minimo

#vetor = [64, 34, 25, 12, 22, 11, 90]

#elemento_maximo = encontrar_maximo(vetor)
#elemento_minimo = encontrar_minimo(vetor)

#print("Vetor:", vetor)
#print("Elemento máximo:", elemento_maximo)
#print("Elemento mínimo:", elemento_minimo)



#exercicio4

#def encontrar_segundo_menor(vetor):
#    if len(vetor) < 2:
#        return None

#    menor = float('inf')
#    segundo_menor = float('inf')

#    for numero in vetor:
#        if numero < menor:
#            segundo_menor = menor
#            menor = numero
#        elif numero < segundo_menor and numero != menor:
#            segundo_menor = numero

#    if segundo_menor == float('inf'):
#        return None
#    else:
#        return segundo_menor

#vetor = [64, 34, 25, 12, 22, 11, 90, 12]

#segundo_menor = encontrar_segundo_menor(vetor)

#if segundo_menor is not None:
#    print("Vetor:", vetor)
#    print("Segundo menor número:", segundo_menor)
#else:
#    print("Não há segundo menor número no vetor.")



#exercicio5

#def remover_duplicatas(vetor):
#    vetor_sem_duplicatas = []
#    for elemento in vetor:
#        if elemento not in vetor_sem_duplicatas:
#            vetor_sem_duplicatas.append(elemento)
#    return vetor_sem_duplicatas

#vetor = [1, 2, 2, 3, 4, 4, 5, 5, 5]

#vetor_sem_duplicatas = remover_duplicatas(vetor)

#print("Vetor original:", vetor)
#print("Vetor sem duplicatas:", vetor_sem_duplicatas)



#exercicio6

#def ordenar_decrescente(vetor):
#    vetor.sort(reverse=True)

#def contar_pares_impares(vetor):
#    pares = 0
#    impares = 0
#    for numero in vetor:
#        if numero % 2 == 0:
#            pares += 1
#        else:
#            impares += 1
#    return pares, impares

#vetor = [64, 34, 25, 12, 22, 11, 90]

#ordenar_decrescente(vetor)
#print("Vetor ordenado em ordem decrescente:", vetor)

#pares, impares = contar_pares_impares(vetor)
#print("Quantidade de números pares:", pares)
#print("Quantidade de números ímpares:", impares)



#exercicio7

#def terceiro_maior(vetor):
#    vetor_sem_duplicatas = list(set(vetor))

#    if len(vetor_sem_duplicatas) < 3:
#        return "O vetor não tem pelo menos três números únicos."

#    vetor_sem_duplicatas.sort(reverse=True)
#    return vetor_sem_duplicatas[2]

#vetor = [12, 34, 25, 34, 22, 11, 90]

#terceiro = terceiro_maior(vetor)

#print("Vetor original:", vetor)
#print("Terceiro maior número:", terceiro)



#exercicio8

#def encontrar_mediana(vetor):
#    vetor.sort()

#    meio = len(vetor) // 2

#    mediana = vetor[meio]

#    return mediana

#vetor = [12, 34, 25, 22, 11, 90]

#mediana = encontrar_mediana(vetor)

#print("Vetor original:", vetor)
#print("Mediana:", mediana)

