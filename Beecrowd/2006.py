certa = int(input())
tentativas = list(map(int, input().split()))
certas = 0

for i in range(5):
    if tentativas[i] == certa:
        certas += 1

print(certas)