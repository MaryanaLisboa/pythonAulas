import os
os.system("cls")
os.system("color 5")

#Continuação INPUT com INT e FLOAT 

#int() -> converte para inteiro
#float() -> converte para n quebrado

#type serve para retornar o tipo da variavel

# #EXEMPLO 1
# numero = 10
# numero2= input("digite um numero:")
# print("o tipo de numero é,", type(numero2))
# soma = numero + int(numero2)
# print(f"soma de {numero} + {numero} =", soma)

# # #EXEMPLO 2
# num1= input("digite um numero: ")
# soma=float (num1) + 15
# print("A soma de ", num1 , "+", "15" , "=", soma)

# #float -> numero quebrado

# #EXEMPLO 3
# n1 = float(input ("digite um numero: "))
# n2 = float(input ("digite outro numero: "))

# soma= n1+n2

# print(f"a soma de {n1} = {n2} =", soma)

#ATIVIDADE 1
# n1 = float (input ("digite um numero: "))
# n2= float (input ("Digite outro numero: "))

# multi= n1*n2
# print(f"A multiplicação de {n1} = {n2} =", multi)

#ATV 2

# num1= input("digite um numero: ")
# antecessor= float (num1) -1
# sucessor= float (num1) +1
# print(f"O antecessor de {num1}, =",antecessor)
# print(f"O sucessor de {num1}, =",sucessor)


# #ATV 3
# ano= 2025
# idade= input ("digite sua data de nascimento: ")
# conta =ano - int(idade) 
# print("sua idade é,", conta)

#                      PORCENTAGEM

# print("25% de 100 = ", 0.25 * 100 )
# print("4% de 400 =", 0.04 * 400)
# print("99% de 1525= " 0.99% * 1525)

# exemplo = float(input("digite o preco do produto: "))
# desconto = 0.15 * exemplo 
# print(" O preço do produto com 15% de desconto é", exemplo-desconto )

#             ATIVIDADE 1

print("="*10, "SUPERMERCADO", "="*10)

nome1 = input("digite o nome do produto:  ")
valor1 = float(input("digite o valor desse produto:  "))
desconto1= 0.25 * valor1

nome2 = input("digite o nome do segundo produto:  ")
valor2 = float(input("digite o valor do segundo produto:  "))

print("#"*10, "CAIXA", "#"*10)

desconto2= 0.25 * valor2

print("O preço de", (nome1) ,"com 25% de desconto é", valor1-desconto1 )
print(" O preço de", (nome2), "com 25% de desconto é", valor2-desconto2 )

# total1= round(valor1-desconto1)
# total2= round(valor2-desconto2)

# final= total1+total2

total= (valor1-desconto1)+(valor2-desconto2)

print("O preço total é", (total))




