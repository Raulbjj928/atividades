# Faça um programa que gera uma lista dos números primos existentes entre 1 e 
# um número inteiro informado pelo usuário. 

num = int(input("Digite um numero"))
if num :
    for i in range(3, num // 2, 2):
        if num % i == 0:
            print('não é primo')
            break 
    else:
        print('é primo')