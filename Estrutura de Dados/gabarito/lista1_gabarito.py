#exercicio1

#numero1 = float(input("Digite um número: "))
#numero2 = float(input("Digite o segundo número: "))
#numero3 = float(input("Digite o terceiro número: "))

#media = (numero1 + numero2 + numero3) / 3


#print(f"A média dos números {numero1}, {numero2} e {numero3} é: {media:.2f}")



#exercicio2

#numero = int(input("Digite um número: "))


#if numero % 2 == 0:
    #print(f"O número {numero} é par.")
#else:
    #print(f"O número {numero} é ímpar.")



#exercicio3

#numero = int(input("Digite um número inteiro: "))

#print(f"Números pares de 0 até {numero}:")

#for i in range(0, numero + 1, 2):
    #0print(i)



#exercicio4

#entrada = input("Digite uma lista de números separados por espaços: ")


#numeros_str = entrada.split()


#numeros = [int(numero) for numero in numeros_str]


#if len(numeros) == 0:
    #print("A lista está vazia. Não é possível encontrar o maior e o menor valor.")
#else:

    #maior_valor = max(numeros)
    #menor_valor = min(numeros)


    #print(f"O maior valor na lista é: {maior_valor}")
    #print(f"O menor valor na lista é: {menor_valor}")



#exercicio5

#entrada = input("Digite uma lista de números separados por espaços: ")


#numeros_str = entrada.split()


#numeros_pares = [int(numero) for numero in numeros_str if int(numero) % 2 == 0]


#if len(numeros_pares) == 0:
    #print("Não há números pares na lista.")
#else:

    #media = sum(numeros_pares) / len(numeros_pares)

    #print(f"A média dos números pares na lista é: {media}")



#exercicio6

#numero = int(input("Digite um número positivo: "))


#if numero < 0:
    #print("Por favor, insira um número positivo.")
#else:

    #fatorial = 1


    #for i in range(1, numero + 1):
        #fatorial *= i


    #print(f"O fatorial de {numero} é {fatorial}")



#exercicio7

#maximo = int(input("Digite um valor máximo para a sequência de Fibonacci: "))

#a, b = 0, 1

#while a <= maximo:
    #print(a, end=" ")
    #a, b = b, a + b



#exercicio8

#numero = int(input("Digite um número inteiro: "))

#if numero > 1:

    #for i in range(2, numero):
        #if (numero % i) == 0:
            #print(f"{numero} não é um número primo.")
            #break
    #else:
        #print(f"{numero} é um número primo.")
#else:
    #print(f"{numero} não é um número primo.")



#exercicio9

#nomes = input("Digite uma lista de nomes separados por vírgulas: ")


#lista_nomes = nomes.split(",")


#nomes_com_A = []


#for nome in lista_nomes:
    #if nome.strip().startswith('A'):
        #nomes_com_A.append(nome.strip())


#print("Nomes que começam com a letra 'A':")
#for nome in nomes_com_A:
    #print(nome)



#exercicio10

#import random


#print("Escolha uma opção:")
#print("1. Pedra")
#print("2. Papel")
#print("3. Tesoura")

#opcao_usuario = int(input("Digite o número da sua escolha (1/2/3): "))


#if opcao_usuario not in [1, 2, 3]:
    #print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
#else:

    #opcoes_computador = ["Pedra", "Papel", "Tesoura"]


    #opcao_computador = random.choice(opcoes_computador)


    #print(f"Você escolheu: {opcoes_computador[opcao_usuario - 1]}")
    #print(f"O computador escolheu: {opcao_computador}")


    #if opcoes_computador[opcao_usuario - 1] == opcao_computador:
        #print("Empate!")
    #elif (opcoes_computador[opcao_usuario - 1] == "Pedra" and opcao_computador == "Tesoura") or \
         #(opcoes_computador[opcao_usuario - 1] == "Papel" and opcao_computador == "Pedra") or \
         #(opcoes_computador[opcao_usuario - 1] == "Tesoura" and opcao_computador == "Papel"):
        #print("Você venceu!")
    #else:
        #print("O computador venceu!")
