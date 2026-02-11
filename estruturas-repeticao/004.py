"""Exercício 4: Análise de Custos Mensais (Setor Financeiro) Você tem dois dicionários: 
um com a meta de gastos de cada mês e outro com os gastos reais. metas = {"jan": 
1000, "fev": 1200, "mar": 1100} gastos = {"jan": 900, "fev": 1350, 
"mar": 1100} Crie um loop que percorra os meses e informe para cada mês: 
● Se o gasto foi menor ou igual à meta: "Mês [mês]: Dentro do orçamento." 
● Se o gasto ultrapassou a meta: "Mês [mês]: Orçamento estourado em R$[valor da 
diferença]."""

metas = {"jan": 1000, "fev": 1200, "mar": 1100}
gastos = {"jan": 900, "fev": 1350, "mar": 1100}

for meta,gasto in metas.items(),gastos.items() : 
    print(meta,gasto)
    