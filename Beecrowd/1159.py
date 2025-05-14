soma = 0

while True:
    n = int(input())
    if n == 0:
        break

    if n % 2 == 0:
        soma += n + n+2 + n+4 + n+6 + n+8
    elif n % 2 != 0:
        soma += n+1 + n+3 + n+5 + n+7 + n+9
    print(soma)
    soma = 0