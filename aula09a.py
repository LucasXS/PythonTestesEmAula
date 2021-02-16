frase = '   Curso em Video Python   '
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.split())

print(frase.replace('Python','Android')) #string é imutavel
print(frase)
frase = frase.replace('Python','Android')
print(frase)

print('Curso' in frase)
print(frase.find('Video'))
print(frase.find('video'))
print(frase.lower().find('video'))
print(frase.split())
