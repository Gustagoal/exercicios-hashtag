"""Exercício 2: Sistema de Cadastro de Colaborador (Setor de RH) Ao cadastrar um novo 
funcionário, o RH precisa extrair o primeiro nome para criar um crachá e padronizar o 
e-mail. Crie um programa que: 
1. Peça o nome completo do colaborador. 
2. Peça o e-mail pessoal do colaborador. 
3. Extraia o primeiro nome (deixe-o com a primeira letra maiúscula). 
4. Padronize o e-mail (remova espaços extras e deixe tudo em letras minúsculas). 
5. Exiba a mensagem: "Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail 
padronizado]". """


nome = input("Digite seu nome : ")
email = input("Digite o seu email : ")
primeiro_nome = nome.split()[0].title()
email_ajustado = email.lower().strip()

print(f"Cadastro concluído : {primeiro_nome}\n Email de acesso : {email_ajustado}")