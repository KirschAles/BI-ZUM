from common_utils import reconstruct_path, Map

def print_list(liist):
    for item in liist:
        print(item, end=" ")
    print()

def enque(frontier, coord, goal, dist_table):
    coord_heuretic = coord.manhattan_distance(goal)
    isInserted = False
    for i in range(len(frontier)):
        front_heuretic = frontier[i].manhattan_distance(goal)
        if dist_table[str(coord)] + coord_heuretic < dist_table[str(frontier[i])] + front_heuretic:
            frontier.insert(i, coord)
            isInserted = True
            break
    if not isInserted:
        frontier.append(coord)
def jump_que(frontier, coord, goal, dist_table):
    frontier.remove(coord)
    enque(frontier, coord, goal, dist_table)
def astar_search(new_map):
    if new_map.case_endIsStart():
        return [new_map.get_start()]
    progress_map = new_map.copy()
    goal = new_map.get_end()
    prev_table = {}
    dist_table = {}
    current_position = new_map.get_start()
    current_position.set_current_map(new_map)
    frontier = []
    neighbours = current_position.get_neigbours()
    for neighbour in neighbours:
        dist_table[str(neighbour)] = 1
        enque(frontier, neighbour, goal, dist_table)
    closed = []
    closed.append(current_position)
    prev_table[str(current_position)] = None
    
    for i in frontier:
        prev_table[str(i)] = current_position
    
    solution = []
    
    while len(frontier) > 0:
        x = frontier[0]
        if goal == x:
            solution.extend(reconstruct_path(prev_table, x))
            break
        new_neighbours = x.get_neigbours()
        for neighbour in new_neighbours:
            if neighbour not in closed:
                goal_dist = neighbour.manhattan_distance(goal)
                dist = dist_table[str(x)] + 1 + goal_dist
                small_dist = dist_table[str(x)] + 1
                if neighbour not in frontier or dist_table[str(neighbour)] + goal_dist > dist:
                    prev_table[str(neighbour)] = x
                    dist_table[str(neighbour)] = small_dist
                    if neighbour not in frontier:
                        enque(frontier, neighbour, goal, dist_table)
                    else:
                        jump_que(frontier, neighbour, goal, dist_table)
        frontier.remove(x)
        closed.append(x)
        
        progress_map.update_map(frontier, closed)
        progress_map.print_map()
    progress_map.update_map(frontier, closed, path=solution)
    progress_map.end_print(solution, frontier, closed)
    return solution

new_map = Map()
solution = astar_search(new_map)