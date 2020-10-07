from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects\\adventure\maps\\test_line.txt"
map_file = "projects\\adventure\maps\\test_cross.txt"
# map_file = "projects\\adventure\maps\\test_loop.txt"
# map_file = "projects\\adventure\maps\\test_loop_fork.txt"
# map_file = "projects\\adventure\maps\main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

print('test')
# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room.id)


# construct my own traversal graph
rooms = dict()

'''# get current room id
id = player.current_room.id

# get the exits of the current room
exits = player.current_room.get_exits()
room_exits = dict()
# put them in a dictionary
for exit in exits:
    room_exits[exit] = '?'
# put that dictionary in our rooms dictionary
rooms[id] = room_exits

print(rooms)'''


opposite_dir = dict()
opposite_dir['n'] = 's'
opposite_dir['s'] = 'n'
opposite_dir['e'] = 'w'
opposite_dir['w'] = 'e'

print(opposite_dir['s'])

# this function makes a new dictionary of unknown exits
# for rooms that are new to our rooms dictionary
def new_room(room):
    # get the exits of the current room
    exits = room.get_exits()
    room_exits = dict()
    # put them in a dictionary
    for exit in exits:
        room_exits[exit] = '?'  
    # return that dictionary
    return room_exits


id = player.current_room.id
rooms[id] = new_room(player.current_room)
print(rooms)


# define function to get available exits
def available_exits(room):
    # get the room's id
    room_id = room.id
    # create list to hold available exits
    exits = []
    # put them in a dictionary
    for exit in rooms[room_id]:
        if rooms[room_id][exit] == '?':
            exits.append(exit)
    
    return exits

print(available_exits(player.current_room))

def dft(room):
    # find the list of exits for the given room
    exits = available_exits(room)
    # run this code as long as there are undiscovered exits
    while len(exits) > 0:
        # randomly choose a direction from the list of available exits
        index = random.randint(0, len(exits)-1)
        direction = exits[index]

        # store the current room we're in to a variable so we can reference later once we travel
        old_room = room

        # append that direction to traversal_path
        traversal_path.append(direction)

        # travel that direction 
        player.travel(direction)
        # update the room
        room = player.current_room
        # if the new room is not in our rooms dictionary
        if room.id not in rooms:
            # add it to the dictionary with its exits in a dicionary
            rooms[room.id] = new_room(room)

        # find the opposite direction
        opp = opposite_dir[direction]
        # Make sure the directions are updated for each room
        rooms[room.id][opp] = old_room.id
        rooms[old_room.id][direction] = room.id

        # update the list of exits
        exits = available_exits(room)

dft(player.current_room)
print(rooms)
print(player.current_room.id)


def bfs(room):
    q = Queue()
    visited = set()
    # create a list of room objects
    q.enqueue([room])

    while q.size() > 0:
        # dequeue the list of room objects
        path = q.dequeue()
        # access the most recently added room object
        last_vert = path[-1]
        # if that vertex hasn't been visited
        if last_vert not in visited:
            # check if it has ?'s
            if len(available_exits(last_vert)) > 0:
                return last_vert.id
        # otherwise mark it as visited
        visited.add(last_vert)
        # then add a path to its neighbors to the back of the queue
        for direction in rooms[last_vert.id]:
            # copy the path
            new_path = path.copy()
            # add a new room object to it
            new_path.append(last_vert.get_room_in_direction(direction))
            # enqueue the new path
            q.enqueue(new_path)
        
print(bfs(player.current_room))




# reset the player at the starting room
player.current_room = world.starting_room

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room.id)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
'''player.current_room.print_room_description(player)
exits = player.current_room.get_exits()
for e in exits:
    player.travel(e)
    player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")'''