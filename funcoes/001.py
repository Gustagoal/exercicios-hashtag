"""Exercício 1: Padronizador de Nomes de Produtos (Setor de E-commerce) Muitas 
vezes, os nomes dos produtos entram no sistema de qualquer jeito (ex: "iPHonE 13", " 
macbook air "). Crie uma função chamada padronizar_texto que receba uma string 
como parâmetro e retorne esse texto sem espaços extras nas extremidades e com todas as 
palavras com a primeira letra maiúscula (formato de título). Teste a função com uma lista de 
nomes bagunçados. 
produtos_baguncados = [ " iphone 13 ", "MACBOOK PRO ", " aIrPoDs Pro", "iPad mini ", " 
caixa de som bluetooth " ]"""


def padronizar_texto(nome):
     return nome.strip().title()

produtos_baguncados = [ " iphone 13 ", "MACBOOK PRO ", " aIrPoDs Pro", "iPad mini ", " caixa de som bluetooth " ]

for produtos in produtos_baguncados:
    print(padronizar_texto(produtos))