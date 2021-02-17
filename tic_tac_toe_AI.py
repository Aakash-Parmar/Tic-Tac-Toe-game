board={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
def board_show():
    print(board[1] + ' |' + board[2] + ' |' + board[3])
    print('--+--+--')
    print(board[4] + ' |' + board[5] + ' |' + board[6])
    print('--+--+--')
    print(board[7] + ' |' + board[8] + ' |' + board[9])

def player_move():
    choice=input("x's move: ")
    if choice.isdigit() and int(choice)>0 and int(choice)<10 and board[int(choice)]==' ':
        board[int(choice)]='x'
        board_show()
    else:
        print('INVALID MOVE, PLEASE TRY AGAIN!')
        player_move()

def iswinner(string,board):
    if (board[1]==string and board[2]==string and board[3]==string) or (board[4]==string and board[5]==string and board[6]==string) or (board[7]==string and board[8]==string and board[9]==string) or (board[1]==string and board[4]==string and board[7]==string) or (board[2]==string and board[5]==string and board[8]==string)or (board[3]==string and board[6]==string and board[9]==string) or (board[1]==string and board[5]==string and board[9]==string) or (board[3]==string and board[5]==string and board[7]==string):
        return True
    else:
        return False

def isfull():
    count=0
    for _ in range(1,10):
        if board[_]!=' ':
            count=count+1
    if count==9:
        return True
    else:
        return False



def comp_move():
    print("o's move")
    import random
    boardcopy=board.copy()
    possiblemoves=[i for i in board if board[i]==' ']
    corners=[i for i in possiblemoves if (i==1 or i==3 or i==7 or i==9)]
    edges=[i for i in possiblemoves if (i==2 or i==4 or i==6 or i==8)]


    for i in possiblemoves:
        boardcopy[i]='o'
        if iswinner('o',boardcopy):
            board[i]='o'
            return
        else:
            boardcopy[i]=' '
    for i in possiblemoves:
        boardcopy[i]='x'
        if iswinner('x',boardcopy):
            board[i]='o'
            return
        else:
            boardcopy[i]=' '
    if boardcopy[i]==' ':
        if boardcopy[5]==' ':
            board[5]='o'
            return
        elif len(corners)!=0:
            board[random.choice(corners)]='o'
            return
        elif len(edges)!=0:
            board[random.choice(edges)]='o'
            return
        else:
            return


while True :
    print('Please select a position for \'x\' from (1-9)')
    board_show()
    player_move()
    if iswinner('x',board):
        print("'x' won")
        break
    if isfull():
        print('MATCH DRAWN!')
        break
    comp_move()
    board_show()
    if iswinner('o',board):
        print("'o'WON, BETTER LUCK NEXT TIME!")
        break
    if isfull():
        print('MATCH DRAWN!')
        break



