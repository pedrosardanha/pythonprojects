from random import randrange

def display_board(board):
    # A função aceita um parâmetro contendo o status atual da placa e o imprime no console.
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada,
    # verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.
    move = int(input("Digite seu movimento: "))
    valid_moves = make_list_of_free_fields(board)
    for move_tuple in valid_moves:
        if board[move_tuple[0]][move_tuple[1]] == str(move):
            board[move_tuple[0]][move_tuple[1]] = 'O'
            return

def make_list_of_free_fields(board):
    # A função navega pelo tabuleiro e constrói uma lista de todas as casas livres;
    # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # A função analisa o estado da placa a fim de verificar se
    # o jogador usando 'O's ou 'X's ganhou o jogo.
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[row][col] == sign for row, col in condition):
            return True
    return False

def draw_move(board):
    # A função desenha o movimento do computador e atualiza o tabuleiro.
    free_fields = make_list_of_free_fields(board)
    move = randrange(len(free_fields))
    board[free_fields[move][0]][free_fields[move][1]] = 'X'

# Inicializa o tabuleiro
board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

# Exibe o tabuleiro inicial
display_board(board)

# Loop principal do jogo
while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("Você ganhou!")
        break
    if not make_list_of_free_fields(board):
        print("Empate!")
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("O computador ganhou!")
        break
    if not make_list_of_free_fields(board):
        print("Empate!")
        break
