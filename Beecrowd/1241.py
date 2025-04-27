n = int(input())

for i in range(0,n):
    a,b = input().split(' ')
    if a.endswith(b):
        print("encaixa")
    else:
        print("nao encaixa")