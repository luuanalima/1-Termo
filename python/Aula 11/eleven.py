# Tkinter

#Componentes principais
# tk: a janela
# Label: texto em rotulo
# Button: um botão de clique
# Entry: um campo de entrada de texto

#Biblioteca
import tkinter as tk
from tkinter import messagebox

# 1. Criar janela principal 
janela = tk.Tk()
janela.configure(bg="#586d77")
janela.title("Minha Primeira Janela em GUI")
janela.geometry("400x200") #largura e altura

# 2. Criar função que o botão vai executar (evento)
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão! :)")

# 3. Criar componentes (widgets)
lbl_titulo = tk.Label(janela, text="Bem-vindo a aula de Tkinter!", font=("Arial", 14, "bold"), bg="#9513d1")
btn_clique = tk.Button(janela, text="Clique Aqui :)", font=("Arial", 14), bg="#c715b8", fg="white", command=mostrar_mensagem)

# 4. Posicionar componentes
lbl_titulo.pack(padx=60)
btn_clique.pack(pady=50) 
#pady: posicionar vertical 
# #padx: posicionar horizontal

# 5. Rodar o loop da interface
janela.mainloop()