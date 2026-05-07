# # Condições lógicas
# # if: "Se" a condição for verdadeira.
# # elif: "Senão, se" (usado para múltiplas condições).
# # else: "Senão" (executa se nenhuma das anteriores for verdadeira).

print("verificar maioridade")
idade = int(input("digite sua idade \n"))

if idade >= 18:
    print("você é adulto")
elif idade >= 16:
    print("Você não é adulto mas pode votar")
else: 
    print("você é adolescente")

# # Sinais de > Maior e >= Maior igual
# # Sinais de < Menor e <= Menor igual
# # Sinais de == Igual 

# #Exemplo 2 
print("Loja")
print("Bem-vindo ao sistema da luana")
print("Opções:")
print("1 - Sapatos")
print("2 - Roupas")
print("3 - Perfumes")

escolha = int(input("Digite sua escolha pelo numero da opção: \n "))
if escolha == 1:
    print("Você quer compar sapatos, OK")
    v1 = float(input("Digite o valor do produto: \n "))
    qnt1 = int(input("Digite a quantidade desejada: \n "))
    total = v1 * qnt1
    print("Sua compra de sapatos foi um total de: ", total)

elif escolha == 2:
    print("Você quer comprar Roupas, OK")
    v2  = float(input("Digite o valor do produto: \n "))
    qnt2 = int(input("Digite a quantidade desejada: \n "))
    total = v2 * qnt2
    print("Sua compra de Roupas foi um total de: ", total)

elif escolha == 3:
    print("Você quer comprar Perfumes, OK")
    v3 = float(input("Digite o valor do produto: \n "))
    qnt3 = int(input("Digite a quantidade desejada: \n "))
    total = v3 * qnt3
    print("Sua compra de Perfumes foi um total de: ", total)

else:
    print("Obrigada por utilizar o sistema da Luana")

# # Exemplo 3
print("Escolha uma opção para iniciar o Sistema")
print("Series = S")
print("Filmes = F")
categoria = input("Digite sua categoria \n ")
if categoria == "S":
    print("Você escolheu por Séries \n ")
elif categoria == "F":
    print("Você escolheu por filmes \n ")
else:
    print("Obrigada por escolher uma das categorias")

# # Exercício 1
# # Crie um algoritimo que simule uma calculadora e que por opção de escolha permita calcular os operadores.
# # Ex: Ao escolher a opção 1, ele irá calcular a soma e assim por diante

print("Bem- vindo a calculadora")
print("Escolha oque deseja calcular")
print("Soma = SS")
print("Subtração = SU")
print("Multiplicação = M")
print("Divisão = DV")

cálculo = input("Digite a expressão \n ")
if cálculo == "SO":
    print("Você escolheu somar")
    v6 = float(input("Digite o valor que deseja somar: \n "))
    num1 = int(input("Digite o segundo valor desejado: \n "))
    total = v6 + num1
    print("Sua conta foi um total de: ", total)

if cálculo == "SU":
    print("Você escolheu subtrair")
    v7 = float(input("Digite o valor que deseja subtrair: \n"))
    num2 = int(input("Digite o segundo valor desejado: \n "))
    total = v7 - num2
    print("Sua conta foi um total de: ", total)

if cálculo == "MU":
    print("Você escolheu Multiplicar")
    v8 = float(input("Digite o valor que deseja multiplicar: \n "))
    num3 = int(input("Digite o segundo valor desejado: \n "))
    total = v8 * num3
    print("Sua conta foi um total de: ", total)

if cálculo == "DV":
    print("Você escolheu Dividir")
    v9 = float(input("Digite o valor que deseja Dividir: \n "))
    num4 = int(input("Digite o segundo valor desejado: \n "))
    total = v9 / num4
    print("Sua conta foi um total de: ", total)

    print("Obrigada por usar a calculadora da Luana")

#     # Exercício 2
#     # Calculo de idade: Deve apresentar o nome, curso, data nascimento (ano) e apresentar a idade sua no final. 

    print("Bem-vindo ao cálculo de idades")
    nome = input("Digite o seu nome: \n ")
    curso = input("Digite seu curso: \n ")
    nascimento = float(input("Digite seu ano de nascimento: \n "))
    idade = 2026 - nascimento
    print("Sua idade é:", idade)

#     # Exercício 3
#     # Calcular gorjetas receba o valor da conta de um restaurante e retorne o valor da gorjeta (considerando 10% do valor da conta)
#     # Atendimento em mesa com garçom 10%
#     # Atendimento em mesa sem garçom 5%

print("Bem-vindo ao cálculo de gorjetas") 
garçom = input("Digite se o seu atendimento foi com ou sem garçom: \n ")

if garçom == "Sem":
    print("Você não recebeu atendimento de um garçom")
    v10 = float(input("Digite o valor da sua comanda: \n "))
    total = v10 * (5 / 100) + v10
    print("Sua conta foi um total de: ", total)

if garçom == "Com":
    print("Você recebeu o atendimento de um garçom")
    v11 = float(input("Digite o valor da sua comanda: \n "))
    total = v11 * (10 / 100) + v11
    print("Sua conta foi um total de: ", total)

    # Exercício 4
    # Criar um sistema para calcular o sucessor e antecessor de um valor

print("Bem vindo ao calculador de antecessor ou sucessor")
n1 = float(input("Qual o valor que deseja saber o antecessor e sucessor: \n "))
n2 = n1 - 1
n3 = n1 + 1
print("Seu antecessor é: ", n2, "Seu sucessor é: ", n3)

    # Exercício 5
    # Criar um algoritmo para calcular a venda de livros e que toda venda apresente um desconto fixo de 5%
n1 = float(input("Informe o valor da soma dos livros que você quer comprar, para adicionar o desconto: \n "))
n2 = n1 * (5/100)
n3 = n1 - n2
print("O valor da sua conta é: ", n3)

