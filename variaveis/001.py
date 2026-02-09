"""Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas) 
Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a 
equipe de vendas. Objetivo: Calcule o valor do bônus e o faturamento final da empresa 
após subtrair esse bônus. 
● Faturamento inicial: 50.000 
● Percentual de bônus: 0.10 """


faturamento = 50_000

bonus = 0.10

valor_do_bonus  = (faturamento * bonus)
faturamento_final = faturamento + valor_do_bonus

print(f'Valor de faturamento R$ {faturamento:.2f}')

print(f"O valor do bonus é R$ {valor_do_bonus:.2f}")
print(f"O valor final de faturamento é R$ {faturamento_final:.2f}")



