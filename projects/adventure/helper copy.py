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
# map_file = "projects\\adventure\maps\\test_cross.txt"
# map_file = "projects\\adventure\maps\\test_loop.txt"
map_file = "projects\\adventure\maps\\test_loop_fork.txt"
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

'''while len(rooms) < len(room_graph):
# find a room that hasn't been explored
    id = player.current_room.id
    # if the room hasn't been visited
    if id not in rooms:
        # find its exits
        exits = player.current_room.get_exits()
        room_exits = dict()
        # put them in a dictionary
        for exit in exits:
            room_exits[exit] = '?'
        # put that dictionary in our rooms dictionary
        rooms[id] = room_exits
    
    # check to see if the direction is a valid exit
    if 'n' in rooms[id] and rooms[id]['n'] == '?':

        # get the id of the room in that direction
        new_id = player.current_room.get_room_in_direction('n').id
        rooms[id]['n'] = new_id

        # travels and logs that direction
        player.travel('n')
        traversal_path.append('n')
        
        # if the new id isn't in our rooms dictionary
        if new_id not in rooms:
            # find its exits
            exits = player.current_room.get_exits()
            room_exits = dict()
            # add them to a dictionary
            for exit in exits:
                room_exits[exit] = '?'
            # put that dictionary in the rooms dictionary
            rooms[new_id] = room_exits
            rooms[new_id]['s'] = id'''

    


# reset the player at the starting room
player.current_room = world.starting_room
print(rooms)
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