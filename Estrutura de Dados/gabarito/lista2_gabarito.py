#exercicio1

#import math

#class Circulo:
    #def __init__(self, raio):
        #self.raio = raio

    #def calcular_area(self):

        #area = math.pi * self.raio ** 2
        #return area


#raio_do_circulo = 5.0  # Substitua pelo raio desejado
#circulo = Circulo(raio_do_circulo)
#area_do_circulo = circulo.calcular_area()
#print(f"A área do círculo com raio {raio_do_circulo} é {area_do_circulo:.2f}")



#exercicio2

#class Livro:
#    def __init__(self, titulo, autor):
#        self.titulo = titulo
#        self.autor = autor

#    def detalhes(self):
#        return f"Título: {self.titulo}\nAutor: {self.autor}"

#livro1 = Livro("Dom Quixote", "Miguel de Cervantes")
#livro2 = Livro("Cem Anos de Solidão", "Gabriel García Márquez")

#print("Detalhes do Livro 1:")
#print(livro1.detalhes())

#print("\nDetalhes do Livro 2:")
#print(livro2.detalhes())



#exercicio3

#class Retangulo:
#    def __init__(self, base, altura):
#        self.base = base
#        self.altura = altura

#    def calcular_area(self):
#        return self.base * self.altura


#retangulo1 = Retangulo(5, 10)
#retangulo2 = Retangulo(8, 6)

#print(f"A área do retângulo 1 é {retangulo1.calcular_area()} unidades quadradas.")
#print(f"A área do retângulo 2 é {retangulo2.calcular_area()} unidades quadradas.")



#exercicio4

#class ContaBancaria:
#    def __init__(self, titular, saldo=0.0):
#        self.titular = titular
#        self.saldo = saldo

#    def depositar(self, valor):
#        if valor > 0:
#            self.saldo += valor
#            return f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}"
#        else:
#            return "O valor do depósito deve ser maior que zero."

#    def sacar(self, valor):
#        if valor > 0:
#            if valor <= self.saldo:
#                self.saldo -= valor
#                return f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}"
#            else:
#                return "Saldo insuficiente para efetuar o saque."
#        else:
#            return "O valor do saque deve ser maior que zero."


#conta = ContaBancaria("João")

#print(f"Saldo inicial da conta de {conta.titular}: {conta.saldo}")

#print(conta.depositar(100.0))
#print(conta.sacar(50.0))
#print(conta.sacar(70.0))



#exercicio5

#class Pessoa:
#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade

#    def falar(self):
#        print(f"{self.nome} está falando.")

#pessoa1 = Pessoa("Alice", 30)
#pessoa2 = Pessoa("Bob", 25)

#pessoa1.falar()
#pessoa2.falar()

#exercicio6

#class Produto:
#    def __init__(self, nome, preco, quantidade):
#        self.nome = nome
#        self.preco = preco
#        self.quantidade = quantidade

#    def calcular_total(self):
#        return self.preco * self.quantidade


#produto1 = Produto("Camiseta", 20.0, 3)
#produto2 = Produto("Tênis", 50.0, 2)

#total_produto1 = produto1.calcular_total()
#total_produto2 = produto2.calcular_total()

#print(f"Produto 1 - {produto1.nome}: Preço: R${produto1.preco}, Quantidade: {produto1.quantidade}, Total: R${total_produto1}")
#print(f"Produto 2 - {produto2.nome}: Preço: R${produto2.preco}, Quantidade: {produto2.quantidade}, Total: R${total_produto2}")

#exercicio7

#class Carro:
#    def __init__(self, marca, modelo, ano):
#        self.marca = marca
#        self.modelo = modelo
#        self.ano = ano

#    def detalhes(self):
#        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

#carro1 = Carro("Toyota", "Corolla", 2022)
#carro2 = Carro("Ford", "Mustang", 2023)

#print("Detalhes do Carro 1:")
#print(carro1.detalhes())

#print("\nDetalhes do Carro 2:")
#print(carro2.detalhes())



#exercicio8

#class Aluno:
#    def __init__(self, nome, notas):
#        self.nome = nome
#        self.notas = notas

#    def calcular_media(self):
#        if len(self.notas) > 0:
#            soma = sum(self.notas)
#            media = soma / len(self.notas)
#            return media
#        else:
#            return 0.0

#aluno1 = Aluno("João", [8.5, 7.0, 9.5, 6.5])
#aluno2 = Aluno("Maria", [])

#media_aluno1 = aluno1.calcular_media()
#media_aluno2 = aluno2.calcular_media()

#print(f"Média das notas do aluno {aluno1.nome}: {media_aluno1:.2f}")
#print(f"Média das notas do aluno {aluno2.nome}: {media_aluno2:.2f}")



#exercicio9

#class Triangulo:
#    def __init__(self, lado1, lado2, lado3):
#        self.lado1 = lado1
#        self.lado2 = lado2
#        self.lado3 = lado3

#   def calcular_perimetro(self):
#        return self.lado1 + self.lado2 + self.lado3

#triangulo1 = Triangulo(3, 4, 5)
#triangulo2 = Triangulo(6, 8, 10)

#perimetro_tri1 = triangulo1.calcular_perimetro()
#perimetro_tri2 = triangulo2.calcular_perimetro()

#print(f"Perímetro do triângulo 1: {perimetro_tri1}")
#print(f"Perímetro do triângulo 2: {perimetro_tri2}")



#exercicio10

#class Funcionario:
#    def __init__(self, nome, salario, cargo):
#        self.nome = nome
#        self.salario = salario
#        self.cargo = cargo

#    def aumentar_salario(self, percentual_aumento):
#        if percentual_aumento > 0:
#            aumento = (percentual_aumento / 100) * self.salario
#            self.salario += aumento
#            return f"O salário de {self.nome} foi aumentado em {percentual_aumento}% para R${self.salario:.2f}"
#        else:
#            return "O percentual de aumento deve ser maior que zero."

#funcionario1 = Funcionario("João", 3000.0, "Analista")
#funcionario2 = Funcionario("Maria", 4500.0, "Gerente")

#print(funcionario1.aumentar_salario(10))
#print(funcionario2.aumentar_salario(5))

