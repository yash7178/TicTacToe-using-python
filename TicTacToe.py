def display_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def space_check(board, position):
        return(board[position] == ' ')

def player_input(board, position, mark):
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
                position = int(input('Choose your next position: (1-9) '))

        board[position]= mark
        position = 0

def tie_check(board):
        for i in range(1,10):
                if space_check(board, i):
                        return False
        return True


def replay():
        return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def win_check(board, mark):
        return(board[1] == board[2] == board[3] == mark or
                board[4] == board[5] == board[6] == mark or
                board[7] == board[8] == board[9] == mark or
                board[1] == board[4] == board[7] == mark or
                board[2] == board[5] == board[8] == mark or
                board[3] == board[6] == board[9] == mark or
                board[1] == board[5] == board[9] == mark or
                board[3] == board[5] == board[7] == mark)
while True:
        game_on = True
        b_list = [' '] * 10
        turn = 0
        display_board(b_list)
        while game_on == True:
        
        
        
                position = 0
                if turn == 0:
                
                        player_input(b_list, position, 'X')
                        display_board(b_list)

                        if (win_check(b_list, 'X')):
                                print("Player 1 has won")
                                game_on = False
                        
                        else:
                                if (tie_check(b_list)):
                                        print("Its a tie")
                                        game_on = False
                                else:
                                        turn = 1                
                
                else:
                
                        player_input(b_list, position, 'O')
                        display_board(b_list)

                        if (win_check(b_list, 'O')):
                                print("Player 2 has won")
                                game_on = False
                        else:
                                if (tie_check(b_list)):
                                        print("Its a tie")
                                        game_on = False
                                else:
                                        turn = 0
        
        if not replay():
                break
