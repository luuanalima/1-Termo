# Tipos de dados 
# int
# float

x = 10
Y = 5.15
print ("10")
print ("5.15")

#Texto e String
print ("meu nome é luana")

#Concatenar
print ("eu gosto de programar \n' + ' \n Python \n")
print ("eu gosto de programar \n + Python")
print ("eu gosto de programar \n" + "Python")

#Contas
n1 = 10
n2 = 5
print ('Os valores são', n1 + n2)

#Operadores matematicos
# + = soma
# - = subtração
# * = multiplicação
# / = divisão
# ^ = expoente

#Exemplo 2
n1 = 20
n2 = 10
print('Os valores', n1 * n2)

#Exemplo 3
n2 = input("Digite o seu primeiro número: \n")
print('Seu primeiro foi: \n' , n2)

#Exemplo 4 
nome = input('Qual é seu nome? \n')
print('Seu nome é: \n' , nome) #Aqui ficaria mais completo
print(nome) #Aqui mais simples

#Exemplo 5
#Duas perguntas
# 1ª Qual é seu Curso?
# 1ª Qual é sua idade?

curso = input("Qual é seu curso? \n")
print("Seu curso é \n", curso)

idade = input("Qual é sua idade? \n")
print("Sua idade é: \n", idade)

#Exemplo 6
base = 10
altura = 5
area = (base * altura) /2
print(area)

#Exemplo 6B
#Com informações

base = int(input('informe o valor da base: \n'))
altura = float(input('informe o valor da altura: \n'))
area = (base * altura) /2
print ('Os seus cálculos são:', int(area))

#Exercício 1
#Criar uma calculadora com os operadores soma , subtrair

n1 = int(input("Digite o valor:"))
n2 = int(input("Informe o valor do segundo numero:"))
soma = n1 + n2
print("Resultado:" , n1 + n2)

n3= int(input("Informe o valor do terceiro numero:"))
n4 = int(input("Informe o valor do quarto numero:"))
subtração = n3 - n4
print("Resultado:" , n3 - n4)

#Exercicio 2
#Calculadora de IMC (Potencia e divisao)
#O indice de massa corporal (IMC) é calculado dividindo o peso pela altura ao quadrado (altura^25)

peso = int(input("Digite o peso:"))
altura = int(input("Digite a altura:"))
alturadocorpo = (altura * altura)
resultado = (peso / alturadocorpo)
print(resultado)

nome = input("digite seu nome")
idade = int(input("digite sua idade"))
prof = input("digite sua profissão")

print("seu nome é: ", nome, "e sua idade foi", idade, "e sua profissão foi", prof)
print("teste",nome + "ola" ,idade)


