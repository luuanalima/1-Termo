# 1. O laço 'for' (repetições determinadas)
# use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1: 
for lote in range(1, 6):
    print(f"Processando lote número {lote}...")
    print("Qualidade verificada. [OK]")
    print("Produção do dia finalizada!")

#Imagine que você queira atingir uma meta de produção de 5 carros e numera-los
for carro in range(1, 6):
    print(f"Processando meta de produção de carros {carro}...")
   
# Exemplo 2
# Contar até 4  
for i in range (5):
    print(i)

# Exemplo 3 
pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
tipospecas = ["Barra Dentada", "Porca do Eixo", "Anel Externo", "Parafuso Phillips", "Martelo cabeça chata"]

for item in pecas:
    print(f"Item em estoque: {item}")
    for tipos in tipospecas:
        print(f"Minha lista de tipos de peças: {tipospecas}")

# Exemplo 4
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar os produtos

print("Bem - vindo ao sistema de menu")
print("Escolha uma das opções:")
print("1 - Peças")
print("2 - Tipos de Peças")

opcao = int(input("Digite sua opção de pesquisa: "))
pecas = [pecas = "Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
tipospecas = ["Barra Dentada", "Porca do Eixo", "Anel Externo", "Parafuso Phillips", "Martelo cabeça chata"]

if opcao == 1:
    for item in pecas:
        print(f"Item em estoque: {item}")
        print("Fim da lista")
elif opcao == 2:
    for item in pecas:
        print(f"Item em estoque: {item}")
        print("Fim da lista")

# Exercicio 1 
# 1. Contador de Produção (for)
# Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça nº X processada com sucesso". No final, exiba "ciclo de produção concluido"

print("Bem - vindo ao contador")
for pecas in range(1, 11):
    print(f"Peça nº {pecas} processada com sucesso")
print("Ciclo de produção concluido!")

# Exercicio 2
# Imagine a produção de frutas em uma feira. desejo apresentar as frutas banana, manga, melancia, abacaxi. com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxis.

print("Bem - vindo a feira")
opcao = input("Digite sua opção de escolha de fruta: ")

for banana in range (1, 11):
    print(f" nº de bananas em estoque: {banana}")

for mangas in range (1, 6):
    print(f" nº de mangas em estoque: {mangas}")

for melancias in range (1, 11):
    print(f" nº de melancias em estoque: {melancias}")

for abacaxis in range (1, 14):
    print(f" nº de abacaxis em estoque: {abacaxis}")
   
# Exercicio 3
# montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta

print("Bem - Vindo as tabuadas")

numero = int(input("Digite o valor da tabuada:"))

print(f"Tabuada do {numero}:")
for tabuada in range(1, 11):
    resultado = numero * tabuada
    print(f"{numero} x {tabuada} = {resultado}")

# 2.  O laço while (Repetições Inderteminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergencia)
# Exemplo: monitor de temperatura estiver segura
# Inicio
# import time
temperatura = 25 
while temperatura < 40:
    print(f"temperatura atual: {temperatura}°C. Sistema operando ...")
    # time.sleep(2)
    temperatura += 3 #Simulando o aquecimento da máquina
print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Exemplo: Menu de Interação
# != diferente
# lower minusculo
# upper maiusculo
# opcao = ""

while opcao != "sair" and "SAIR":
    opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").lower()
    if opcao != "sair" and "SAIR":
        print(f"Dado '{opcao}' registrado no banco de dados.")
print("Sistema encerrado.")

# and e or
# and comparações verdadeiras e iguais
# or comparações verdadeiras e não iguais 

# Exercicio 5
# Monitor de Pressão crítica (while)
# Crie um simulador onde o usuario deve digitar a pressão atual de um compressor.
# Enquanto a pressão for menor que 100 PSI, o programa continua pedindo uma nova leitura.
# Assim que o usuario digitar um valor maior ou igual a 100, o loop para e exibe a mensagem : "ALERTA: Pressão critica atingida! Desligando sistema."

pressao = int(input("Digite a pressão atual: \n"))
while pressao < 100:
    pressao = int(input("Digite a pressão atual: \n"))
    print("Pressão OK")
    if pressao >= 100:
        print("ALERTA: Pressão critica atingida! Desligando sistema.")

# Exercicio 5
# Criar um menu de opções com 4 itens ex: Escolher series apresente sua escolha de series das outras tres.
# qualquer opcao diferente sair do menu

print("Escolha uma serie das opções:")
print("elite = 1")
print("you = 2")
print("la casa de papel = 3")
print("riverdale = 4")

series = input("sua escolha:")

