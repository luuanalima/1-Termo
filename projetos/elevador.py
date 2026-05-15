#Sistema de elevador de prédio
# o prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode
# se mover para cima ou para baixo, e tem a capacidade de tranasportar até 5 pessoas
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas
# O programa deve continuar rodando até que o usuario decida encerrar.

# Requisitos Funcionais (RF):
# O elevador deve se mover para cima e para baixo
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador possui uma capacidade limite de pessoas
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas.

# Requisitos Não Funcionais (RNF):
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas.
# O programa pode continuar rodando até que o usuario decida encerrar.
# O elevador pode começar do andar 0


def elevador():

    andar_atual = 0
    pessoas = 0 
    import time
    print(f"Seu andar atual é: {andar_atual}")
    print(f"Tem {pessoas} pessoas no elevador neste momento.")

    while True:
        chamar_elevador = input("Deseja chamar o elevador? (s/n): ")
        if chamar_elevador == "n":
            print("Saindo...")
            break
        
        elif chamar_elevador == "s":
            pessoas_elevador = int(input("Quantas pessoas irão usar o elevador? \n"))
            if pessoas_elevador > 5:
                print("Elevador está cheio!")
            elif pessoas_elevador <=5:
                andar_elevador = int(input("Qual andar você deseja ir? \n "))
            if andar_elevador >10:
                print("Este andar não existe!")
                
            elif andar_elevador < andar_atual:
                print ("Descendo...")
                time.sleep(4)
                print("O elevador chegou no seu andar!")
                print(f"Seu andar atual é {andar_elevador}.")
                andar_atual = andar_elevador + andar_atual

            elif andar_elevador >andar_atual:
                print ("Subindo...")
                time.sleep(4)
                print("O elevador chegou no seu andar!")
                print(f"Seu andar atual é {andar_elevador}.")
                andar_atual = andar_elevador - andar_atual

elevador()