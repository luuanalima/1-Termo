# Exercício
# Crie uma aplicação que pergunte o nome e o ano de nascimento do usuário
# Calcule a idade

import tkinter as tk
from tkinter import messagebox, ttk

def calcular_idade():
    nome_usuario = ent_nome_usuario.get()
    ano_nascimento = ent_ano_nascimento.get()
    
    if nome_usuario == "" and ano_nascimento == "":
        messagebox.showwarning("Atenção", "Preencha os dados corretamente!")
    else:
        idade = 2026 - int(ano_nascimento)
        messagebox.showinfo("Resultado", f"Olá {nome_usuario}, sua idade é {idade}")
        
        
janela = tk.Tk()
janela.title("Cadastro de usuário:")
janela.geometry("500x500")
lbl_nome_usuario = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12), fg="black", bg="white")
lbl_nome_usuario.grid(row=0, column=0, pady=20, padx=20)

lbl_idade_usuario = tk.Label(janela, text="Digite seu ano de nascimento:", font=("Arial", 12))
lbl_idade_usuario.grid(row=2, column=0, pady=10, padx=10)

ent_nome_usuario = tk.Entry(janela, font=("Arial", 12), fg="black", width=20)
ent_nome_usuario.grid(row=0, column=1, pady=20, padx=20)

ent_ano_nascimento = tk.Entry(janela, font=("Arial", 12))
ent_ano_nascimento.grid(row=2, column=1, pady=10, padx=10)

btn_enviar_dados = tk.Button(janela, text="Cadastrar Usuário", bg="black", fg="white", width=30, command=calcular_idade)
btn_enviar_dados.grid(row=3, column=0, pady=10, padx=10)


janela.mainloop()