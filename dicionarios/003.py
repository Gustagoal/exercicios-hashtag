"""Exercício 3: Análise de Faturamento por Região (Setor Financeiro) Dada a lista de 
faturamento por região: vendas_regiao = {"Norte": 15000, "Sul": 22000, 
"Leste": 18000, "Oeste": 25000}. Seu programa deve: 
1. Extrair todos os valores (faturamentos) para uma lista. 
2. Calcular e exibir o faturamento total da empresa (soma de todas as regiões). 
3. Calcular e exibir o faturamento médio das regiões."""

import numpy as np
import statistics

vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}

faturamento = list(vendas_regiao.values())
print(f"Faturamento total R$ {sum(vendas_regiao.values()):_.2f}")
print(f"Faturamento médio R$ {statistics.mean(faturamento):_.2f}")

