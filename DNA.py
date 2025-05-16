def mostrar_menu():
    print("\nMenu de Modificação de DNA")
    print("1 - Substituir base")
    print("2 - Inserir base")
    print("3 - Remover base")
    print("4 - Mostrar sequência atual")
    print("0 - Sair")

def substituir_base(dna, pos, nova_base):
    if 0 <= pos < len(dna):
        dna = dna[:pos] + nova_base + dna[pos+1:]
    return dna

def inserir_base(dna, pos, nova_base):
    if 0 <= pos <= len(dna):
        dna = dna[:pos] + nova_base + dna[pos:]
    return dna

def remover_base(dna, pos):
    if 0 <= pos < len(dna):
        dna = dna[:pos] + dna[pos+1:]
    return dna

# DNA inicial (pode editar essa sequência)
dna = "ATCGGATAC"

print(f"Sequência de DNA original: {dna}")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        pos = int(input("Posição da base a substituir (começa do 0): "))
        nova = input("Nova base (A, T, C ou G): ").upper()
        dna = substituir_base(dna, pos, nova)
        print(f"Nova sequência: {dna}")

    elif escolha == "2":
        pos = int(input("Posição para inserir nova base: "))
        nova = input("Base a inserir (A, T, C ou G): ").upper()
        dna = inserir_base(dna, pos, nova)
        print(f"Nova sequência: {dna}")

    elif escolha == "3":
        pos = int(input("Posição da base a remover: "))
        dna = remover_base(dna, pos)
        print(f"Nova sequência: {dna}")

    elif escolha == "4":
        print(f"Sequência atual: {dna}")

    elif escolha == "0":
        print("Encerrando o editor de DNA.")
        break

    else:
        print("Opção inválida.")
