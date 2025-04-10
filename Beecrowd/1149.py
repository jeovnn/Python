valores = input().split()

a = int(valores[0])
n = 0

for i in range(1,len(valores)):
    if int(valores[i])> 0:
        n = int(valores[i])
        break

soma = 0
for i in range(n):
    soma += a + i

print(soma)