array = [1,12,32]

for i in range(0,len(array)):
    print(array[i])

for i in array:
    print(i)

for i in range(5):
    print(i)

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Estratégia: iterar por uma cópia
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

