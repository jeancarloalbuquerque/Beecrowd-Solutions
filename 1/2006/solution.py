"""
Bloco: 1 - Iniciante
Problema: Identificando o Chá
Autor: Inês Kereki

Resolução: Jean Carlo de Albuquerque

"""

correct = input()

answers = input().split(' ')

correctAnswers = 0

for answer in answers:
    if int(answer) == int(correct):
        correctAnswers += 1

print(correctAnswers)