"""Exercício 4: Performance de Vendas Regionais (Setor de Dashboard) Crie uma função 
chamada analisar_vendas que receba uma lista de números (vendas). A função deve 
retornar o total vendido e a média das vendas. Dado o dicionário dados_filiais = 
{"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}: 
1. Percorra o dicionário. 
2. Para cada filial, use a função e faça o unpacking do resultado. 
3. Exiba: "Filial [Nome] -> Total: R$[valor], Média: R$[valor]"."""

import statistics

def analisar_vendas(**vendas):
    total_vendido = sum(vendas)
    media_vendida = statistics.mean(vendas)
    return total_vendido,media_vendida

dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}

print(f"Filial {analisar_vendas(dados_filiais)} -> Total : R$ {analisar_vendas(dados_filiais)} , Média : R${analisar_vendas(dados_filiais)}")

