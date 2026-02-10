"""Exercício 1: Dashboard de Vendas (Análise de Dados) Você recebeu uma lista com as 
vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200]. Crie um 
programa que exiba um pequeno relatório contendo: 
1. O total de vendas na semana. 
2. A média de vendas diária. 
3. O valor da melhor venda e da pior venda do período."""

import statistics

vendas = [1500, 2000, 800, 3500, 1200]

print(f"Total de vendas por semana : {sum(vendas)}")
print(f"Média de vendas diária :  {statistics.mean(vendas)}")
print(f"O valor da melhor venda {max(vendas)}")
print(f"O valor da pior venda {min(vendas)}")

