# Lista de temperaturas lidas pelo sensor por minuto

# leituras = [70, 75, 82, 98, 110, 85, 80]
# baixos = [50, 55, 52, 30, 20, 15, 10]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRITICO: {temp}°C detectado! Acionando parada de emergência.")
#         break # O loop para aqui e NÃO lê os próximos valores (85 e 80)
#     else:
#         print(f"Temperatura está em {temp}°C. Operação normal.")

# for temp1 in baixos:
#       if temp1 < 50:  
#         print(f"CRITICO: {temp1}°C detectado! Acionando parada de emergência.")
#         break
#       else:
#         print(f"Temperatura está em {temp1}°C. Operação normal.")
# print("Checar sitema. Aguardando manutenção")

# exemplo 2
# materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
#         continue #Pula o restante do código abaixo e vai para a próxima peça

#     # Este código só roda se a peça for de metal
#     print(f"Processando peça de {peca}. Furando e polindo...")

# print("Fim do lote de produção.")

# Exercício 1
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5).

# for numero in range(1,11):
#     if numero == 5:
#         print(f"Falha ao ler o nº {numero}")
#         continue
#     print(numero)
# print("Fim da contagem!")

# Exercício 2
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa

# from time import sleep
# for i in range(1,11):
#     sleep(0.5)
#     print("Verde")
# print("Siga em frente")

# for i in range(1,11):
#     sleep(1)
#     print("Amarelo")
# print("Atenção!")

# for i in range(1,11):
#     sleep(0.5)
#     print("Vermelho")
# print("Pare!")

# Exercício 3 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

# consumo = 0
# for maquina in range(1, 6):
#     consumo = consumo + int(input("Qual foi o consumo da máquina em kWh? \n"))
# print(f"O valor de consumo da máquina é de {consumo}")

#  4 - Identificador de Peças Defeituosas (for + if)
# Percorra uma lista de medidas de peças: 
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".

# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# for pecas in medidas:
#     if pecas > 50:
#         print(f"Peça {pecas} aprovada...")
#     else:
#         print(f"Peça {pecas} rejeitada...")