"""Exercício 3: Análise de Metas de Vendas (Setor Comercial) Um gerente quer comparar o 
desempenho de duas filiais. O programa deve: 
1. Pedir o faturamento da Loja A e o faturamento da Loja B (o usuário pode digitar 
números decimais). 
2. Calcular o faturamento total das duas lojas. 
3. Calcular a média de faturamento entre elas. 
4. Exibir uma única mensagem formatada informando o total e a média, utilizando o 
separador de milhar e duas casas decimais."""


import statistics
import numpy as np

loja_a = 1_500 # input("Digite o faturamento da loja A : ")
loja_b = 3_000 # input("Digite o faturamento da loja B : ")

total_faturamento = loja_a + loja_b

media = total_faturamento/2
media_np = np.mean([loja_a,loja_b])
media_statistics = statistics.mean([loja_a,loja_b])


print(f" Total R$ : {total_faturamento:,.2f}\n Media R$ : {media:,.2f}")
print(f"Com a biblioteca Numpy R$ {media_np:,.2f}")
print(f"Com a biblioteca statistics R$ {media_statistics:,.2f}")
