import tkinter as tk
from tkinter import messagebox

# 1. Configurar evento

def solicitar_informacoes():
    # .get() serve para buscar o texto que foi digitado
    nome_usuario = campo_nome.get()
    idade_usuario = idade_nome.get()

    if nome_usuario == "":
        messagebox.showwarning("Aviso", "Por favor, digite seu nome e idade :)")

    else:
        messagebox.showinfo("Saudações querido aluno", f"Olá, {nome_usuario}, você tem {idade_usuario} anos, Seja bem vindo ao mundo das interfaces gráficas.")
        

# 2. Configuração de janela
app = tk.Tk()
app.title("Tela de usuário")
app.geometry("300x300")

# 3. Componentes (widgets)
lbl_nom_usuario = tk.Label(app, text="Digite seu nome :) ").grid(row=1, column=0, padx=10, pady=10) #grid - posicionamento em grade
# lbl_nom_usuario.pack(pady=10)

lbl_idade_usuario = tk.Label(app, text="Digite sua idade :) ")
# lbl_idade_usuario.pack(pady=10)

campo_nome = tk.Entry(app, font=("Arial", 12))
campo_nome.grid(row=1, column=0, padx=10, pady=5)

idade_nome = tk.Entry(app, font=("Arial", 12))
idade_nome.grid(row=1, column=0, padx=10, pady=5)

btn_cadastrar = tk.Button(app, text="Cadastrar", command=solicitar_informacoes)
btn_cadastrar.grid(row=1, column=0, padx=10, pady=5)

# 4. Rodar interface
app.mainloop()