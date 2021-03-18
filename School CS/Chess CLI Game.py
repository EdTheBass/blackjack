from copy import deepcopy

a_to_h = "abcdefgh"


def pos_to_coord(pos):
    return [a_to_h[pos[0]], int(pos[1])+1]


def coord_to_pos(pos):
    return [a_to_h.index(pos[0]), pos[1]-1]


# Needs to be globally accessed, so we'll
# declare it outside of the scope of the board
# class
board_arr = [[]]


class Pawn:
    def __init__(self, colour, number, pos):
        self.colour = colour
        self.number = number
        self.start_pos = pos
        self.pos = pos

    def move(self, pos, board_lst):
        pos_dif_x = pos[0] - self.pos[0]
        pos_dif_y = pos[1] - self.pos[1]

        try:
            if board_lst[pos[1]][pos[0]].colour == self.colour:
                return False
        except AttributeError:
            pass

        if pos_dif_x == 0:
            dbl_move_white = (pos_dif_y == 2 and self.pos == self.start_pos and board_lst[pos[1]-1][pos[0]] is None)
            dbl_move_black = (pos_dif_y == -2 and self.pos == self.start_pos and board_lst[pos[1]+1][pos[0]] is None)
            valid_move_white = (dbl_move_white or pos_dif_y == 1) and self.colour == "w"
            valid_move_black = (dbl_move_black or pos_dif_y == -1) and self.colour == "b"
            if (valid_move_white or valid_move_black) and board_lst[pos[1]][pos[0]] is None:
                return True
            else:
                return False
        elif abs(pos_dif_x) == 1:
            if abs(pos_dif_y) == 2 and board_lst[pos[1]][pos[0]] is not None:
                return True
            else:
                return False
        return False


class Rook:
    def __init__(self, colour, number, pos):
        self.colour = colour
        self.number = number
        self.start_pos = pos
        self.pos = pos

    def move(self, pos, board_lst):
        pos_dif_x = pos[0] - self.pos[0]
        pos_dif_y = pos[1] - self.pos[1]

        try:
            if board_lst[pos[1]][pos[0]].colour == self.colour:
                return False
        except AttributeError:
            pass

        if pos_dif_x != 0 and pos_dif_y == 0:
            if pos_dif_x < 0:
                for x in range(1, abs(pos_dif_x)):
                    if board_lst[pos[1]][self.pos[0] - x] is not None:
                        return False
                return True
            else:
                for x in range(1, pos_dif_x):
                    if board_lst[pos[1]][self.pos[0] + x] is not None:
                        return False
                return True
        elif pos_dif_x == 0 and pos_dif_y != 0:
            if pos_dif_y < 0:
                for y in range(1, abs(pos_dif_y)):
                    if board_lst[self.pos[1] - y][pos[0]] is not None:
                        return False
                return True
            else:
                for y in range(1, pos_dif_y):
                    if board_lst[self.pos[1] + y][pos[0]] is not None:
                        return False
                return True
        return False


class Knight:
    def __init__(self, colour, number, pos):
        self.colour = colour
        self.number = number
        self.start_pos = pos
        self.pos = pos

    def move(self, pos, board_lst):
        pos_dif_x = pos[0] - self.pos[0]
        pos_dif_y = pos[1] - self.pos[1]

        try:
            if board_lst[pos[1]][pos[0]].colour == self.colour:
                return False
        except AttributeError:
            pass

        if (abs(pos_dif_x) == 2 and abs(pos_dif_y) == 1) or (abs(pos_dif_x) == 1 and abs(pos_dif_y) == 2):
            return True
        else:
            return False


class Bishop:
    def __init__(self, colour, number, pos):
        self.colour = colour
        self.number = number
        self.start_pos = pos
        self.pos = pos

    def move(self, pos, board_lst):
        pos_dif_x = pos[0] - self.pos[0]
        pos_dif_y = pos[1] - self.pos[1]

        try:
            if board_lst[pos[1]][pos[0]].colour == self.colour:
                return False
        except AttributeError:
            pass

        if abs(pos_dif_x) == abs(pos_dif_y) and pos_dif_x != 0:
            if pos_dif_x < 0:
                if pos_dif_y < 0:
                    for x in range(1, abs(pos_dif_x)):
                        if board_lst[self.pos[1] - x][self.pos[0] - x] is not None:
                            return False
                    return True
                else:
                    for x in range(1, abs(pos_dif_x)):
                        if board_lst[self.pos[1] + x][self.pos[0] - x] is not None:
                            return False
                    return True
            else:
                if pos_dif_y < 0:
                    for x in range(1, abs(pos_dif_x)):
                        if board_lst[self.pos[1] - x][self.pos[0] + x] is not None:
                            return False
                    return True
                else:
                    for x in range(1, abs(pos_dif_x)):
                        if board_lst[self.pos[1] + x][self.pos[0] + x] is not None:
                            return False
                    return True
        return False


