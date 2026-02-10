"""Exercício 5: Sistema de Triagem de E-mails (Setor de Customer Experience) Crie um 
sistema que ajude a filtrar para qual departamento uma reclamação deve ir. O usuário deve 
digitar o assunto do e-mail. 
● Se no assunto aparecer a palavra "pagamento" ou "boleto", exiba: "Encaminhado 
para o Financeiro". 
● Se no assunto aparecer a palavra "entrega" ou "atraso", exiba: "Encaminhado para a 
Logística". 
● Caso não seja nenhum desses, exiba: "Encaminhado para o Suporte Geral". Dica: 
Use o operador in para verificar se a palavra está dentro do texto."""





assunto = ["pagamento","boleto"]

if "pagamento" and "boleto" in assunto:
    print("Encaminhando para o setor de Financeiro")
elif "entrega" and "atraso" in assunto:
    print("Encaminhando para o setor de Logística")
else:
    print("Encaminhando para o Suporte geral")

    