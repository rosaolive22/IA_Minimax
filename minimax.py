from jogo_da_velha import branco, token, verificaGanhador

#Contém 3 funções principais:

# 1ª, 
def movimentoIA(board, jogador):
    #Verifica todas as posições que estão em branco
    possibilidades = getPosicoes(board)
    melhor_valor = None
    melhor_movimento = None
    #Procura a melhor possibilidade
    for possibilidade in possibilidades:
        # Marca a posição no tabuleiro com o token do jogador atual
        #Acessando a lista de posições(linha 41)
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
	#Chama a função minimax para avaliar essa jogada
        valor = minimax(board, jogador)
	#Após a jogada limpa--> Desfaz a jogada para avaliar a próxima
        board[possibilidade[0]][possibilidade[1]] = branco
       # Analiza a melhor jogada  


        #print(possibilidade, valor)


        if(melhor_valor is None):
            melhor_valor = valor
            melhor_movimento = possibilidade
        elif(jogador == 0):
            print(possibilidade, valor)
            if(valor > melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade
     
    print("Chance de vitória: ",melhor_valor*100,"%")
    # Retorna a linha e a coluna da melhor jogada		
    return melhor_movimento[0], melhor_movimento[1]

#Pega todas as posições vazias	
def getPosicoes(board):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == branco):
                posicoes.append([i, j])
    
    return posicoes

score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}
def minimax(board, jogador):
     # Verifica se há um ganhador no tabuleiro atual
    ganhador = verificaGanhador(board)
    if(ganhador):
         # Retorna o resultado do jogo
        return score[ganhador]
        # Alterna para o próximo jogador
    jogador = (jogador + 1)%2    
     # Obtém todas as posições vazias no tabuleiro
    possibilidades = getPosicoes(board)
    melhor_valor = None
      # Explora todas as possibilidades de jogada
    for possibilidade in possibilidades:
         # Coloca X ou O
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
         # Pega o valor
        valor = minimax(board, jogador)
        # Desfaz a jogada para explorar outras possibilidades       
        board[possibilidade[0]][possibilidade[1]] = branco
 # Atualiza o melhor valor de acordo com o jogador atual
        if(melhor_valor is None):
            melhor_valor = valor
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor
 # Retorna o melhor valor encontrado
    return melhor_valor