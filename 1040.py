notas = input().split(" ")
for i in range(len(notas)):
    notas[i] = float(notas[i])

media_ponderada = (notas[0] * 2 + notas[1] * 3 + notas[2] * 4 + notas[3] * 1) / (2 + 3 + 4 + 1)
print(f"Media: {media_ponderada:.1f}")

if media_ponderada >= 7:
    print("Aluno aprovado.")
elif media_ponderada < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    nota_do_exame = float(input())
    print(f"Nota do exame: {nota_do_exame:.1f}")

    media_final = (media_ponderada + nota_do_exame) / 2

    if media_final >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {media_final:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {media_final:.1f}")