class Queen:
    def __init__(self, colour, pos):
        self.colour = colour
        self.start_pos = pos
        self.pos = pos

    def move(self, pos, board_lst):

        pos_dif_x = pos[0] - self.pos[0]
        pos_dif_y = pos[1] - self.pos[1]

        try:
            if board_lst[pos[1]][pos[0]].colour == self.colour:
                return False
        except AttributeError:
            pass

        if pos_dif_x != 0 and pos_dif_y == 0:
            if pos_dif_x < 0:
                for x in range(1, abs(pos_dif_x)):
                    if board_lst[pos[1]][self.pos[0] - x] is not None:
                        return False
                return True
            else:
                for x in range(1, pos_dif_x):
                    if board_lst[pos[1]][self.pos[0] + x] is not None:
                        return False
                return True
        elif pos_dif_x == 0 and pos_dif_y != 0:
            if pos_dif_y < 0:
                for y in range(1, abs(pos_dif_y)):
                    if board_lst[self.pos[1] - y][pos[0]] is not None:
                        return False
                return True
            else:
                for y in range(1, pos_dif_y):
                    if board_lst[self.pos[1] + y][pos[0]] is not None:
                        return False
                return True
        elif abs(pos_dif_x) == abs(pos_dif_y) and pos_dif_x != 0:
            if pos_dif_x < 0:
                if pos_dif_y < 0:
                    for x in range(1, abs(pos_dif_x)):
                        if board_lst[self.pos[1] - x][self.pos[0] - x] is not None:
                            return False
                    return True
                else:
                    for x in range(1, abs(pos_dif_x)):
                        if board_lst[self.pos[1] + x][self.pos[0] - x] is not None:
                            return False
                    return True
            else:
                if pos_dif_y < 0:
                    for x in range(1, abs(pos_dif_x)):
                        if board_lst[self.pos[1] - x][self.pos[0] + x] is not None:
                            return False
                    return True
                else:
                    for x in range(1, abs(pos_dif_x)):
                        if board_lst[self.pos[1] + x][self.pos[0] + x] is not None:
                            return False
                    return True
        return False


class King:
    def __init__(self, colour, pos):
        self.colour = colour
        self.start_pos = pos
        self.pos = pos

    def move(self, pos, board_lst):
        pos_dif_x = pos[0] - self.pos[0]
        pos_dif_y = pos[1] - self.pos[1]

        try:
            if board_lst[pos[1]][pos[0]].colour == self.colour:
                return False
        except AttributeError:
            pass

        if abs(pos_dif_x) > 1 or abs(pos_dif_y) > 1 or (pos_dif_x == 0 and pos_dif_y == 0):
            return False
        return True


