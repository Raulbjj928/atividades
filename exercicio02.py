# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
# área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
# que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#  Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#  comprar apenas latas de 18 litros;
#  comprar apenas galões de 3,6 litros;
#  misturar latas e galões, de forma que o desperdício de tinta seja menor.
#  Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# 
def menu ():
    print("""
    1)digite o metros quadrados da area desejada:
    2)preços dos produtos: 
    3)calcular os preço: 
    """)
    opcao = input('digite a opçao desejada: ')
    while not 1 <= opcao <=3:
        print()
    else:
        return opcao


while loop:
    entrada = menu(1)
    if entrada ==  1:
        area = eval(input('digite o metros quadrado da area desejada: '))
        litros = float(area/6)
        litrosr = math.ceil(float(litros*1.1))
        latas


