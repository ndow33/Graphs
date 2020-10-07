from util import Queue, Stack

visited_rooms = set()

def bfs(starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue a path to the starting vertex
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        # visited = set()
		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            path = q.dequeue()
			# Grab the last vertex from the PATH
            last_vert = path[-1]
			# If that vertex has not been visited...
            if last_vert not in visited_rooms:
				# CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
				  # IF SO, RETURN PATH
                  return path
				# Otherwise Mark it as visited...
                visited_rooms.add(last_vert)
				# Then add A PATH TO its exits to the back of the queue
                for exit in player.current_room.get_exits():
                    # COPY THE PATH
                    new_path = path.copy()
                    # add the new vertex to it
                    new_path.append(player.current_room.get_room_in_direction(exit))
                    # enqueue the new path
                    q.enqueue(new_path)
        return None