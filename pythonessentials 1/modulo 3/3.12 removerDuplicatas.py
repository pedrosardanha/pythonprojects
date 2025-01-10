my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Cria uma nova lista para armazenar os elementos exclusivos
unique_list = []

# Itera sobre os elementos da lista original
for number in my_list:
    # Adiciona o número à lista exclusiva se ele ainda não estiver nela
    if number not in unique_list:
        unique_list.append(number)

# Substitui a lista original pela lista de elementos exclusivos
my_list = unique_list

# Imprime a lista com os elementos exclusivos
print("A lista com os elementos exclusivos:", my_list)
