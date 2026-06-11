# Revisão Tkinter

#Biblioteca
import tkinter as tk
from tkinter import messagebox, ttk

#DEF - Linha de bloco de função
def cadastrar_usuario():
    #.get em todos os componentes que irão receber informação
    
    nome_usuario = ent_nome_usuario.get()
    nome_escola = cmb_nome_escola.get()
    
    if nome_usuario == "" and nome_escola == "":
        messagebox.showwarning("Verificar Dados", "Verificar os campos")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá usuário {nome_usuario} sua escola cadastrada é {nome_escola}")

# 0 Etapas - Janela 
janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("500x500")
# janela.configure(bg="red")

# 1 - Etapa - Componentes
# Labels = Rotulos e Textos antigo print
lbl_titulo_aplicacao = tk.Label(janela, text="Revisão Tkinter :)", font=("Arial", 14), fg="black", bg="white")
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

lbl_nome_usuario = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12), fg="black", bg="red")
lbl_nome_usuario.grid(row=1,column=0, pady=20, padx=20)

lbl_nome_escola = tk.Label(janela, text="Escolha sua Escola:", font=("Arial", 12))
lbl_nome_escola.grid(row=2, column=0, pady=10, padx=10)

# Entrys = Caixa de texto ou antigo input
ent_nome_usuario = tk.Entry(janela, font=("Arial", 14), fg="black", width=20)
ent_nome_usuario.grid(row=1, column=1, pady=10, padx=10)

# Caixa de seleção ou combobox
cmb_nome_escola = ttk.Combobox(janela, values=["SESI5", "SESI408"], state="readonly",width=20)
cmb_nome_escola.grid(row=2, column=1, pady=10, padx=10)

#Botões 
btn_enviar_dados = tk.Button(janela, text="Cadastrar Usuário", width=30, command=cadastrar_usuario)
btn_enviar_dados.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", width=30, command=janela.destroy) 
btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)



# 4 Etapa - Mainloop
janela.mainloop()