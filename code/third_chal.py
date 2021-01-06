f = open("second_chal.txt")
data = f.readlines()
f.close()
data = [i.replace("\n", "") for i in data]
class hills:
    def __init__(self):
        self.layout = data
        self.cols = len(data[0])
        self.rows= len(data)
    def __getitem__(self,idx):#,col):
        row, col = idx
        col = col%self.cols
        return self.layout[row][col]

class sleddy:
    def __init__(self, board, move_right = 3, move_down=1):
        self.pos = [0,0]
        self.board=board
        self.landed_on = [self.board[self.pos]]
        self.finished=False
        self.move_right, self.move_down = move_right, move_down
    def move(self):
        """ Augment our position, record what we land on"""
        if self.pos[0]<=(self.board.rows-self.move_down-1):
            self.pos= [self.pos[0]+self.move_down, self.pos[1]+self.move_right]
            self.landed_on.append(self.board[self.pos])
        else:
            self.finished=True
    def WEEEE(self):
        """#SENDIT down the hill into all the trees"""
        while self.finished == False:
            self.move()


board = hills()
us = sleddy(board)
move_type =[[1,1], [3,1], [5,1], [7,1],[1,2]]

def get_trees(moves):
    us =sleddy(board, moves[0], moves[1])
    us.WEEEE()
    return (len([i for i in us.landed_on if i=='#']))

## We got the first answer right so lets assure this is true
assert get_trees([3,1])==259
k = [get_trees(moves) for moves in move_type]

prod=1
for i in k:
    prod=prod*i
print(prod)