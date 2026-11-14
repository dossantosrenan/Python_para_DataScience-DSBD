nome_aluno = input("Digite o nome do aluno: ")  # Armazena o nome do aluno
idade_aluno = int(input("Digite a idade: "))  # Armazena a idade do aluno
media_aluno = float(input("Digite a média: "))  # Armazena a média do aluno

print(
    f"Nome do aluno é {nome_aluno}, "
    f"ele tem {idade_aluno} anos "
    f"e sua média é {media_aluno:.2f}."
)