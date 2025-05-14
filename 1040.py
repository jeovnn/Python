[nota1,nota2,nota3,nota4] = list(map(float, input().split()))

media = (2 * nota1 + 3 * nota2 + 4 * nota3 + 1 * nota4)/10

print(f"Media: {media:.1f}")

if(media >= 7.0):
    print("Aluno aprovado.")
elif(media < 5.0):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    exame = float(input().strip())
    print(f"Nota do exame: {exame:.1f}")

    media = (media + exame)/2

    if(media >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media:.1f}")