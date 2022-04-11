from common_utils import reconstruct_path, Map

def hungry_enque(frontier, coord, goal):
    isInserted = False
    for i in range(len(frontier)):
        if coord.euclidean_sq_distance(goal) < frontier[i].euclidean_sq_distance(goal):
            frontier.insert(i, coord)
            isInserted = True
            break
    if not isInserted:
        frontier.append(coord)
def enque_neighbours(frontier, neighbours, goal):
    for neighbour in neighbours:
        hungry_enque(frontier, neighbour, goal)
def hungry_search(new_map):
    progress_map = new_map.copy()
    if new_map.case_endIsStart():
        return [new_map.get_start()]
    prev_table = {}
    current_position = new_map.get_start()
    current_position.set_current_map(new_map)
    print(current_position.get_x(), current_position.get_y())
    frontier = []
    neighbours = current_position.get_neigbours()
    enque_neighbours(frontier, neighbours, new_map.get_end())
    closed = []
    closed.append(current_position)
    prev_table[str(current_position)] = None
    
    for i in frontier:
        prev_table[str(i)] = current_position
    
    solution = []
    
    while len(frontier) > 0:
        x = frontier[0]
        new_neighbours = x.get_neigbours()
        if new_map.get_end() in new_neighbours:
            prev_table[str(new_map.get_end())] = x
            solution.extend(reconstruct_path(prev_table, new_map.get_end()))
            break
        for neighbour in new_neighbours:
            if neighbour not in frontier and neighbour not in closed:
                hungry_enque(frontier, neighbour, new_map.get_end())
                prev_table[str(neighbour)] = x
        frontier.remove(x)
        closed.append(x)
        #progress_map.update_map(frontier, closed)
        #progress_map.print_map()        
    
    return solution
