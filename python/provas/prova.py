# # 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# # "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox

# def registrar_operador():
#    nome_operador = ent_nome_operador.get()
#    turno_operador = ent_turno_operador.get()
   
#    if nome_operador == "" or turno_operador == "":
#        messagebox.showwarning("Atenção", "Preencha os dados corretamente!")
       
#    else:
#        messagebox.showinfo("Bem vindo!", f"Operador {nome_operador} registrado no Turno {turno_operador}. Boa jornada!")
        
# janela = tk.Tk()
# janela.title("Registro de operador")
# janela.geometry("500x500")
# lbl_nome_operador = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12), fg="black", bg="white")
# lbl_nome_operador.grid(row=0, column=0, pady= 20, padx=20)
# ent_nome_operador = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_nome_operador.grid(row=0, column=1, pady=20, padx=20)

# lbl_turno_operador = tk.Label(janela, text= "Digite seu turno ( A, B ou C):", font=("Arial", 12))
# lbl_turno_operador.grid(row=2, column=0, pady=10, padx=10)
# ent_turno_operador = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_turno_operador.grid(row=2, column=1, pady=10, padx=10)

# btn_registrar_operador = tk.Button(janela, text="Registrar operador",  bg="black", fg="white", width=30, command=registrar_operador)
# btn_registrar_operador.grid(row=3, column=0, pady=10, padx=10)
# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", width=30, command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)

# janela.mainloop()


# # 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# # exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# def calculo_producao():
#     quantidade_pecas = ent_quantidade_pecas.get()
    
#     if quantidade_pecas == "":
#         messagebox.showwarning("Atenção", "Preencha os dados corretamente!")
        
#     else:
#         total_pecas = int(quantidade_pecas) * 8
#         messagebox.showinfo("Calculo de produção realizado!", f"Em 8 horas foram produzidas {total_pecas} peças.")
        
# janela = tk.Tk()
# janela.title("Calculo de produção:")
# janela.geometry("1200x600")
# lbl_quantidade_pecas = tk.Label(janela, text= "Digite quantas peças foram produzidas em 1 hora:", font=("Arial", 12), fg="black", bg="white")
# lbl_quantidade_pecas.grid(row=0, column=0, pady=20, padx=20)
# ent_quantidade_pecas = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_quantidade_pecas.grid(row=0, column=1, pady=20, padx=20)

# btn_calculo_producao = tk.Button(janela, text="Calcular produção", bg="black", fg="white", width=30, command= calculo_producao)
# btn_calculo_producao.grid(row=3, column=0, pady=10, padx=10)
# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", width=30, command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)

# janela.mainloop()

# # 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# # ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# def conversor_bar():
#     conversor_unidade = ent_conversor_unidade.get()
    
#     if conversor_unidade == "":
#         messagebox.showwarning("Atenção", "Preencha os dados corretamente!")
    
#     else: 
#         total_conversor = float(conversor_unidade) * 14.5
#         messagebox.showinfo("Resultado da conversão", f" O valor convertido de {conversor_unidade} Bar para PSI é de: {round(total_conversor,2)} PSI.  ")
        
# janela = tk.Tk()
# janela.title("Conversor de unidade:")
# janela.geometry("500x500")
# lbl_conversor_unidade = tk.Label( text="Digite a pressão em bar:", font=("Arial", 12), fg="black", bg="white")
# lbl_conversor_unidade.grid(row=0, column=0, pady=20, padx=20)
# ent_conversor_unidade = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_conversor_unidade.grid(row=0, column=1, pady=20, padx=20)

# btn_conversao = tk.Button(janela, text="Converter para PSI.", bg="black", fg="white", width=30, command= conversor_bar)
# btn_conversao.grid(row=3, column=0, pady=10, padx=10)
# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", width=30, command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)

# janela.mainloop()

# # 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# # aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox

# def qualidade_media():
#     n1 = ent_n1.get()
#     n2 = ent_n2.get()
#     n3 = ent_n3.get()
    
#     if n1 == "" and n2 == "" and n3 == "":
#         messagebox.showwarning("Atenção", "Preencha os dados corretamente!")
        
#     else: 
#         total_qualidade = (float(n1) + float(n2) + float(n3)) / 3
#         messagebox.showinfo("Resultado da média aritmetica simples", f"A média de qualidade das peças é de {total_qualidade}.")
        
# janela = tk.Tk()
# janela.title("Calculador da média de qualidade:")
# janela.geometry("500x500")
# lbl_n1 = tk.Label(janela, text="Digite o valor do primeiro número:", font=("Arial", 12), fg="black", bg="white")
# lbl_n1.grid(row=0, column=0, pady=20, padx=20)
# ent_n1 = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_n1.grid(row=0, column=1, pady=20, padx=20)

