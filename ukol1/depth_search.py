from common_utils import reconstruct_path, Map

def depth_search(new_map):
    progress_map = new_map.copy()
    if new_map.case_endIsStart():
        return [new_map.get_start()]
    prev_table = {}
    current_position = new_map.get_start()
    current_position.set_current_map(new_map)
    frontier = current_position.get_neigbours()
    closed = []
    closed.append(current_position)
    prev_table[str(current_position)] = None
    
    for i in frontier:
        prev_table[str(i)] = current_position
    
    solution = []
    
    while len(frontier) > 0:
        x = frontier[-1]
        new_neighbours = x.get_neigbours()
        if new_map.get_end() in new_neighbours:
            prev_table[str(new_map.get_end())] = x
            solution.extend(reconstruct_path(prev_table, new_map.get_end()))
            break
        for neighbour in new_neighbours:
            if neighbour not in frontier and neighbour not in closed:
                frontier.append(neighbour)
                prev_table[str(neighbour)] = x
        frontier.remove(x)
        closed.append(x)
        
        progress_map.update_map(frontier, closed)
        progress_map.print_map()
    progress_map.update_map(frontier, closed, path=solution)
    progress_map.end_print(solution, frontier, closed)
    return solution

new_map = Map()
solution = depth_search(new_map)