import os
os.system("cls")
os.system("color 5")

#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


if x <=20:
    print("entrou no if 14")
elif x<=15:
    print("entrou no if 15")
elif x <=16:
    print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA

# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

# input(print("digite sua nota: "))

# n1 = float(input("digite sua primeira nota: "))
# n2 = float(input("digite sua segunda nota: "))
# media= (n1 + n2) /2



# print(f"sua media é: {media:.f}")
# #:.f -> formata para duas casas decimais APENAS NO FSTRING 

# if media < 5: 
#     print("REPROVADO")

# elif media <7.0 :
#     print("EM RECUPERAÇÃO")

# # elif media > 7:
# else:
#     print("APROVADO")

# print("*"*10,"IMC CALCULADORA","*"*10)

# peso = float(input("informe o seu peso: "))
# altura = float(input("Informe a sua altura: "))
# # imc = round((peso/altura)*altura)
# imc = round(peso/(altura*altura))

# print(f"Seu IMC é: {imc}")

# if imc <17:
#     print("MUITO abaixo do peso")

# elif imc >=17 and imc <18.49 :
#     print("ABAIXO do peso")

# elif imc >=18.5 and imc <24.99:
#     print("peso normal")

# elif imc >= 25 and imc <29.99: 
#     print("ACIMA do peso")

# elif imc >=30 and imc < 34.99:
#     print("Obesidade I")

# elif imc >=35 and imc < 39.99:
#     print("Obesidade II")

# else:
#     print("Obesidade III")

# print("*"*10,"REAJUSTE AUTOCAR","*"*10)


# print(r"""
#   ________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______
# _____¶¶¶¶¶¶_¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____
# ____¶¶¶¶¶__¶¶¶¶¶_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___
# __¶¶¶¶¶___¶¶¶¶¶¶________________¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶_
# _¶¶¶¶¶___¶¶¶¶¶¶¶_________________¶¶¶¶¶¶¶¶¶___¶¶¶¶¶
# __¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________¶¶¶¶¶_
# ___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶___
# _____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶____
# ______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____
# ________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______
# _________¶¶¶¶¶___________________¶¶¶¶¶¶¶¶¶________
# ___________¶¶¶¶_¶¶¶¶¶¶¶____________¶¶¶¶¶__________
# ____________¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶_¶¶¶¶¶¶¶¶¶___________
# ______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________
# _______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________
# ________________¶¶¶¶¶___¶¶¶__¶¶¶¶¶________________
# __________________¶¶¶¶¶_____¶¶¶¶¶_________________
# ___________________¶¶¶¶¶___¶¶¶¶¶__________________
# _____________________¶¶¶¶¶¶¶¶¶____________________
# ______________________¶¶¶¶¶¶¶_____________________
# ________________________¶¶¶_______________________            
       
      
# """)

# print("TABELA DE REAJUSTES DE SALARIO")
# print("Salários até R$ 2799,99 :aumento de 20%")
# print("Salários entre R$ 2800,00 e R$6999,99: aumento de 15%")
# print("Salários entre R$ 7000,00 e R$ 14999,99: aumento de 10%")
# print("Salários de R$ 15000,00 em diante: aumento de 5%")


# salario = float(input("informe o seu salário: "))

# if salario < 2799.99:
#     a1= 0.20 * salario
#     print("Você recebeu um aumento de:", 0.20 * salario ) 
#     print(f"O seu salario antes do aumento era de: {salario}") 
#     print("Você recebeu um amento de 20%")
#     print(f"Seu novo salario é {a1}") 

# elif salario >=2800.00 and salario <6999.99:
#     a2= 0.15 * salario 
#     print("Você recebeu um aumento de:", 0.15 * salario )
#     print(f"O seu salario antes do aumento era de: {salario}") 
#     print("Você recebeu um amento de 15%")
#     print(f"Seu novo salario é {a2}")

# elif salario >=7000.00 and salario <14999.99 :
#     a3= 0.10* salario 
#     print("Você recebeu um aumento de:", 0.10 * salario )
#     print(f"O seu salario antes do aumento era de: {salario}") 
#     print("Você recebeu um amento de 10%")
#     print(f"Seu novo salario é {a3}")

# elif salario >=15000.00:
#     a3= 0.5 * salario
#     print("Você recebeu um aumento de: ", 0.5 * salario)
#     print(f"O seu salario antes do aumento era de: {salario}") 
#     print("Você recebeu um amento de 5%")
#     print(f"Seu novo salario é {a3}")


# print("*"*10,"ATIVIDADE PARTE DOIS","*"*10)

# print(f"O seu salário era de: {salario}")

# if a0:
#     print("Você recebeu um aumento de 20%")

# elif a1:
#     print("Você recebeu um aumento de 15%")
# # elif a2:
# #     print("Você recebeu um aumento de 10%")
# # elif a3:
# #     print("Você recebeu um aumento de 5%")




    