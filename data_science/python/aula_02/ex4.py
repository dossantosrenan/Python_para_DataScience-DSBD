# Armazena o preço e substitui a vírgula por ponto para converter corretamente para float
preco = float(input("Digite o preço: ").replace(",", "."))
print(f"Preço: R$ {preco:.2f}")
