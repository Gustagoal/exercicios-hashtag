"""Exercício 2: Calculadora de Imposto Sobre Serviço - ISS (Setor Fiscal) Crie uma função 
chamada calcular_iss que receba o valor de um serviço. 
● Se o valor for maior que R$ 5.000,00, a taxa é de 5%. 
● Caso contrário, a taxa é de 3%. A função deve retornar o valor do imposto (e não o 
valor total). Depois, use essa função para calcular o imposto de uma nota de R$ 
8.000,00 e outra de R$ 2.000,00, exibindo os resultados."""


def calcular_iss(iss):
    if iss >5_000:
        return iss*0.05
    else:
        return iss*0.03


valor = calcular_iss(8_000)
valor2 = calcular_iss(2_000)


print(f"O valor da aliquota é de 5 % acima de R$ 5,000 , valor do imposto : R$ {valor:,.2f}")
print(f"O valor da aliquota é de 3 % acima de R$ 2,000 , valor do imposto : R$ {valor2:,.2f}")
