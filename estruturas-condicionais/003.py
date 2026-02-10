"""Exercício 3: Cálculo de Desconto Progressivo (Setor de Vendas) Um e-commerce 
aplica descontos automáticos no carrinho. Crie um programa que receba o valor total da 
compra e aplique a seguinte lógica: 
● Compras a partir de R$ 500,00: 15% de desconto. 
● Compras a partir de R$ 200,00 (e menos de 500): 10% de desconto. 
● Compras abaixo de R$ 200,00: Sem desconto. O programa deve exibir o valor do 
desconto e o valor final a pagar, formatados em R$."""


valor_compra = 5_00

if valor_compra>500:
    desconto = 0.15 * valor_compra
    print(f" O valor do desconto é R$ {desconto:,.2}\n Valor final R$ : {valor_compra-desconto:,.2f} ")
elif 200 <= valor_compra >= 500:
    desconto = 0.10 * valor_compra
    print(f" O valor do desconto é R$ {desconto:,.2f}\n Valor final R$ : {valor_compra-desconto:,.2} ")
elif valor_compra<200:
    desconto = 0.0 * valor_compra
    print(f" O valor esta abaixo , o desconto é R$ {desconto}\n Valor final R$ : {valor_compra-desconto:.2f} ")