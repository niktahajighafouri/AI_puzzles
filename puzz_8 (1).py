from copy import deepcopy
from colorama import Fore, Back, Style
from time import sleep
import os

# direction matrix
DIRECTIONS = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
# target matrix
END = [[1, 2, 3],
       [8, 0, 4],
       [7, 6, 5]]

# unicode for draw puzzle in command promt or terminal
left_down_angle = '\u2514'
right_down_angle = '\u2518'
right_up_angle = '\u2510'
left_up_angle = '\u250C'

middle_junction = '\u253C'
top_junction = '\u252C'
bottom_junction = '\u2534'
right_junction = '\u2524'
left_junction = '\u251C'

# bar color
bar = Style.BRIGHT + Fore.CYAN + '\u2502' + Fore.RESET + Style.RESET_ALL
dash = '\u2500'

# Line draw code
first_line = Style.BRIGHT + Fore.CYAN + left_up_angle + dash + dash + dash + top_junction + dash + dash + dash + top_junction + dash + dash + dash + right_up_angle + Fore.RESET + Style.RESET_ALL
middle_line = Style.BRIGHT + Fore.CYAN + left_junction + dash + dash + dash + middle_junction + dash + dash + dash + middle_junction + dash + dash + dash + right_junction + Fore.RESET + Style.RESET_ALL
last_line = Style.BRIGHT + Fore.CYAN + left_down_angle + dash + dash + dash + bottom_junction + dash + dash + dash + bottom_junction + dash + dash + dash + right_down_angle + Fore.RESET + Style.RESET_ALL


# puzzle print function
def print_puzzle(array):
    print(first_line)
    for a in range(3):
        for i in array[a]:
            if i == 0:
                print(bar, Back.RED + ' ' + Back.RESET, end=' ')
            else:
                print(bar, i, end=' ')
        print(bar)
        if a == 2:
            print(last_line)
        else:
            print(middle_line)


# it is the node which store each state of puzzle
class Node:
    def __init__(self, current_node, previous_node, g, h, dir):
        self.current_node = current_node
        self.previous_node = previous_node
        self.g = g
        self.h = h
        self.dir = dir

    def f(self):
        return self.g + self.h


def get_pos(current_state, element):
    pos = [(row, current_state[row].index(element)) for row in range(3) if element in current_state[row]]
    # return (row_index, col index)
    return pos[0]


# it is a distance calculation algo witch calculate the sumation of all the pieces' cost
def euclidianCost(current_state):
    cost = 0
    for row in range(3):
        for col in range(3):
            pos = get_pos(END, current_state[row][col])
            # current row index pos - End row index pos
            # current col index pos - End col index pos 
            cost += abs(row - pos[0]) + abs(col - pos[1])
    return cost


# get possible Nodes
def getAdjNode(node):
    # possible movements list
    listNode = []
    emptyPos = get_pos(node.current_node, 0)

    for dir in DIRECTIONS.keys():
        newPos = (emptyPos[0] + DIRECTIONS[dir][0], emptyPos[1] + DIRECTIONS[dir][1])
        if 0 <= newPos[0] < 3 and 0 <= newPos[1] < 3:
            newState = deepcopy(node.current_node)
            newState[emptyPos[0]][emptyPos[1]] = node.current_node[newPos[0]][newPos[1]]
            newState[newPos[0]][newPos[1]] = 0
            # listNode += [Node(newState, node.current_node, node.g + 1, euclidianCost(newState), dir)]
            listNode.append(Node(newState, node.current_node, node.g + 1, euclidianCost(newState), dir))

    return listNode


# get the best node available among nodes
def getBestNode(openSet):
    firstIter = True

    for node in openSet.values():
        if firstIter or node.f() < bestF:
            firstIter = False
            bestNode = node
            bestF = bestNode.f()
    return bestNode


# this functionn create the smallest path
def buildPath(closedSet):
    node = closedSet[str(END)]
    branch = list()

    while node.dir:  # not ""
        branch.append({
            'dir': node.dir,
            'node': node.current_node
        })
        node = closedSet[str(node.previous_node)]
    branch.append({
        'dir': '',
        'node': node.current_node
    })
    branch.reverse()

    return branch


# retuns the fastest path after calculating the best path using A* algorithm
def main(puzzle):
    open_set = {str(puzzle): Node(puzzle, puzzle, 0, euclidianCost(puzzle), "")}
    closed_set = {}

    while True:
        test_node = getBestNode(open_set)
        closed_set[str(test_node.current_node)] = test_node

        if test_node.current_node == END:
            return buildPath(closed_set)

        adj_node = getAdjNode(test_node)
        for node in adj_node:
            if str(node.current_node) in closed_set.keys() or str(node.current_node) in open_set.keys() and open_set[
                str(node.current_node)].f() < node.f():
                continue
            open_set[str(node.current_node)] = node

        del open_set[str(test_node.current_node)]


def print_message(msg):
    print(dash + dash + right_junction, msg, left_junction + dash + dash)


def menu():
    initial_matrix = [[2, 8, 3],
                      [1, 6, 4],
                      [7, 0, 5]]

    sleep(0.1)
    print(Fore.RED + " [" + Fore.WHITE + "*" + Fore.RED + "]" + Fore.CYAN + " Choose one of the options below. \n")
    sleep(0.1)
    print(Fore.RED + "[1]" + Fore.WHITE + " Default calculation \n")
    sleep(0.1)
    print(Fore.RED + "[2]" + Fore.WHITE + " Custom matrix \n" + Fore.RESET + Style.RESET_ALL)
    print()

    sleep(0.1)
    print_message("Initial")
    print_puzzle(initial_matrix)

    sleep(0.1)
    print_message("Final")
    print_puzzle(END)

    user_input = input(
        Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "8-Puzzle" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + """]
 └──╼ """ + Fore.WHITE + "$ ")
    os.system("cls")
    if user_input == "2":
        first_row = input("first row (sample 1,2,3) : ").split(",")
        middle_row = input("middle row (sample 1,2,3) : ").split(",")
        last_row = input("last row (sample 1,2,3) : ").split(",")
        initial_matrix = [first_row, middle_row, last_row]
        initial_matrix = [[int(el) for el in row] for row in initial_matrix]
        print(initial_matrix)

    return initial_matrix


if __name__ == '__main__':
    # it is start matrix
    initial = menu()

    branchs = main(initial)
    # branchs = buildPath output (List)

    print(Style.BRIGHT + Fore.CYAN + f'total steps : {len(branchs) - 1}' + Fore.RESET + Style.RESET_ALL)
    print()
    print_message("INPUT")
    for b in branchs:
        if b['dir'] != '':
            letter = ''
            if b['dir'] == 'U':
                letter = 'UP'
            elif b['dir'] == 'R':
                letter = "RIGHT"
            elif b['dir'] == 'L':
                letter = 'LEFT'
            elif b['dir'] == 'D':
                letter = 'DOWN'
            print_message(letter)
        print_puzzle(b['node'])
        print()

    print_message('ABOVE IS THE OUTPUT')
