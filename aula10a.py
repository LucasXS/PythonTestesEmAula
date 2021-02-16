#nome = str(input('Qual é seu nome? ')).upper()
#if nome == 'Lucas':
 #   print('Que nome lindo você tem!')
#else:
#    print('Seu nome é tão normal!')
#print('Bom dia, {}!'.format(nome))


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(media))
if media >=7.0:
    print('Sua media foi boa! PARABÉNS!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')
