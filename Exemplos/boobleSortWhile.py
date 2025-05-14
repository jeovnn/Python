lista = [21,4,3,4,5,6,7,21,43,9]
aux = 0
flag = True

while(flag == True):
    flag = False

    for i in range(0,len(lista)-1):
     if(lista[i]>lista[i+1]):
        aux = lista[i]
        lista[i] = lista[i+1]
        lista[i+1] = aux
        flag = True

print(lista)