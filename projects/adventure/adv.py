from room import Room
from player import Player
from world import World
from util import Stack, Queue  # These may come in handy

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
# create a dictionary
d = dict()

# get the current room id
cur_id = player.current_room.id

# get the room's exits
cur_exits = player.current_room.get_exits()

# make another dictionary of the exits
d2 = dict()

# mark all exits with a question mark
for exit in cur_exits:
    # print(player.current_room.get_room_in_direction(exit))
    d2[exit] = '?'

# store d2 in d
d[cur_id] = d2

counter = 0
# while len(visited_rooms) < len(room_graph):
while counter < 2:    
    # ?'s get priority
    for direction in d[cur_id]:
        if '?' in d[cur_id][direction]:
            print(direction)
            print('yep')
    while 'n' in d[cur_id]:
        if d[cur_id]['n'] == '?':
            # add 'n' to our traversal path
            traversal_path.append('n')
            # update the value of 'n' in d2
            d[cur_id]['n'] = player.current_room.get_room_in_direction('n').id
            # travel to the next room
            player.travel('n')
            # update cur_id
            cur_id = player.current_room.id
            # if the cur_id is not in the visited rooms
            if cur_id not in visited_rooms:
                # update the visited rooms
                visited_rooms.add(cur_id)
                # get the room's exits
                cur_exits = player.current_room.get_exits()
                # create a new dictionary of directions
                d2 = dict()
                # mark all exits with a question mark
                for exit in cur_exits:
                    # print(player.current_room.get_room_in_direction(exit))
                    d2[exit] = '?'
                # update dictionary
                d[cur_id] = d2
        else:
            break

    print(d)
    while 's' in d[cur_id]:
        # add 'n' to our traversal path
        traversal_path.append('s')
        # update the value of 'n' in d2
        d[cur_id]['s'] = player.current_room.get_room_in_direction('s').id
        # travel to the next room
        player.travel('s')
        # update cur_id
        cur_id = player.current_room.id
        # if the room hasn't been visited
        if cur_id not in visited_rooms:
            # update the visited rooms
            visited_rooms.add(cur_id)
            # get the room's exits
            cur_exits = player.current_room.get_exits()
            # create a new dictionary of directions
            d2 = dict()
            # mark all exits with a question mark
            for exit in cur_exits:
                # print(player.current_room.get_room_in_direction(exit))
                d2[exit] = '?'
            # update dictionary
            d[cur_id] = d2

    while 'e' in d[cur_id]:
        # add 'n' to our traversal path
        traversal_path.append('e')
        # update the value of 'n' in d2
        d[cur_id]['e'] = player.current_room.get_room_in_direction('e').id
        # travel to the next room
        player.travel('e')
        # update cur_id
        cur_id = player.current_room.id
        # if the room hasn't been visited
        if cur_id not in visited_rooms:
            # update the visited rooms
            visited_rooms.add(cur_id)
            # get the room's exits
            cur_exits = player.current_room.get_exits()
            # create a new dictionary of directions
            d2 = dict()
            # mark all exits with a question mark
            for exit in cur_exits:
                # print(player.current_room.get_room_in_direction(exit))
                d2[exit] = '?'
            # update dictionary
            d[cur_id] = d2

    while 'w' in d[cur_id]:
        # add 'n' to our traversal path
        traversal_path.append('w')
        # update the value of 'n' in d2
        d[cur_id]['w'] = player.current_room.get_room_in_direction('w').id
        # travel to the next room
        player.travel('w')
        # update cur_id
        cur_id = player.current_room.id
        # if the room hasn't been visited
        if cur_id not in visited_rooms:
            # update the visited rooms
            visited_rooms.add(cur_id)
            # get the room's exits
            cur_exits = player.current_room.get_exits()
            # create a new dictionary of directions
            d2 = dict()
            # mark all exits with a question mark
            for exit in cur_exits:
                # print(player.current_room.get_room_in_direction(exit))
                d2[exit] = '?'
            # update dictionary
            d[cur_id] = d2

    counter +=1
print(f'current room: {cur_id}')    
print(d)
print(traversal_path)
print(len(room_graph))
# reset starting room
player.current_room = world.starting_room
# reset set
visited_rooms = set()
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room.id)

print(visited_rooms)
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