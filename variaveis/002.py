"""Exercício 2: Controle de Estoque de E-commerce (Logística) 
Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no 
estoque. Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um 
fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo final."""

estoque = 250 

entradas = 100
saidas = 78

estoque_atual = estoque + entradas - saidas

print(f"Estoque inicial : {estoque}")
print(f"Entrada : {entradas}")
print(f"Saida: {saidas}")
print(f"Estoque final {estoque_atual}")




