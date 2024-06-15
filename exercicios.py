#Exercicio 1. Verificacao de Qualidade de Dados
#Voce esta analisando um conjunto de dados de vendas e precisa garantir que todos os 
#registros tenham valores positivos para quantidade e preco
#Escreva um programa que verifique esses campos e imprima Dados Validos se ambos
#forem positivos ou Dados invalidos caso contrario

quantidade = 40
preco = 20

if quantidade > 0 and preco > 0:
    print("Valores Validos")
else:
    print("Valores invalidos")


#Exercicio 2. Contagem de Palavras em textos
#Objetivo: Dado um texto, contar quantas vezes cada palavra unica aparece nele
 
texto = "hoje e nossa terceira aula do bootcamp, bootcamp de python"

palavras = texto.split()

contagem_de_palavras = {}

#eu quero percorrer todas as palavras dentro de palavras e checar se ela ja esta no meu contagem de palavras

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras = +1
    else:
        contagem_de_palavras = 1