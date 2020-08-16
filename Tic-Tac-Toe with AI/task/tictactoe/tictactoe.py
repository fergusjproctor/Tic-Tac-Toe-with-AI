# write your code here
import string
import random
import operator

# Game output        Coordinates to request:  Corresponding representation in state list:
#  ---------
#  | _ _ _ |              (3 1) (3 2) (3 3)                             (2 0) (2 1) (2 2)
#  | _ _ _ |              (2 1) (2 2) (2 3)                             (1 0) (1 1) (1 2)
#  | _ _ _ |              (1 1) (1 2) (1 3)                             (0 0) (0 1) (0 2)
#  ---------


class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.other_symbol = list({'X', 'O'} - {self.symbol})[0]


class User(Player):
    def move(self):
        while True:
            coord_request = input('Enter the coordinates: ')
            if not len(coord_request) == 3:
                print('Enter two digits separated by a space!')
                continue
            if not (coord_request[0].isnumeric() and coord_request[2].isnumeric()):
                print('You should enter numbers!')
                continue
            elif (set(coord_request[0]) & {'1', '2', '3'} == set()) or (set(coord_request[2]) & {'1', '2', '3'} == set()):
                print('Coordinates should be from 1 to 3!')
                continue
            elif get_spot_value(state, coord_request) != ' ':
                print('This cell is occupied! Choose another one!')
                continue
            # Set game state to account for new input
            else:
                set_state(state, coord_request, self.symbol)
                break


class CPU(Player):
    @staticmethod
    def check_almost(state2check, side):
        # Check if side is about to win
        # Check horizontal
        count = 0
        for i in state2check:
            if i.count(side) == 2 and ' ' in i:
                return str(count + 1) + ' ' + str(i.index(' ') + 1)
            count += 1
        count = 0
        # Check vertical
        for k in [[j[i] for j in state2check] for i in range(0, 3)]:
            if k.count(side) == 2 and ' ' in k:
                return str(k.index(' ') + 1) + ' ' + str(count + 1)
            count += 1
        # Check diagonal
        diagonal1 = [state2check[i][j] for j in range(0, 3) for i in range(0, 3) if i == j]
        diagonal2 = [state2check[i][j] for j in range(0, 3) for i in range(0, 3) if i == 2 - j]
        if diagonal1.count(side) == 2 and ' ' in diagonal1:
            return str(diagonal1.index(' ') + 1) + ' ' + str(diagonal1.index(' ') + 1)
        elif diagonal2.count(side) == 2 and ' ' in diagonal2:
            return str(3 - diagonal2.index(' ')) + ' ' + str(diagonal2.index(' ') + 1)
        else:
            return None

    def move(self):
        print('Making move level "easy"')
        while True:
            # Enter and check coordinates
            coord_request = str(random.randint(1, 3)) + ' ' + str(random.randint(1, 3))
            if get_spot_value(state, coord_request) != ' ':
                continue
            # Set game state to account for new input
            else:
                set_state(state, coord_request, self.symbol)
                break


class EasyCPU(CPU):
    pass


class MediumCPU(CPU):
    def move(self):
        print('Making move level "medium"')
        # If it can win in one move, make it
        if self.check_almost(state, self.symbol) is not None:
            coord_request = self.check_almost(state, self.symbol)
            set_state(state, coord_request, self.symbol)
        # If the opponent is about to win, beat it
        elif self.check_almost(state, self.other_symbol):
            coord_request = self.check_almost(state, self.other_symbol)
            set_state(state, coord_request, self.symbol)
        # Otherwise, make a random move
        else:
            while True:
                coord_request = str(random.randint(1, 3)) + ' ' + str(random.randint(1, 3))
                if get_spot_value(state, coord_request) != ' ':
                    continue
                else:
                    set_state(state, coord_request, self.symbol)
                    break


