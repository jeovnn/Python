# A palavra-chave lambda em Python é usada para criar funções anônimas, 
# ou seja, funções que não têm um nome definido.
# Essas funções são frequentemente utilizadas quando você precisa de uma 
# função simples e de curta duração, especialmente como argumento para 
# outras funções, como map(), filter(), e sorted().

# sintaxe =>    lambda argumentos: expressão

num1 = 7
num2 = 10

soma = lambda x,y: x+y

print(soma(num1,num2))
# 17
