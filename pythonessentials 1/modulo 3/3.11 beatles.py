# Etapa 1: criar uma lista vazia chamada beatles
beatles = []
print("Etapa 1:", beatles)

# Etapa 2: usar o método append() para adicionar John Lennon, Paul McCartney e George Harrison à lista
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)

# Etapa 3: usar o loop for e o método append() para solicitar que o usuário adicione Stu Sutcliffe e Pete Best à lista
for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(member)
print("Etapa 3:", beatles)

# Etapa 4: usar a instrução del para remover Stu Sutcliffe e Pete Best da lista
del beatles[-2]
del beatles[-1]
print("Etapa 4:", beatles)

# Etapa 5: usar o método insert() para adicionar Ringo Starr ao início da lista
beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)
