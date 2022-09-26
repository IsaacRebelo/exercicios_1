"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inderido a frase apresente:
 - Qual é o comprimento da frase inserida (incluindo espaços)
 - Quantas palavras tem a frase
 - Quantas vogais tem a frase
 - Quantas letras maiusculas tem a frase
 - Quantas letras minusculas tem a frase
 - Quantos numeros tem a frase
 - Apresente a frase invertida. Exemplo: A frase é 'Bom dia!' deve dar '!aid moB'
"""
str1 = input('Introduza a sua frase')
vogais= 'aeiouAEIOU'
conta_vogais= 0
conta_consoantes= 0
conta_tamanhodafrase=0
l,u=0,0
consoantes= 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'

for i in str1:
    if (i >='A' and i <='Z'):
        l=l+1
    if(i >='a' and i <='z'):
        u=u+1

for i in str1:
    if i in vogais:
        conta_vogais+=1
    if i in consoantes:
        conta_consoantes+=1
for k in str1:
    conta_tamanhodafrase=conta_tamanhodafrase+1

(print(f'vogais: {conta_vogais}'))
(print(f'consoantes:{conta_consoantes}'))
(print(f'tamanho da frase: {conta_tamanhodafrase}'))
(print(f'maiusculas e minusculas da frase: {l,u}'))