# this is the board class.
class Board:
    def __init__(self):
        global board_arr

        self.dimensions = [8, 8]
        # here is a 2D list of the chess
        # grid. A 2D list is essentially
        # any number of lists inside one
        # list. That's why it's known
        # as a 2D list - it has 2
        # dimensions.
        self.wp1 = Pawn('w', 1, [0, 1])
        self.wp2 = Pawn('w', 2, [1, 1])
        self.wp3 = Pawn('w', 3, [2, 1])
        self.wp4 = Pawn('w', 4, [3, 1])
        self.wp5 = Pawn('w', 5, [4, 1])
        self.wp6 = Pawn('w', 6, [5, 1])
        self.wp7 = Pawn('w', 7, [6, 1])
        self.wp8 = Pawn('w', 8, [7, 1])
        self.wr1 = Rook('w', 1, [0, 0])
        self.wr2 = Rook('w', 2, [7, 0])
        self.wk1 = Knight('w', 1, [1, 0])
        self.wk2 = Knight('w', 2, [6, 0])
        self.wb1 = Bishop('w', 1, [2, 0])
        self.wb2 = Bishop('w', 2, [5, 0])
        self.wq = Queen('w', [3, 0])
        self.wk = King('w', [4, 0])
        self.bp1 = Pawn('b', 1, [0, 6])
        self.bp2 = Pawn('b', 2, [1, 6])
        self.bp3 = Pawn('b', 3, [2, 6])
        self.bp4 = Pawn('b', 4, [3, 6])
        self.bp5 = Pawn('b', 5, [4, 6])
        self.bp6 = Pawn('b', 6, [5, 6])
        self.bp7 = Pawn('b', 7, [6, 6])
        self.bp8 = Pawn('b', 8, [7, 6])
        self.br1 = Rook('b', 1, [0, 7])
        self.br2 = Rook('b', 2, [7, 7])
        self.bk1 = Knight('b', 1, [1, 7])
        self.bk2 = Knight('b', 2, [6, 7])
        self.bb1 = Bishop('b', 1, [2, 7])
        self.bb2 = Bishop('b', 2, [5, 7])
        self.bk = King('b', [4, 7])
        self.bq = Queen('b', [3, 7])
        board_arr = [
            [self.wr1, self.wk1, self.wb1, self.wq, self.wk, self.wb2, self.wk2, self.wr2],
            [self.wp1, self.wp2, self.wp3, self.wp4, self.wp5, self.wp6, self.wp7, self.wp8],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [self.bp1, self.bp2, self.bp3, self.bp4, self.bp5, self.bp6, self.bp7, self.bp8],
            [self.br1, self.bk1, self.bb1, self.bq, self.bk, self.bb2, self.bk2, self.br2]
        ]
        self.white = [
            self.wp1, self.wp2, self.wp3, self.wp4, self.wp5, self.wp6, self.wp7, self.wp8,
            self.wr1, self.wk1, self.wb1, self.wq, self.wk, self.wb2, self.wk2, self.wr2]

        self.black = [
            self.bp1, self.bp2, self.bp3, self.bp4, self.bp5, self.bp6, self.bp7, self.bp8,
            self.br1, self.bk1, self.bb1, self.bq, self.bk, self.bb2, self.bk2, self.br2]

    def check_calc_black(self, board_lst):
        for piece in self.white:
            if piece.move(self.bk.pos, board_lst):
                return True
        return False

    def check_calc_white(self, board_lst):
        for piece in self.black:
            if piece.move(self.wk.pos, board_lst):
                return True
        return False

    def checkmate_check_white(self):
        global board_arr
        board_cpy = deepcopy(board_arr)
        for piece in self.white:
            for row in range(len(board_cpy)):
                for square in range(len(board_cpy[row])):
                    if piece.move([row, square], board_arr):
                        self.execute_move(piece.pos, [row, square])
                        if not self.check_calc_white(board_arr):
                            board_arr = board_cpy
                            return False
                        board_arr = board_cpy
        return True

    def checkmate_check_black(self):
        global board_arr
        board_cpy = deepcopy(board_arr)
        for piece in self.black:
            for row in range(len(board_arr)):
                for square in range(len(board_arr[row])):
                    old_pos = deepcopy(piece.pos)
                    if piece.move([square, row], board_arr):
                        self.execute_move(piece.pos, [square, row])
                        if not self.check_calc_black(board_arr):
                            return False
        return True

    @staticmethod
    def draw_black():
        print(" |7 ||6 ||5 ||4 ||3 ||2 ||1 ||0 ")
        count = 7
        for __ in board_arr:
            print(count, end="")
            count -= 1
            for _ in __:
                try:
                    curr = str(_)[str(_).index("__main__")+9:str(_).index("__main__")+10] + _.colour.upper()
                except:
                    curr = "__"
                print(f"|{curr}|", end='')
            print()

    @staticmethod
    def draw_black2(board_ls):
        print(" |7 ||6 ||5 ||4 ||3 ||2 ||1 ||0 ")
        count = 7
        for __ in board_ls:
            print(count, end="")
            count -= 1
            for _ in __:
                try:
                    curr = str(_)[str(_).index("__main__") + 9:str(_).index("__main__") + 10] + _.colour.upper()
                except:
                    curr = "__"
                print(f"|{curr}|", end='')
            print()

    @staticmethod
    def draw_white():
        print(" |0 ||1 ||2 ||3 ||4 ||5 ||6 ||7")
        count = 0
        for __ in board_arr[::-1]:
            print(count, end="")
            count += 1
            for _ in __[::-1]:
                try:
                    curr = str(_)[str(_).index("__main__")+9:str(_).index("__main__")+10] + _.colour.upper()
                except:
                    curr = "__"
                print(f"|{curr}|", end='')
            print()

    def execute_move(self, start_pos, end_pos):
        board_arr[start_pos[1]][start_pos[0]].pos = end_pos
        if board_arr[end_pos[1]][end_pos[0]] is not None:
            if board_arr[end_pos[1]][end_pos[0]].colour == "w":
                self.white.remove(board_arr[end_pos[1]][end_pos[0]])
            elif board_arr[end_pos[1]][end_pos[0]].colour == "b":
                self.black.remove(board_arr[end_pos[1]][end_pos[0]])
        board_arr[end_pos[1]][end_pos[0]] = board_arr[start_pos[1]][start_pos[0]]
        board_arr[start_pos[1]][start_pos[0]] = None
        return


