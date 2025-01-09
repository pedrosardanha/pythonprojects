blocks = int(input("Insira o número de blocos:"))

height = 0
layer_blocks = 1

while blocks >= layer_blocks:
    blocks -= layer_blocks
    height += 1
    layer_blocks += 1

print("A altura da pirâmide:", height)
