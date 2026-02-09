"""Exercício 3: Divisão de Cargas (Logística/Transporte) 
Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada 
caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão 
totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma 
última viagem menor? (Use %)"""



caixas  = 1_250
caminhao = 12 # caixas 

viagem = caixas/caminhao

print(f"Cada caminhão pode transportar {round(viagem,2)} de caixas")