class Player:
    def __init__(self, name, col):
        self.name = name
        self.colour = col


def main(player1, player2):
    board = Board()

    playing = True
    while playing:
        board.draw_white()

        print(f"\n{player1.name}, it is your turn.\n")

        while True:
            print("Enter the piece's starting coordinate, in the form \"x,y\":")
            start_pos = input().split(',')
            if len(start_pos) != 2:
                print("Invalid coordinate.\n")
                continue
            try:
                start_pos[0] = 7 - int(start_pos[0])
                start_pos[1] = 7 - int(start_pos[1])
            except ValueError:
                print("Invalid coordinate.\n")
                continue

            print("Enter the piece's finishing coordinate, in the form \"x,y\":")
            end_pos = input().split(',')
            if len(end_pos) != 2:
                print("Invalid coordinate.\n")
                continue
            try:
                end_pos[0] = 7 - int(end_pos[0])
                end_pos[1] = 7 - int(end_pos[1])
            except ValueError:
                print("Invalid coordinate.\n")
                continue

            piece = board_arr[start_pos[1]][start_pos[0]]

            if piece is None or piece.colour != player1.colour:
                print("Invalid piece.\n")
                continue

            if piece.move(end_pos, board_arr):
                board.execute_move(start_pos, end_pos)
                if board.check_calc_white(board_arr):
                    board.execute_move(end_pos, start_pos)
                    print("Invalid move, this puts your king in check.")
                if board.check_calc_black(board_arr):
                    if board.checkmate_check_black():
                        return 0
            else:
                print("Invalid move.\n")
                continue

            break

        # --------------------------------------------------------------------------------------------------------------
        board.draw_black()

        print(f"\n{player2.name}, it is your turn.\n")

        while True:
            print("Enter the piece's starting coordinate, in the form \"x,y\":")
            start_pos = input().split(',')
            if len(start_pos) != 2:
                print("Invalid coordinate.\n")
                continue
            try:
                start_pos[0] = 7 - int(start_pos[0])
                start_pos[1] = 7 - int(start_pos[1])
            except ValueError:
                print("Invalid coordinate.\n")
                continue

            print("Enter the piece's finishing coordinate, in the form \"x,y\":")
            end_pos = input().split(',')
            if len(end_pos) != 2:
                print("Invalid coordinate.\n")
                continue
            try:
                end_pos[0] = 7 - int(end_pos[0])
                end_pos[1] = 7 - int(end_pos[1])
            except ValueError:
                print("Invalid coordinate.\n")
                continue

            piece = board_arr[start_pos[1]][start_pos[0]]

            if piece is None or piece.colour != player2.colour:
                print("Invalid piece.\n")
                continue

            if piece.move(end_pos, board_arr):
                board.execute_move(start_pos, end_pos)
                if board.check_calc_black(board_arr):
                    board.execute_move(end_pos, start_pos)
                    print("Invalid move, this puts your king in check.")
                if board.check_calc_white(board_arr):
                    if board.checkmate_check_white():
                        return 0
            else:
                print("Invalid move.\n")
                continue

            break


print("Welcome to Chess!")
print("-----------------")
print("This was created by Edmund, Lawrence, and Max.")
print("-----------------\n")
player1name = input("Player 1's name: ")
player2name = input("Player 2's name: ")
p1 = Player(player1name, "w")
p2 = Player(player2name, "b")
winner = main(p1, p2)
if winner == 0:
    print(f"Congratulations, {p1.name}, you won!")
else:
    print(f"Congratulations, {p2.name}, you won!")
