secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

while True:
    guess = int(input("Digite seu palpite: "))
    if guess == secret_number:
        print("Muito bem, trouxa! Você está livre agora.")
        break
    else:
        print("Ha ha! Você está preso no meu loop!")
