pilha = [1,2,3,4]

print(pilha)
tem = False

for i in range(0,len(pilha)):
    if pilha[i] == 2:
        tem = True

if tem:
    print("tem dois")