class HardCPU(CPU):
    @staticmethod
    def check_almost_draw(state2check, side):
        # Check if about to draw (if not almost win and only one space left). This function should only be used after check almost
        if sum(i.count(' ') for i in state2check) == 1:
            count = 0
            for i in state2check:
                if ' ' in i:
                    return str(count + 1) + ' ' + str(i.index(' ') + 1)
                count += 1
        else:
            return None

    @staticmethod
    def symbols_turn(state, symbol, other_symbol):
        total_symbols = sum(i.count(symbol) for i in state)
        total_other_symbols = sum(i.count(other_symbol) for i in state)
        if (symbol == 'X' and total_symbols > total_other_symbols) or (symbol == 'O' and total_other_symbols == total_symbols):
            return False
        else:
            return True

    def minimax(self, base_state):
        # if opponent move
        if not self.symbols_turn(base_state, self.symbol, self.other_symbol):
            # if symbol about to win return 10 and move required
            if self.check_almost(base_state, self.other_symbol) is not None:
                return -10, self.check_almost(base_state, self.other_symbol)
            elif self.check_almost_draw(base_state, self.other_symbol) is not None:
                return 0, self.check_almost_draw(base_state, self.other_symbol)
            else:
                states2check = self.state_options(base_state, self.other_symbol)
                count = 0
                state_values = []
                move_coords = []
                for a_state in states2check:
                    value, coords = self.minimax(a_state)
                    state_values.append(value)
                    move_coords.append(coords)
                move = move_coords[state_values.index(max(state_values))]
                return min(state_values), move

        # else it's CPU's move, return maximum of minimax(all possible states)
        else:
            # if symbol about to win return 10 and move required
            if self.check_almost(base_state, self.symbol) is not None:
                return 10, self.check_almost(base_state, self.symbol)
            elif self.check_almost_draw(base_state, self.symbol) is not None:
                return 0, self.check_almost_draw(base_state, self.symbol)
            else:
                states2check = self.state_options(base_state, self.symbol)
                count = 0
                state_values = []
                move_coords = []
                for a_state in states2check:
                    value, coords = self.minimax(a_state)
                    state_values.append(value)
                    move_coords.append(coords)
                move = move_coords[state_values.index(min(state_values))]
                return max(state_values), move

    @staticmethod
    def create_state(old_state):
        new_state = []
        for i in range(len(old_state)):
            new_state.append([])
            for j in range(len(old_state[i])):
                if old_state[i][j] == ' ':
                    new_state[i].append(' ')
                elif old_state[i][j] == 'X':
                    new_state[i].append('X')
                elif old_state[i][j] == 'O':
                    new_state[i].append('O')
        return new_state

    def state_options(self, ori_state, next_symbol):
        number_options = sum(i.count(' ') for i in ori_state)
        states = []
        for i in range(len(ori_state)):
            for j in range(len(ori_state[i])):
                if ori_state[i][j] == ' ':
                    state2add = self.create_state(ori_state)
                    state2add[i][j] = next_symbol
                    states.append(state2add)
        return states

    def move(self):
        print('Making move level "hard"')
        # Make whichever move minimax suggests
        coord_request = self.minimax(state)[1]
        set_state(state, coord_request, self.symbol)

    @staticmethod
    def check_draw(draw_state):
        # Check if draw, otherwise it game is not finished
        if any(i == ' ' for j in draw_state for i in j):
            return False
        else:
            return True


def printing():
    graphic_state = """---------
| {} |
| {} |
| {} |
---------""".format(' '.join(state[2]), ' '.join(state[1]), ' '.join(state[0]))
    print(graphic_state)


def check_win(arg):
    # Check if arg has won
    # Check horizontal
    if any(i == [arg, arg, arg] for i in state):
        return True
    # Check vertical
    elif any(k == [arg, arg, arg] for k in [[j[i] for j in state] for i in range(0, 3)]):
        return True
    # Check diagonal
    elif ([state[i][j] for j in range(0, 3) for i in range(0, 3) if i == j] == [arg, arg, arg]) or ([state[i][j] for j in range(0, 3) for i in range(0, 3) if i == 2 - j] == [arg, arg, arg]):
        return True
    else:
        return False


def set_state(state, coord_request, symbol):
    state[int(coord_request[0]) - 1][int(coord_request[2]) - 1] = symbol


def get_spot_value(state, coord_request):
    return state[int(coord_request[0]) - 1][int(coord_request[2]) - 1]


while True:
    # Request whether to start new game or exit
    inp = input('Input command')
    if inp == 'exit':
        break
    inp = inp.split()
    if 'start' not in inp or (inp.count('easy') + inp.count('user') + inp.count('medium') + inp.count('hard')) < 2:
        print('Bad parameters')
        continue
    else:
        state = [[' ', ' ', ' '] for i in range(0, 3)]
        printing()
        players = []
        symbol = 'X'
        # Set users
        for i in range(1, len(inp)):
            if inp[i] == 'easy':
                players.append(EasyCPU(symbol))
            if inp[i] == 'medium':
                players.append(MediumCPU(symbol))
            if inp[i] == 'hard':
                players.append(HardCPU(symbol))
            if inp[i] == 'user':
                players.append(User(symbol))
            symbol = 'O'
        move_counter = 1
    while True:
        # Request move
        if move_counter % 2 != 0:
            players[0].move()
        else:
            players[1].move()
        move_counter += 1
        printing()
        # Check if anyone has won
        if check_win('X'):
            print('X wins')
            break
        elif check_win('O'):
            print('O wins')
            break
        # Check if draw, otherwise it game is not finished
        elif any(i == ' ' for j in state for i in j):
            continue
        else:
            print('Draw')
            break
