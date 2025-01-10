hat_list = [1, 2, 3, 4, 5]

# Etapa 1: substitua o número do meio por um número inteiro inserido pelo usuário.
user_input = int(input("Digite um número inteiro para substituir o número do meio: "))
hat_list[2] = user_input

# Etapa 2: remova o último elemento da lista.
hat_list.pop()

# Etapa 3: imprima o comprimento da lista atual.
print("O comprimento atual da lista é:", len(hat_list))

print(hat_list)
