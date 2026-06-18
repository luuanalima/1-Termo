total_vagas = 500
vagas_tag = 50
vagas_ocupadas = 0
livres = total_vagas - vagas_ocupadas

while True:
    print("1- Entrada TAG")
    print("2- Entrada Ticket")
    print("3- Pagar")
    print("4- Perda de Ticket")
    print("0- Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        tag = input("Qual é o ID da sua TAG: ")
        ativa = input("A TAG está ativa? (s/n): ")

        if ativa == "s":
            print("Pode entrar")
        else:
            print("TAG inválida")

    elif opcao == "2":
        livres = total_vagas - vagas_ocupadas

        if livres > 0:
            ticket = input("ID do Ticket: ")
            print("Ticket emitido")
            total_vagas = livres - 1
        else:
            print("Estacionamento lotado (vagas comuns)")

    elif opcao == "3":
        id = input("Você entrou com tag ou ticket?\n ").strip().lower()


        if id == "tag":
            valor = 0
            minutos = float(input("Informe o tempo que você ficou no shopping em minutos: "))

            if minutos <= 0.15:
                print("Obrigado.")

            elif 0.15 > minutos <3:
                
                valor = valor - (valor * 10 /100)


            else:
                valor = 25
                valor = valor - (valor * 10 /100)


            print(f"Valor: {valor:.2f}")
            forma_pagamento = input("Informe a sua forma de pagamento\n1-Débito\n2-Pix\n")
            if forma_pagamento =="1":
                saldo = float(input("Informe o saldo na sua conta:\n"))
                saldo_restante = saldo - valor
                if saldo >= valor:
                    print ("Acesso Liberado!")
                    print("Pagamento realizado")
                    print(f"Saldo restante:R${saldo_restante:.2f}")
                    total_vagas = +1
                    continue

                else:
                    print("Saldo Insuficiente")

            if forma_pagamento =="2":
                saldo = float(input("Informe o saldo na sua conta:\n"))
                saldo_restante = saldo - valor
                if saldo >= valor:
                    print ("Acesso Liberado!")
                    print("Pagamento realizado")
                    print(f"Saldo restante:R${saldo_restante:.2f}")
                    total_vagas = +1

                    continue
                else:
                    print("Saldo Insuficiente")

        elif id == "ticket":
             minutos = int(input("Informe o tempo que você ficou no shopping em minutos: "))

             if minutos <= 15:
              valor = 0

             elif minutos <= 180:
                valor = 15

             else:
              valor = 25
            
             print(f"Valor: {valor:.2f}")
             forma_pagamento = input("Informe a sua forma de pagamento\n1-Débito\n2-Pix\n")
             if forma_pagamento =="1":
                  saldo = float(input("Informe o saldo na sua conta:\n"))
             saldo_restante = saldo - valor
             if saldo >= valor:
                    print ("Acesso Liberado!")
                    print("Pagamento realizado")
                    print(f"Saldo restante:R${saldo_restante:.2f}")
                    continue

             else:
                    print("Saldo Insuficiente")

             if forma_pagamento =="2":
                saldo = float(input("Informe o saldo na sua conta:\n"))
                saldo_restante = saldo - valor
                if saldo >= valor:
                    print ("Acesso Liberado!")
                    print("Pagamento realizado")
                    print(f"Saldo restante:R${saldo_restante:.2f}")
                    continue
                else:
                    print("Saldo Insuficiente")

    if opcao == "4":
        id_temp = input("Informe o seu ID provisório: ")
        valor = 50
        print("Cobrança fixa: R$ 50,00")
        print(f"Valor: {valor:.2f}")
        forma_pagamento = input("Informe a sua forma de pagamento\n1-Débito\n2-Pix\n")
        if forma_pagamento =="1":
                saldo = float(input("Informe o saldo na sua conta:\n"))
                saldo_restante = saldo - valor
                if saldo >= valor:
                    print ("Acesso Liberado!")
                    print("Pagamento realizado")
                    print(f"Saldo restante:R${saldo_restante:.2f}")
                    total_vagas = +1

                    continue

                else:
                    print("Saldo Insuficiente")

        if forma_pagamento =="2":
                saldo = float(input("Informe o saldo na sua conta:\n"))
                saldo_restante = saldo - valor
                if saldo >= valor:
                    print ("Acesso Liberado!")
                    print("Pagamento realizado")
                    print(f"Saldo restante:R${saldo_restante:.2f}")
                    total_vagas = +1

                    continue
                else:
                    print("Saldo Insuficiente")
        
    if opcao == "0":
         print("Encerrando sistema...")
    break