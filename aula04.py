#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     # print("falso")
#     # print("falso")
#     # print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2) 

# x= 5

# if x > 10:
#     print("verdade")
# else: 
#     print("falso")

    #Crie um programa em Python que solicite a idade do usuário e informe se este e menor ou maior de idade. 

# print("#"*10, "IDADE", "#"*10)
# idade= int(input("Digite sua idade: "))

# if idade >= 18:
#     print("Maior de idade")
# else:
#     print("Menor de idade")

#DESAFIO: considere avaliar se a idade é válida, senod que não pode ser menor que zero ou maior que 120 anos

# print("#"*10, "LOGIN", "#"*10)
# idade= int(input("Digite sua idade: "))

# if idade == 0 or idade > 120: 
#     print("Idade inválida")
# else:
#     print("Idade Valida")

# email= (input("Digite seu email: "))
# senha= (input("Digite sua senha: "))

# if "python@senai.com" == email:
#     if "12345678" == senha:
#         print("USUARIO AUTENTICADO")
# else: 
#     print("Senha ou usuario invalidos")

# print("="*10, "SUPERMERCADO", "="*10)

# nome1 = input("digite o nome do produto:  ")
# valor1 = float(input("digite o valor desse produto:  "))
# desconto1= 0.25 * valor1

# nome2 = input("digite o nome do segundo produto:  ")
# valor2 = float(input("digite o valor do segundo produto:  "))

# print("#"*10, "CAIXA", "#"*10)

# desconto2= 0.25 * valor2

# print("O preço de", (nome1) ,"com 25% de desconto é", valor1-desconto1 )
# print(" O preço de", (nome2), "com 25% de desconto é", valor2-desconto2 )

#MAÇÃS

print("="*10, "MAÇÃS PALMEIRAS", "="*10)

quantidade = input("digite a quantidade de maçãs que deseja levar:  ")
valorf= quantidade
valor1= 0.30 * quantidade
valor2 = 0.25 * quantidade

if valorf >= 12 or valorf > 12: 
    print("TOTAL: " (valor1))
else:
    print("TOTAL: " (valor2)
          
        
qtd = int(input("Digite a qtd de maçãs que deseja levar: "))

if qtd < 12 :
    calc = qtd * 30
    print("Voce ira pagar (0.30 p unid.): R$")
else :
    calc = qtd * 0.25
    print("vc ira pagar (0.25 p unid.): R$ ")