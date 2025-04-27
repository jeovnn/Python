# sintaxe =>    map(função, iterável1, iterável2, ...)

letras = ['Alan', 'breno', 'clovis', 'dudu']

maiusculas = map(str.upper, letras)
print(list(maiusculas))  
# ['ALAN', 'BRENO', 'CLOVIS', 'DUDU']

minusculas = list(map(str.lower, letras))
print(minusculas)
# ['alan', 'breno', 'clovis', 'dudu']

numeros = [1, 2, 3, 4, 5]



# Função que eleva um número ao quadrado
def quadrado(x):
    return x ** 2

resultado = map(quadrado, numeros)
print(list(resultado))  
# [1, 4, 9, 16, 25]