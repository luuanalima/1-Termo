# Atividade 1: Mensagem de Boas-Vindas
# Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da
# programação em Python!".

#print("Bem-vindo ao mundo da programação em Python")

# Atividade 2: Informações Pessoais
# Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.
# Exemplo de saída:
# Fulano de Tal
# 30

# print("Informações pessoais")
# print("Qual é seu nome completo?")
# nome = input("digite seu nome \n")

# print("Qual é sua idade?")
# idade = int(input("digite sua idade \n"))

# print("Seu nome é:", nome)
# print("Sua idade é:", idade)

# Atividade 3: Calculadora de Soma e Subtração
# Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512
# por 128. Cada resultado deve ser exibido em uma linha separada.
# ● Dica: Use o print() diretamente com os operadores (print(135 + 246)).
# ● Obs: Realize também a mesma situação com variáveis

# print("Bem-vindo a calculadora de Soma e Subtração")
# print("Para somar:")
# n1 = int(input("Digite o valor do primeiro numero para somar:"))
# n2 = int(input("Informe o valor do segundo numero para somar:"))
# soma = n1 + n2
# print("Resultado:" , n1 + n2)

# print("Para subtrair:")
# n3= int(input("Informe o valor do primeiro numero para subtrair:"))
# n4 = int(input("Informe o valor do segundo numero para subtrair:"))
# subtração = n3 - n4
# print("Resultado:" , n3 - n4)

# Atividade 4: Multiplicação e Divisão
# Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da
# divisão de 78 por 3.

# print("Bem-vindo a calculadora de Multiplicação e Divisão")
# print("Para multiplicar:")
# n5 = int(input("Digite o valor do primeiro numero para multiplicação:"))
# n6 = int(input("Informe o valor do segundo numero para a multiplicação:"))
# soma = n5 * n6
# print("Resultado:" , n5 * n6)

# print("Para dividir:")
# n7 = int(input("Digite o valor:"))
# n8 = int(input("Informe o valor do segundo numero para a divisão:"))
# soma = n7 / n8
# print("Resultado:" , n7 / n8)

# Atividade 5: Potenciação
# Calcule e exiba o resultado de "5 elevado à 3a potência" (53).
# ● Dica: O operador de potenciação em Python é **.

# print("Bem-vindo a calculadora de Potenciação")
# print("O valor é:")
# print(5**3)

# Atividade 6: Concatenando Palavras
# Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use
# o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.
# ● Exemplo: print("Maria" + " " + "Silva")

# print("Meu nome é: Luana" + " " + "Lima")

# Atividade 7: Cálculo de Eficiência (OEE)
# ● Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule
# e exiba a taxa de aproveitamento (peças boas / total).

# print("Bem-vindo ao calculo de eficiencia")
# n9 = int(input("Qual é a quantidade de peças produzidas? \n"))
# n10 = int(input("Qual é a quantidade de peças defeituosas? \n"))
# n11 = n10 - n9
# print("Taxa de aproveitamento é: ", n11)

# Atividade 8: Descrição com Cálculos
# Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados:
# "Eu tenho 25 anos e, em 10 anos, terei 35 anos."
# ● Dica: Use a vírgula dentro do print() para combinar strings e cálculos.
# ● Ex: print("Texto", 25 + 10).
# print("Eu tenho", 20 + 5, "anos e, em 10 anos, terei", 25 + 10, "anos.")

# Atividade 9: Orçamento de Viagem (Cálculo com float)
# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e
# o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
# ● Ex: Fórmula: (custo_hotel * 3) + custo_passagem

# print("Bem - vindo ao calculo de orçamento de viagem")
# n1 = int(input("Olá, irei fazer seu orçamento da sua viagem. Estamos cobrando 250.50 por noite, quantas deseja ficar? \n"))
# total = (250.50 * n1) + 412
# print("Seu orçamento já somado com sua passagem é", total)

# Atividade 10: Desafio - Mini Relatório
# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a
# saída de forma organizada.
# ● Exemplo de saída:
# Relatório de Vendas
# Produto: Notebook Gamer
# Quantidade vendida: 15
# Preço unitário: R$ 5499.50
# Total de vendas: R$ 82492.50

# n1 = input("Qual o produto que deseja fazer o relatório de vendas? \n")
# n2 = int(input("Qual a quantidade vendida? \n"))
# n3 = int(input("Qual o valor de cada produto? \n"))
# n4 = n3 * n2
# print("Seu relatório de Vendas, esta pronto!")
# print("Seu produto escolhido para o relatório foi:", n1)
# print("A quantidade vendida foi de:", n2)
# print("O preço unitário foi de: R$" , n3)
# print("Total de vendas: R$" , n4)
