import os
os.system("cls")

#estruturas condicionais if else (ELIF)
#
#SWITH CASE -> (match case) escolha o caso (a partir da versão 3.10)
#macth valor:
#   case valor:

# linguagem = 10

# match linguagem:

#     case "pynthon":
#         print("é fácil")
#     case "java":
#         print("muito codigo, python faz com linhas menores")
#     case "c#":
#         print("massa")
#     case "js":
#             print("sou do back")
#     case "html":
#             print("kaua nao dorme")
#     case 10:
#         print("entrou aqui")
#     case _ :
#         print("outro caso")


# dia= int(input("Digite o dia da semana: "))
 
# match dia: 

#     case 1:
#         print("SEGUNDA-FEIRA")
#     case 2:
#         print("TERÇA-FEIRA")
#     case 3:
#         print("QUARTA-FEIRA")
#     case 4:
#         print("QUINTA-FEIRA")
#     case 5:
#         print("SEXTA-FEIRA")
#     case 6:
#         print("SÁBADO")
#     case 7:
#         print("DOMINGO")
#     case_:


# print("*************MUNDO CELULAR*************")
# print("""
      
# 1- IPHONE 15 - R$ 5000.00
# 2- XIAOMI REDI 13 - R$ 2500.00
# 3- SAMSUNG S25 - R$ 6999.99
      
# FRETE: SP- 10.00
#       MG- 15.00
#       RS- 20.00

# """)

# n= int(input("DIGITE O NÚMERO DO PRODUTO: "))
# e= int(input("DIGITE A SIGLA DO ESTADO: "))

# print("*******************************************************************************************")

# preco= 0
# frete= 0
# # produto_valido = True 
# # estado_invalido= False
# match n: 
#     case 1: 
#         preco = 5000.00
#     case 2: 
#         preco = 2500.00
#     case 3: 
#         preco = 6999.99
#     case _ :
#         print("Produto inválido!")
#         # produto_valido = False

# match e: 
#     case "RS" "rs": 
#             frete= 20
#     case "SP" "sp": 
#             frete = 10
#     case "MG" "mg": 
#             frete = 15
#     case _ :
#         print("Estado inválido!")
#         # estado_invalido= False

# # match (produto_valido, estado_invalido):
# #     case (True, True):
# #           total= preco + frete 
# #           print(f"Valor do celular: R$ {preco:.2f}")
# #           print(f"Valor do Frete R$ {frete:.2f}")
# #           print(f"Valor total R$ {total:.2f}")



# total = preco + frete 
# print(f"O valor do produto: R$ {preco:.2}")
# print(f"Valor do frete: R$ {frete:.2}")
# print(f"Valor total: R$ {total:.2}")
# print("produto invalido")

# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete:.2f}")

# import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")
import random 

o1= input("PEDRA, PAPEL OU TESOURA?: ")


match o1: 
    case _ if o1== "pedra":
        print("VOCÊ ESCOLHEU PEDRA")
    case _ if o1== "papel":
        print("VOCÊ ESCOLHEU PAPEL")
    case _ if o1== "tesoura":
        print("VOCÊ ESCOLHEU TESOURA")
    case _ :
        print("ERRO")

o2= 0
o2= random.randint(1,3)

match o2:
    case _ if o2 == 1:
        print("A MÁQUINA ESCOLHEU PEDRA")
    case _ if o2 == 2:
        print("A MÁQUINA ESCOLHEU PAPEL")
    case _ if o2 == 3:
        print("A MÁQUINA ESCOLHEU TESOURA") 

o3= 0
match o3: 
    case _ if o1 == "pedra" and o2 == 1: 
        print("EMPATE!")
    case _ if o1 == "papel" and o2 == 2: 
        print("EMPATE!")
    case _ if o1 == "tesoura" and o2 == 3:
        print("EMPATE!")

o4= 0
match o4:
    case _ if o1 == "pedra" and o2 == 2:
        print("VOCÊ PERDEU KKKK")
    case _ if o1 == "pedra" and o2 == 3:
        print("VOCÊ GANHOU")
    case _ if o1 == "papel" and o2 == 1:
        print("VOCÊ GANHOU")
    case _ if o1 == "papel" and o2 == 3:
        print("VOCÊ PERDEU KKKKK")
    case _ if o1 == "tesoura" and o2 == 2:
        print("VOCÊ GANHOU")
    case _ if o1 == "tesoura" and o2 == 1:
        print("VOCÊ PERDEU KKK")

