total_vagas = 500
vagas_tag = 50
vagas_ocupadas = 0

registros = {}

while True:
    print("1- Entrada TAG")
    print("2- Entrada Ticket")
    print("3- Pagar")
    print("4- Saída")
    print("5- Perda de Ticket")
    print("0- Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        id_tag = input("Informe o ID da TAG: ")
        ativa = input("A TAG está ativa? (s/n): ")

        if ativa == "s":
            registros[id_tag] = {
                "tipo": "TAG",
                "entrada": (),
                "pago": False
            }
            vagas_ocupadas += 1
            print("Entrada liberada (TAG)")
        else:
            print("TAG inválida")

    elif opcao == "2":
        vagas_comuns = (total_vagas - vagas_tag) - vagas_ocupadas

        if vagas_comuns > 0:
            id_ticket = input("ID do Ticket: ")
            registros[id_ticket] = {
                "tipo": "TICKET",
                "entrada": (),
                "pago": False
            }
            vagas_ocupadas += 1
            print("Ticket emitido")
        else:
            print("Estacionamento lotado (vagas comuns)")

    elif opcao == "3":
        id_registro = input("ID: ")

        if id_registro in registros:
            entrada = registros[id_registro]["entrada"]
            tipo = registros[id_registro]["tipo"]

            minutos = int(input("Quantos minutos você permaneceu? "))

            if minutos <= 15:
                valor = 0
            elif minutos <= 180:
                valor = 15

            if tipo == "TAG":
                valor = valor * 0.9

            registros[id_registro]["pago"] = True

            print(f"Valor: R$ {valor:.2f}")
        else:
            print("Registro não encontrado")

    elif opcao == "4":
        id_registro = input("Informe o ID: ")

        if id_registro in registros:
            if registros[id_registro]["pago"] == True:
                print("Saída liberada")
            else:
                print("Pagamento não realizado")
        else:
            print("Registro não encontrado")

    elif opcao == "5":
        id_temp = input("ID provisório: ")

        registros[id_temp] = {
            "tipo": "TICKET",
            "entrada": (),
            "pago": True
        }

        print("Cobrança fixa: R$ 50,00")

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida")