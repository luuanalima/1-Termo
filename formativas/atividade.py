
# 1.Registro de Veículo: Peça o modelo do veículo e a placa.
# ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa
# viagem!"

# print("Bem-vindo ao registro de veículos!")
# modelo = input("Qual é o modelo do seu veículo? \n")
# placa = input("Qual é a sua placa? \n")
# print("Veículo", modelo, "de placa", placa, "registrado no sistema. Boa viagem!")

# 2.Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e
# o consumo médio do caminhão (km/l).
# ○ Calcule e exiba a distância total que o veículo pode percorrer com o tanque
# cheio.

# print("Bem-vindo ao cálculo de autonomia!")
# litros = float(input("Digite a capacidade do tanque de combustível em litros: \n"))
# consumo = float(input("Digite qual é o consumo médio do caminhão em km: \n"))
# total = litros/ consumo
# print("Seu caminhão pode percorrer o total de:", total,"com o tanque cheio." )

# 3.Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em
# Dólar (USD).
# ○ Converta para Real (BRL) considerando a taxa de $1,00~USD \approx
# 5,00~BRL$ e exiba com duas casas decimais.

# print("Bem-vindo ao conversor de moedas!")
# frete = float(input("Digite o valor do frete em dólares:\n "))
# total = frete * 5 
# print("Seu frete convertido em real é de:", round(total,2))

# 4. Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes
# realizadas por um motorista.
# ○ Exiba a média aritmética simples do tempo dessas entregas.

# print("Bem-vindo ao calculo da média de entrega!")
# n1 = int(input("Qual é o tempo de entrega (em horas) da primeira rota? \n"))
# n2 = int(input("Qual é o tempo de entrega (em horas) da segunda rota? \n"))
# n3 = int(input("Qual é o tempo de entrega (em horas) da terceira rota? \n"))
# total = ( n1 + n2 + n3) /3
# print("Sua média aritmética simples do tempo dessas entregas foi de: ", total)

# 5. Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# Abaixo de 10t: "Carga Leve".
# Entre 10t e 25t: "Carga padrão".
# Acima de 25t: "ALERTA: Excesso de Peso!".

# print("Bem-vindo ao monitor de carga!")
# carga = int(input("Qual é o peso atual do caminhão em toneladas? \n"))

# if carga <= 10:
#     print("Carga leve.")
# elif carga >= 25:
#     print("ALERTA: Excesso de Peso!")
# else: 
#     print("Carga padrão.")

# 6. Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba
# "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região
# Internacional".

# print("Bem-vindo ao classificador de destino!")
# codigo = input("Digite a primeira letra em maiusculo do código da sua carga: \n")

# if codigo == "N":
#     print("Região Norte.")

# elif codigo == "S":
#     print("Região Sul.")

# else:
#     print("Região Internacional.")

# 7. Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o
# motorista_identificado == "sim".
# ○ Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.

# checklist = input("O veículo está concluído para iniciar rota? \n")
# motorista = input("O motorista é alguém indentificado? \n ")

# if checklist == "concluído" and motorista == "sim":
#     print("Está liberado para iniciar a rota!")

# elif checklist == "concluído" and motorista == "não":
#     print("Não está liberado para iniciar rota.")

# else:
#     print("Falta de informação identificada")

# 8. Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas
# com atraso.
# ○ Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar
# Rotas", caso contrário, "Logística Eficiente".

# agendadas = int(input("Digite o total de entregas agendadas: \n"))
# atrasadas = int(input("Digite o total de entregas realizadas com atraso: \n"))

# entregas = (atrasadas / agendadas * 100) 
# if entregas > 10:
#     print(f"É necessário otimizar rotas. Índice de {entregas}%")
# else:
#     print(f"Lógica eficiente. Índice de {entregas}%")

# 9. Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# ○ Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.

# pneu = int(input("Qual é a medida da pressão desse pneu de carga? \n"))

# if pneu <= 100:
#     print("Abaixo do recomendado.")

# elif pneu >= 110:
#     print("Acima do recomendado.")

# else:
#     print("Dentro do padrão.")

# 10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5
# até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".

# print("O portão fecha em:")
# for i in range (6,0,-1):
#     print(i)
# print("Portão Trancado!")

# 11. Somatório de Fretes (Acumulador): Use um while para pedir o valor do frete de
# vários pedidos.
#  O loop para quando o usuário digitar 0. No fim, mostre o faturamento total
# acumulado.

# total = 0 

# while True:
#     frete = float(input("Digite o valor do frete: (0 para encerrar)\n"))

#     if frete == 0:
#         break

#     total += frete
# print(f"O faturamento total é de: RS{total}")

# 12.Monitoramento de Frota: Use um for para pedir a quilometragem de 5 veículos
# diferentes.
# ○ Ao final, mostre qual foi a maior quilometragem registrada.

# maior = 0

# for i in range (1, 6):
#     km = float(input(f"Qual é a quilometragem do veículo {i}? \n"))

#     if km > maior:
#         maior = km

# print (f"Maior quilometragem registrada {maior:} km ")

# 13.Sistema de Rastreio: Crie um while que peça o código de acesso do rastreador
# ("track99").
# ○ Enquanto o usuário errar, diga "Acesso Negado". Ele tem 3 tentativas. Se
# esgotar, exiba "Rastreamento Bloqueado".

# erros = 0
# tentativas = 3

# while erros != 3:

#     codigo = input("Digite o código de acesso: ")

#     if codigo != "track99":
#         erros = erros+1
#         tentativas = tentativas-1
#         print(f"Código incorreto. Tente novamente. Você tem mais {tentativas} tentativas")

#     else:
#         break

# if erros == 3:
#     print("Rastreamento Bloqueado. Usuário exedeu o limite máximo de 3 tentativas")

# else:
#     print("Codigo correto. Acesso Liberado")


# 14.Gerenciador de Combustível: Comece com um tanque de 500 litros. Crie um
# menu (while) onde o usuário pode: (1) Abastecer o tanque da base, (2) Retirar
# combustível para um caminhão ou (3) Sair.
# ○ Se o tanque da base ficar abaixo de 50 litros, avise: "Reserva Crítica!".
