# import graph library
import networkx as nx
import matplotlib.pyplot as plt
import sys

# if argument provided, get the input file from the argument
if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = "input.txt"

# read the input file
with open(input_file, 'r') as f:
    lines = f.readlines()

# close the file
f.close()

# Get the rooms and corridors from the first line
rooms = int(lines[0].split()[0])
corridors = int(lines[0].split()[1])

# Get the color of the rooms from the second line and convert it to a array of strings
room_colors = lines[1].split()
# append the goal room color to the end of the array
room_colors.append("goal")

# Get the starting rooms from the third line
captain_start = int(lines[2].split()[0])
lieutenant_start = int(lines[2].split()[1])


# create a map, where the key is the color string and the value is a list of rooms with that color
room_map = {}
for i in range(rooms-1):
    if room_colors[i] in room_map:
        room_map[room_colors[i]].append(i)
    else:
        room_map[room_colors[i]] = [i]

# create a map, where the key is the room number and the value is currently blank
room_map2 = {}
for i in range(rooms-1):
    room_map2[i] = []


# Create a graph
game_board = nx.DiGraph()

# add a node for each room (skip 0)
for i in range(rooms, 0, -1):
    game_board.add_node(i, color=room_colors[i-1], node_color='lightblue')

# change the node_color for the starting rooms and goal
game_board.nodes[captain_start]['node_color'] = 'red'
game_board.nodes[lieutenant_start]['node_color'] = 'green'
game_board.nodes[rooms]['node_color'] = 'yellow'


# finish reading the input file, where the line format is "room1 room2 color"
# make edges directed
for i in range(3, len(lines)):
    room1 = int(lines[i].split()[0])
    room2 = int(lines[i].split()[1])
    color = lines[i].split()[2]

    # add an edge between the two rooms
    game_board.add_edge(room1, room2, color=color)


# add labels for the edges
edge_labels = nx.get_edge_attributes(game_board, 'color')
room_labels = nx.get_node_attributes(game_board, 'color')


# draw the graph with labels
pos = nx.spring_layout(game_board)
nx.draw(game_board, pos, with_labels=True, verticalalignment='top', node_color=[game_board.nodes[i]['node_color'] for i in game_board.nodes],
        node_size=1500, font_weight='bold')
nx.draw_networkx_edge_labels(game_board, pos, edge_labels=edge_labels)
# add room labels under the number
nx.draw_networkx_labels(game_board, pos, labels=room_labels, font_size=8,
                        font_color='black', font_weight='bold', verticalalignment='bottom')


# Create a Game State class

class GameState:
    def __init__(self, board_graph, captain_location, lieutenant_location, move_name):
        self.board = board_graph
        self.captain = captain_location
        self.lieutenant = lieutenant_location
        self.move_name = move_name

    # function to check if the game is over
    def is_goal(self):
        if self.board.nodes[self.captain]['color'] == 'goal' or self.board.nodes[self.lieutenant]['color'] == 'goal':
            return True
        else:
            return False

    # function to get the possible moves from current game state
    def get_possible_moves(self):
        # Get a list of the rooms that the captain can move to. Captain can move through any edge with the same color as lieutenant's room
        captain_moves = list(self.board.successors(self.captain))
        captain_valid_moves = []
        for item in captain_moves:
            if self.board.get_edge_data(self.captain, item)['color'] == self.board.nodes[self.lieutenant]['color']:
                captain_valid_moves.append(item)

        # Get a list of the rooms that the lieutenant can move to. Lieutenant can move through any edge with the same color as captain's room
        lieutenant_moves = list(self.board.successors(self.lieutenant))
        lieutenant_valid_moves = []
        for item in lieutenant_moves:
            if self.board.get_edge_data(self.lieutenant, item)['color'] == self.board.nodes[self.captain]['color']:
                lieutenant_valid_moves.append(item)

        # Create a list of game states that can be reached from the current game state
        game_states = []
        for item in lieutenant_valid_moves:
            game_states.append(
                GameState(self.board, self.captain, item, "L" + str(item)))
        for item in captain_valid_moves:
            game_states.append(
                GameState(self.board, item, self.lieutenant, "R" + str(item)))

        return game_states

    # function to print the game state
    def print_state(self):
        print("Captain: ", self.captain, " Lieutenant: ",
              self.lieutenant)

    def move_name(self):
        return self.move_name

    def __eq__(self, other):
        return self.captain == other.captain and self.lieutenant == other.lieutenant


# Create a new game state
game = GameState(game_board, captain_start, lieutenant_start, "Start")


# Conduct a BFS search to find the shortest path to the goal do not revisit nodes
def bfs_search(game_state):
    queue = []
    visited = []
    queue.append([game_state])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node.is_goal():
            return path
        if node not in visited:
            for next_node in node.get_possible_moves():
                new_path = list(path)
                new_path.append(next_node)
                queue.append(new_path)
            visited.append(node)
    return None


# print the moves in the shortest path on a single line, skip the first move
shortest_path = bfs_search(game)
output = ""
# if there is no path, print "NO PATH"
if shortest_path is None:
    output = "NO PATH"
else:
    for i in range(1, len(shortest_path)):
        output += shortest_path[i].move_name

print(output)
