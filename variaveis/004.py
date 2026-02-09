"""Exercício 4: Análise de Margem de Lucro (Financeiro) 
Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$ 
5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro 
líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana 
chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%)."""

faturamento = 15.000
imposto = 0.15
lucro = faturamento = 5_000
margem_lucro = (lucro/faturamento)
meta_atingida = 0.30

print(f"O faturamento é de R$ {faturamento}")
print(f"O imposto é de {imposto*100} % ")
print(f"O Lucro é de R$ {faturamento}")
print(f"O margem de lucro é de R$ {margem_lucro}")
print(f"A meta atingida é de {meta_atingida*100} % ")

