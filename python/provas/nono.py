#Incorreto:
# 1. O Problema da Idade
# idade = input("Digite sua idade:")
# if idade >= 18:
#     print("Você é maior de idade.")

#Correto:
# 1. O Problema da Idade
# idade = int(input("Digite sua idade:"))
# if idade >= 18:
#     print("Você é maior idade.")

# Incorreto:
# 2. A Escrita Fiel
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

#Correto:
# 2. A Escrita Fiel
# nome = "Mariana"
# print(f"Seja bem vinda,{nome}!")

#Incorreto:
# 3. Falta de Espaço
# numero = 10
# if numero > 5:
#     print("O número é menor ou igual a cinco.")
# else:
# print("O número é menor ou igual a cinco.")

#Correto:
# 3. Falta de Espaço
# numero = 10
# if numero >= 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

#Incorreto:
# 4. Esquecimento Fatal
# usuario = "aluno123"
# if usuario == "aluno123"
#     print("Login realizado com sucesso.")

#Correto:
#4. Esquecimento Fatal
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso.")

#Incorreto:
#5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
#     print("Leve um guarda-chuva!")

#Correto:
# 5. Atribuição vs. Comparação
# clima = input("Como está o clima hoje? (ensolarado/chuvoso): ")
# if clima == "chuvoso":
#    print("Leve um guarda-chuva.")
# else:
#    print("Aproveite o dia ensolarado!")

#Incorreto:
# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez" +pontos+ "pontos.")

#Correto:
# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print(f"Parabéns! Você fez", pontos, "pontos.")

#Incorreto:
# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")

#Correto:
# 7. A Ordem dos Fatores
# nota = 9.5
# if nota <= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")

#Incorreto:
# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
#     print(i)

#Correto:
# 8. O Contador de 1 a 5
# for i in range(6):
#     print(i)

#Incorreta:
# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
# O código deveria parar após 3 tentativas

#Correto:
# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas += 1

#Incorreto:
# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
#     senha = input("Digite a senha secreta:")
# print("Acesso concedido!")

#Correto:
# 10. A Senha Teimosa
# senha = ""
# while senha != "python123":
#     senha = input("Digite a senha secreta: ")
# print("Acesso concedido.")