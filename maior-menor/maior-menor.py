"""
Faça um programa que pergunte 2 números e fala qual é o maior e o menor
"""

num1 = input("Me fale um número: ")
num2 = input("Me fale outro número: ")

if num1 > num2:
    print(f"O número {num1} é maior que o {num2}")
elif num2 > num1:
    print(f"O número {num2} é maior que o {num1}")     
else: 
    print(f"O número {num1} e {num2} são iguais")