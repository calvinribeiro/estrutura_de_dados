#exercicio1

#nota1 = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))
#nota3 = float(input("Digite a terceira nota: "))
#nota4 = float(input("Digite a quarta nota: "))
#nota5 = float(input("Digite a quinta nota: "))

#media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

#if media >= 7:
#    print(f"Média: {media:.2f}")
#    print("Aluno aprovado!")
#else:
#    print(f"Média: {media:.2f}")
#    print("Aluno reprovado.")



#exercicio2

#def calcular_fatorial(numero):
#    if numero < 0:
#        return "O fatorial não está definido para números negativos."
#    elif numero == 0 or numero == 1:
#        return 1
#    else:
#        fatorial = 1
#        for i in range(2, numero + 1):
#            fatorial *= i
#        return fatorial

#numero = int(input("Digite um número inteiro positivo: "))

#resultado = calcular_fatorial(numero)
#print(f"O fatorial de {numero} é {resultado}")



#exercicio3

#import re

#def eh_palindromo(texto):
#    texto = re.sub(r'[^a-zA-Z]', '', texto.lower())

#    return texto == texto[::-1]

#entrada = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

#if eh_palindromo(entrada):
#    print(f"'{entrada}' é um palíndromo.")
#else:
#    print(f"'{entrada}' não é um palíndromo.")



#exercicio4

#numero = int(input("Digite um número inteiro positivo: "))

#if numero < 0:
#    print("O número deve ser positivo.")
#else:
#    soma = 0

#    numero_str = str(numero)

#    for digito in numero_str:
#        soma += int(digito)

#    print(f"A soma dos dígitos de {numero} é {soma}")



#exercicio5

#def eh_primo(numero):
#    if numero <= 1:
#        return False
#    elif numero <= 3:
#        return True
#    elif numero % 2 == 0 or numero % 3 == 0:
#        return False
#    else:
#        i = 5
#        while i * i <= numero:
#            if numero % i == 0 or numero % (i + 2) == 0:
#                return False
#            i += 6
#        return True

#numero = int(input("Digite um número inteiro: "))

#if eh_primo(numero):
#    print(f"{numero} é um número primo.")
#else:
#    print(f"{numero} não é um número primo.")



#exercicio6

#texto = input("Digite uma string: ")

#texto = texto.lower()

#contador_vogais = 0

#for caractere in texto:
#    if caractere in "aeiou":
#        contador_vogais += 1

#print(f"A quantidade de vogais na string é: {contador_vogais}")



#exercicio7

#def calcular_imc(peso, altura):
#    if peso <= 0 or altura <= 0:
#        return "Peso e altura devem ser valores positivos."
#    else:
#        imc = peso / (altura ** 2)
#        return imc

#peso = float(input("Digite seu peso (em kg): "))
#altura = float(input("Digite sua altura (em metros): "))

#resultado = calcular_imc(peso, altura)

#if isinstance(resultado, float):
#    print(f"Seu IMC é {resultado:.2f}")
#else:
#    print(resultado)



#exercicio8

#def celsius_para_fahrenheit(celsius):
#    return (celsius * 9/5) + 32

#def fahrenheit_para_celsius(fahrenheit):
#    return (fahrenheit - 32) * 5/9

#print("Escolha a opção de conversão:")
#print("1. Celsius para Fahrenheit")
#print("2. Fahrenheit para Celsius")
#opcao = int(input("Digite o número da opção desejada (1/2): "))

#if opcao == 1:
#    celsius = float(input("Digite a temperatura em Celsius: "))
#    fahrenheit = celsius_para_fahrenheit(celsius)
#    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f} °F")
#elif opcao == 2:
#    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
#    celsius = fahrenheit_para_celsius(fahrenheit)
#    print(f"A temperatura em Celsius é: {celsius:.2f} °C")
#else:
#    print("Opção inválida. Escolha 1 para Celsius para Fahrenheit ou 2 para Fahrenheit para Celsius.")



#exercicio9

#def adicao(x, y):
#    return x + y

#def subtracao(x, y):
#    return x - y

#def multiplicacao(x, y):
#    return x * y

#def divisao(x, y):
#    if y == 0:
#        return "Erro! Divisão por zero."
#    else:
#        return x / y

#print("Escolha a operação:")
#print("1. Adição")
#print("2. Subtração")
#print("3. Multiplicação")
#print("4. Divisão")

#opcao = input("Digite o número da operação desejada (1/2/3/4): ")

#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))

#if opcao == '1':
#    resultado = adicao(numero1, numero2)
#    print(f"Resultado: {numero1} + {numero2} = {resultado}")
#elif opcao == '2':
#    resultado = subtracao(numero1, numero2)
#    print(f"Resultado: {numero1} - {numero2} = {resultado}")
#elif opcao == '3':
#    resultado = multiplicacao(numero1, numero2)
#    print(f"Resultado: {numero1} * {numero2} = {resultado}")
#elif opcao == '4':
#    resultado = divisao(numero1, numero2)
#    print(f"Resultado: {numero1} / {numero2} = {resultado}")
#else:
#    print("Opção inválida. Por favor, escolha uma operação válida (1/2/3/4).")



#exercicio10

#def gerar_sequencia_fibonacci(num_termos):
#    sequencia = []
#    a, b = 0, 1

#    for _ in range(num_termos):
#        sequencia.append(a)
#        a, b = b, a + b

#    return sequencia

#num_termos = int(input("Digite o número de termos da sequência de Fibonacci desejado: "))

#if num_termos <= 0:
#    print("O número de termos deve ser maior que zero.")
#else:
#    resultado = gerar_sequencia_fibonacci(num_termos)
#    print(f"Sequência de Fibonacci com {num_termos} termos:")
#    print(resultado)

