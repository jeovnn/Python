while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        respostas = list(map(int, input().split()))
        alternativas = ['A', 'B', 'C', 'D', 'E']
        marcadas = []

        for j in range(5):
            if respostas[j] <= 127:
                marcadas.append(j)

        if len(marcadas) == 1:
            print(alternativas[marcadas[0]])
        else:
            print('*')  