# lbl_n2 = tk.Label(janela, text="Digite o valor do segundo número:", font=("Arial", 12), fg="black", bg="white")
# lbl_n2.grid(row=1, column=0, pady=20, padx=20)
# ent_n2 = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_n2.grid(row=1, column=1, pady=20, padx=20)

# lbl_n3 = tk.Label(janela, text="Digite o valor do terceiro número:", font=("Arial", 12), fg="black", bg="white")
# lbl_n3.grid(row=2, column=0, pady=20, padx=20)
# ent_n3 = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_n3.grid(row=2, column=1, pady=20, padx=20)

# btn_calculador = tk.Button(janela, text="Calcular média aritmética simples", bg="black", fg="white", width=30, command=qualidade_media)
# btn_calculador.grid(row=3, column=0, pady=10, padx=10)
# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", width=30, command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)

# janela.mainloop()

# # 5. Termostato Inteligente: Peça a temperatura de um motor.
# # ● Abaixo de 40°C: "Baixa carga".
# # ● Entre 40°C e 70°C: "Normal".
# # ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox


# def inteligente_termostato():
#     motor_temperatura = ent_motor_temperatura.get()
    
#     if motor_temperatura == "":
#         messagebox.showwarning("Atenção", "Preencha os dados corretamente!")
        
#     else: 
#         if float(motor_temperatura) < 40:
#             messagebox.showinfo("Termmostato inteligente", "Baixa carga.")
            
#         elif float(motor_temperatura) >=40 and float(motor_temperatura) <= 70:
#             messagebox.showinfo("Termostato inteligente", "Normal.")
            
#         else: 
#             messagebox.showinfo("Termostato inteligente", "ALERTA: Resfriamento Ativado!" )
            
# janela = tk.Tk()
# janela. title("Termostato Inteligente:")
# janela.geometry("500x500")
# lbl_motor_temperatura = tk.Label(janela, text="Qual a temperatura atual do motor?", font=("Arial", 12), fg="black", bg="white")
# lbl_motor_temperatura.grid(row=0, column=0, pady=20, padx=20)
# ent_motor_temperatura = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_motor_temperatura.grid(row=0, column=1, pady=20, padx=20)

# btn_motor = tk.Button(janela, text="Situação atual do motor", bg="black", fg="white", width=30, command=inteligente_termostato)
# btn_motor.grid(row=3, column=0, pady=10, padx=10)
# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", width=30, command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)

# janela.mainloop()

# # 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# # exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox

# def lote_classificador():
#     produto_codigo = ent_produto_codigo.get()
    
#     if produto_codigo == "":
#         messagebox.showwarning("Atenção", "Preencha os dados corretamente!")
        
#     else:
#         if produto_codigo == "A":
#             messagebox.showinfo("Classificador de lotes", "Seu lote é de alimentos.")
#         elif produto_codigo == "E":
#             messagebox.showinfo("Classificador de lotes", "Seu lote é de eletrônicos.")
#         else: 
#             messagebox.showinfo("Classificador de lotes", "Seu lote atual não foi reconhecido, tente novamente!")
            
# janela = tk.Tk()
# janela.title("Classificador de lotes:")
# janela.geometry("1200x600")
# lbl_produto_codigo = tk.Label(janela, text="Qual a letra inicial do código do seu produto? (A ou E)", font=("Arial", 12), fg="black", bg="white")
# lbl_produto_codigo.grid(row=0, column=0, pady=20, padx=20)
# ent_produto_codigo = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_produto_codigo.grid(row=0, column=1, pady=20, padx=20)

# btn_classificacao = tk.Button(janela, text="Classificar lote", bg="black", fg="white", width=30, command=lote_classificador)
# btn_classificacao.grid(row=3, column=0, pady=10, padx=10)

# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", width=30, command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)

# janela.mainloop()

# # 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# # botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# # iniciar.

# import tkinter as tk
# from tkinter import messagebox

# def operacao_seguranca():
#     porta_sensor = ent_porta_sensor.get()
#     emergencia_botao = ent_emergencia_botao.get()
    
#     if porta_sensor == "" and emergencia_botao == "":
#         messagebox.showwarning("Atenção", "Preencha os dados corretamente!")
        
#     else:
#         if porta_sensor == "fechada" and emergencia_botao == "desligado":
#             messagebox.showinfo("Segurança de operação", "A máquina pode iniciar!")
#         else:
#             messagebox.showinfo("Segurança de operação", "A máquina não pode inicar, verifique tudo novamente.")
            
