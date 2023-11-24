notas = []

for i in range(4):
    
    nota = float(input(f"Digite a nota do da atividade {i + 1}: " ))
    
    notas.append(nota)
    
    print("Notas dos semestres: ")
    for i, nota in enumerate(notas):
        print(f"nota { i + 1}: {nota}")


media = input("Deseja receber a media do semestre? (s/n): ")

if media.lower() == 's':
    media = sum(notas) / len(notas)
    print(f"a media do semestre foi {media}!")
    
    if media >= 6:
        print("Parabéns você foi aprovado! ")
    else:
        print("Infelizmente você não foi aprovado! ")

else:
    print("Programa encerrado!")
    
    




