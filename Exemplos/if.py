x = int(input("Insira um número inteiro: "))

if x < 0:
    x = 0
    print('Negativo alterado para zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Um')
else:
    print('Mais')