# janela = tk.Tk()
# janela.title("Segurança de operação:")
# janela.geometry("500x500")
# lbl_porta_sensor = tk.Label(janela, text=" A porta esta fechada ou aberta?", font=("Arial", 12), fg="black", bg="white")
# lbl_porta_sensor.grid(row=0, column=0, pady=20, padx=20)
# ent_porta_sensor = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_porta_sensor.grid(row=0, column=1, pady=20, padx=20)

# lbl_emergencia_botao = tk.Label(janela, text="O botão está ligado ou desligado?", font=("Arial", 12))
# lbl_emergencia_botao.grid(row=2, column=0, pady=10, padx=10)
# ent_emergencia_botao = tk.Entry(janela, font=("Arial", 12))
# ent_emergencia_botao.grid(row=2, column=1, pady=10, padx=10)

# btn_seguranca = tk.Button(janela, text="Verificar se a máquina pode iniciar", bg="black", fg="white", width=30, command=operacao_seguranca)
# btn_seguranca.grid(row=3, column=0, pady=10, padx=10)

# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", width=30, command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)

# janela.mainloop()

# # 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# # o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# # "Processo Otimizado".

# import tkinter as tk
# from tkinter import messagebox

# def descarte_calculo():
#     pecas_total = ent_pecas_total.get()
#     defeituosas_total = ent_defeituosas_total.get()
    
#     if pecas_total == "" and defeituosas_total == "":
#         messagebox.showwarning("Atenção", "Preencha os dados corretamente!")
        
#     else: 
#         descarte_porcentagem = (float(defeituosas_total) / float(pecas_total) * 100 )
#         if descarte_porcentagem > 5:
#             messagebox.showinfo("Cálculo de descarte", "O descarte foI maior que 5% do total, revise o processo")
#         else:
#             messagebox.showinfo("Cálculo de descarte", " o descarte foi menor que 5% do total, processo otimizado")
            
# janela = tk.Tk()
# janela.title("Cálculo de descarte:")
# janela.geometry("500x500")
# lbl_pecas_total = tk.Label(janela, text="Digite o total de peças produzidas:", font=("Arial", 12), fg="black", bg="white")
# lbl_pecas_total.grid(row=0, column=0, pady=20, padx=20)
# ent_pecas_total = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_pecas_total.grid(row=0, column=1, pady=20, padx=20)

# lbl_defeituosas_total = tk.Label(janela, text="Digite o total de peças defeituosas:", font=("Arial", 12))
# lbl_defeituosas_total.grid(row=2, column=0, pady=10, padx=10)
# ent_defeituosas_total = tk.Entry(janela, font=("Arial", 12))
# ent_defeituosas_total.grid(row=2, column=1, pady=10, padx=10)

# btn_calculo = tk.Button(janela, text="Calcular peças", bg="black", fg="white", width=30, command=descarte_calculo)
# btn_calculo.grid(row=3, column=0, pady=10, padx=10)

# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", width=30, command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)

# janela.mainloop()

# # 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# # diga se está dentro da tolerância, acima ou abaixo.

# import tkinter as tk
# from tkinter import messagebox

# def medida_validacao():
#     peca_medida = ent_peca_medida.get()
    
#     if peca_medida == "":
#         messagebox.showwarning("Atenção", "Preencha os dados corretamente!")
#     else:
#         if float (peca_medida) < 9.8:
#             messagebox.showinfo("Validação de medida", "A peça está abaixo da tolerância.")
#         elif float(peca_medida) >= 9.8 and float(peca_medida) <= 10.2:
#             messagebox.showinfo("Validação de medida", "A peça está dentro da tolerância.")
#         else:
#             messagebox.showinfo("Validação de medida", "A peça está acima da tolerância.")
            

# janela = tk.Tk()
# janela.title("Validação de medida:")
# janela.geometry("500x500")
# lbl_peca_medida = tk.Label(janela, text="Qual é a medida da peça?", font=("Arial", 12), fg="black", bg="white")
# lbl_peca_medida.grid(row=0, column=0, pady=20, padx=20)
# ent_peca_medida = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
# ent_peca_medida.grid(row=0, column=1, pady=20, padx=20)

# btn_valida = tk.Button(janela, text="Calcular", bg="black", fg="white", width=30, command=medida_validacao)
# btn_valida.grid(row=3, column=0, pady=10, padx=10)

# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", width=30, command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)

# janela.mainloop()

# # 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# # de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".


import tkinter as tk
from tkinter import messagebox

def contagem():
    
    for i in range(10, 0, -1):
        messagebox.showinfo("Contagem", f"Prensa será ativada em: {i}")
        
janela = tk.Tk()
janela.title("Contagem")
janela.geometry("500x500")
        
btn_contagem = tk.Button(janela, text="Contagem", bg="black", fg="white", width=30, command=contagem)
btn_contagem.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", width=30, command=janela.destroy) 
btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)


janela.mainloop()