vetor = list(map(int, input().split()))
aux = 0

for i in range(0,len(vetor)):
    for j in range(0,len(vetor) - 1):
        if vetor[j] > vetor[j+1]:
            aux = vetor[j]
            vetor[j] = vetor[j+1]
            vetor[j+1] = aux

print(vetor)