# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto
# de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$

""" def calcular_pagamento(qtd_horas,valor_horas):
    valor = float(valor_horas)
    horas = float(qtd_horas)
    if horas <= 90:
        salario_total = horas*valo

 """
hora = float(input('trablha quatas horas por mês?'))
valor = float(input('ganha quanto por hora?'))

salario_total = hora * valor
desontoinss = salario_total *0.08
descontoir  = salario_total * 0.11
descontosindi = salario_total * 0.05

salarioliqui = salario_total - desontoinss - descontosindi - descontoir

print(f"""
Salário Bruto : {salario_total}R$   
IR (11%) : {descontoir}R$          
INSS (8%) : {desontoinss}R$        
Sindicato ( 5%) : {descontosindi}R$ 
Salário Liquido : {salarioliqui}R$  
""")

''' Uma coisa legal que da pra fazer com f-string é a formatação
de casas após o ponto ,ex: #{salario_total:.2f} assim indica que você quer 2 
casas após o ponto.a saida ficaria assim : Salário Bruto : xxxx.xxR$ é só detalhe
no resto esta muito bom seu codigo broo parabens!'''

