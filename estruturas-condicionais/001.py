"""Exercício 1: Validação de Investimento (Setor Financeiro) Uma corretora de valores 
quer automatizar a recomendação básica de perfil. Crie um programa que peça ao usuário o 
valor que ele deseja investir. 
1. Se o valor for menor que R$ 1.000,00, exiba: "Perfil iniciante: Sugerimos Tesouro 
Direto". 
2. Se o valor for entre R$ 1.000,00 e R$ 5.000,00 (inclusive), exiba: "Perfil moderado: 
Sugerimos Fundos Imobiliários". 
3. Se o valor for acima de R$ 5.000,00, exiba: "Perfil arrojado: Sugerimos Ações". 
*Lembre-se de tratar o input caso o usuário digite "R$" ou use vírgula."""


valor_investimento  = float(input("Digite o valor que deseja investir R$ : "))

if valor_investimento < 1_000:
    print(f"Valor do investimento R$ : {valor_investimento:,.2f}")
    print("Perfil iniciante: Sugerimos Tesouro Direto")
if valor_investimento >= 1_000 <= 5_000:
    print(f"Valor do investimento R$ : {valor_investimento:,.2f}")
    print("Perfil moderado : Sugerimos fundos imobiliários")
if valor_investimento >5_000:
    print(f"Valor do investimento R$ : {valor_investimento:,.2f}")
    print("Perfil arrojado: Sugerimos Ações")