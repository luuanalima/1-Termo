# 1. Funcionalidades Principais:
#    - O programa deve permitir o cadastro de funcionários, incluindo nome, setor e status dos treinamentos (NR-10, NR-35 e Brigada).
#    - O programa deve verificar a obrigatoriedade de EPIs com base no setor do funcionário.
#    - O programa deve alertar sobre a necessidade de reciclagem do treinamento da Brigada de Incêndio com base no ano do último treinamento.
#    - O programa deve exibir um relatório geral com o total de funcionários cadastrados e quantos estão com treinamentos em dia.
#    - O programa deve validar os dados de entrada para garantir que o nome do funcionário seja uma string, o setor seja um dos setores pré-definidos.
#    - O programa deve calcular a validade do treinamento da Brigada de Incêndio com base no ano atual e no ano do último treinamento.
#    - O usuário deve ser capaz de cadastrar um funcionário fornecendo as informações necessárias.
#    - O usuário deve ser informado sobre os EPIs obrigatórios com base no setor do funcionário.
#    - O usuário deve receber alertas sobre a necessidade de reciclagem do treinamento da Brigada de Incêndio.

def brigada():

    total_funcionarios = 0
    funcionarios_em_dia = 0

    while True:

        print("Bem-vindo ao cadastro de funcionários!")
        nome = input("Digite o nome do funcionário: \n")
        setor = input("Digite o setor (Ex: elétrica, trabalho em altura): \n").strip().lower()
        nr10 = input("NR-10 está em dia? (s/n): ")
        nr35 = input("NR-35 está em dia? (s/n): ")
        brigada = input("Brigada de Incêndio está em dia? (s/n): ")

        if setor == "elétrica":
            print("EPIs Obrigatórios: Luvas de alta tensão e botas dielétricas.")
        elif setor == "trabalho em altura":
            print("EPIs Obrigatórios: Cinturão de segurança e talabarte.")
        else:
            print("Setor não exige EPIs específicos de risco no sistema.")

        print("Alerta de reciclagem!")
        ano_atual = 2026
        ano_treinamento = int(input("Qual foi seu último ano de treinamento da Brigada: \n "))
        tempo_reciclagem = ano_atual - ano_treinamento

        if tempo_reciclagem > 2:
            print("Treinamento Vencido! Encaminhar para reciclagem.")
        else:
            print("Treinamento Válido.")

        print("Relatório geral:")
        total_funcionarios += 1
        funcionarios_em_dia = 0

        if nr10 == "s" and nr35 == "s" and brigada == "s":
            funcionarios_em_dia += 1

        print(f"Total de funcionários cadastrados: {total_funcionarios}")
        print(f"Funcionários com treinamentos em dia: {funcionarios_em_dia}")

        sair = input("Deseja sair do cadastro? (s/n): ")

        if sair == "s":
            break

brigada()