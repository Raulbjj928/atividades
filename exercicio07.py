# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
#  conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u. 


texto = input('digite a frase: ')
vogais = 0
espaco = 0
numero = 0

for letras_numero in texto:
    if letras_numero == texto:
        espaco +=1
    elif letras_numero in texto:
        vogais +=1
    elif letras_numero in texto:
        numero +=1
print(f'a frase tem {espaco}espaco,{vogais}vogais e {numero} numeros: ')
