"""Exercício 4: Análise de Metas Combinadas (Setor Comercial) Uma empresa paga bônus 
se a meta individual do vendedor E a meta da loja forem batidas. 
1. Peça as vendas do vendedor e a meta individual dele. 
2. Peça as vendas totais da loja e a meta da loja. 
3. Se o vendedor bater a meta dele E a loja bater a meta total, o bônus é de 20% sobre 
as vendas do vendedor. 
4. Caso contrário, o bônus é zero. Exiba a mensagem: "Seu bônus este mês é de: 
R$[valor]". """


vendas_vendedor = 40_000
meta_vendedor = 30_000

vendas_totais_loja = 50_000
meta_loja = 20_000

if vendas_vendedor >= meta_loja and vendas_totais_loja >= meta_loja:
    print(f"Parabéns seu bônus é de 20% \n Seu bônus este mês é de R$ {(vendas_vendedor*0.20)+vendas_vendedor:,.2f}")
else:
    print("Seu bônus é zero")






