"""Exercício 4: Sistema de RH – Média de Desempenho (Setor de RH) O RH armazena as 
últimas 3 notas de desempenho de cada funcionário em um dicionário: desempenho = 
{"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}. O gestor 
quer saber a média da funcionária "Paula". Crie um código que: 
1. Acesse a lista de notas da "Paula". 
2. Calcule a média das notas (soma das notas dividida pela quantidade de notas). 
3. Exiba o resultado: "A média de Paula foi [media]"."""

import statistics

desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}

funcionaria = desempenho["Paula"]

print(desempenho.keys())
media = statistics.mean(funcionaria)
print(f"Média de notas da funcionaria {media:.2f}")