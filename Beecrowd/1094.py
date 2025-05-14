n = int(input())
total = 0
total = int(total)
coelhos = 0
ratos = 0
sapos = 0

for i in range(0,n):
    [qtde,animal] = input().split(" ")
    qtde = int(qtde)
    total += qtde

    if animal == "C":
        coelhos += qtde
    elif animal == "R":
        ratos += qtde
    elif animal == "S":
        sapos += qtde

print("Total:",total,"cobaias")
print("Total de coelhos:",coelhos)
print("Total de ratos:",ratos)
print("Total de sapos:",sapos)
print("Percentual de coelhos: {:.2f} %".format(coelhos * 100 / total))
print("Percentual de ratos: {:.2f} %".format(ratos * 100 / total))
print("Percentual de sapos: {:.2f} %".format(sapos * 100 / total))