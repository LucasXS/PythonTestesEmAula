#O PODER DO PRINT
#nome = input('Qual é seu nome? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome)) #com 20 espaços, centralizado e com os '=' em volta
#print('Prazer em te conhecer {:^20}!'.format(nome)) #centralizado
#print('Prazer em te conhecer {:<20}!'.format(nome)) #com 20 espaços a esquerda
#print('Prazer em te conhecer {:>20}!'.format(nome)) #com 20 espaços a direita
#print('Prazer em te conhecer {:20}!'.format(nome)) #com 20 espaços*#

#COMO A SOMA NÃO SERVIRÁ PARA NADA DEPOIS EU POSSO COLOCAR DENTRO DO .FORMAT
#n1 = int(input('Um valor: '))
#n2 = int(input('Outro valor: '))
#print('A soma vale {}'.format(n1+n2))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoInteira = n1 // n2
exponeciacao = n1 ** n2
print('A soma é {}, \nO produto é {}, \nA divisão é {:.3f}'.format(soma, multiplicacao, divisao), end=' ')
print('\nDivisão inteira {} \nPotência {}'.format(divisaoInteira, exponeciacao))



