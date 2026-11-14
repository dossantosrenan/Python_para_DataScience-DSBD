nome, idade, cidade = input(
    "Digite nome, idade e cidade separados por espaço: "
).split()  # Armazena os valores digitados nas variáveis

idade = int(idade)  # Converte a idade de string para inteiro

# Exibe o nome, a idade e a cidade do usuário
print(f"{nome} tem {idade} anos e mora em {cidade}.")