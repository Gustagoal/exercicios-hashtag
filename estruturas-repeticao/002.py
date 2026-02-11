"""Exercício 2: Cálculo de Comissão Progressiva (Setor de Vendas) Você tem uma lista de 
vendas de um vendedor: vendas = [2000, 5000, 1000, 8000, 3000]. A regra de 
comissão é: 
● Vendas acima de R$ 4.000,00: comissão de 10%. 
● Vendas até R$ 4.000,00: comissão de 5%. Crie um programa que percorra a lista e, 
ao final, exiba o valor total que o vendedor receberá de comissão."""


vendas = [2000, 5000, 1000, 8000, 3000]

for venda in vendas:
    if venda >4_000:
        bonus = 0.10
    else:
        bonus = 0.05
    print(print(f"Venda R$ : {venda:,.2f} \n Bônus R$ : {bonus*100:,.2f} % \n Venda + bônus R$ : {(bonus*venda)+venda:,.2f}"))
