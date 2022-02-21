import copy

WALL = "X"
WAY = " " 
OPEN = '#'
CLOSED = '*'
PATH = 'O'
START = 'S'
END = 'E'


class Map():
    def __init__(self, new_map = None, new_start = None, new_end = None):
        if new_map is None or new_start is None or new_end is None:
            self.map, self.start, self.end = parse_input()
        else:
            self.map = new_map
            self.start = new_start
            self.end = new_end
    def set_coord_value(self, coord, value):
        self.map[coord.get_y()][coord.get_x()] = value
    def get_coord_value(self, coord):
        return self.map[coord.get_y()][coord.get_x()]
    def get_start(self):
        return self.start.copy()
    def get_end(self):
        return self.end.copy()
    def print_map(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                print(self.map[y][x],end='')
            print()
        print()
    def print_popisek(self):
        print('-' * 20)
        print("OPEN = " + OPEN)
        print("CLOSED = " + CLOSED)
        print("PATH = " + PATH)
        print("START = " + START)
        print("END = " + END)
        print("UNTOUCHED NODE = space")
        print('-' * 20)
        print()
    def update_map(self, frontier, closed, path=[]):

        for coord in frontier:
            self.set_coord_value(coord, OPEN)
        for coord in closed:
            self.set_coord_value(coord, CLOSED)
        for coord in path:
            self.set_coord_value(coord, PATH)
        self.set_coord_value(self.start, START)
        self.set_coord_value(self.end, END)
    def copy(self):
        return Map(self.map.copy(), self.start.copy(), self.end.copy())
    def print_ending_info(self, path, frontier, closed):
        print("Length of the path: " + str(len(path) - 1))
        print("Nodes expanded: " + str(len(frontier) + len(closed) - 1))
        print()
    def end_print(self, path, frontier, closed):
        self.print_map()
        self.print_popisek()
        self.print_ending_info(path, frontier, closed)
    def case_endIsStart(self):
        if self.end == self.start:
            self.update_map([], [], path=[self.start])
            self.end_print([self.start], [], [self.start])
            return True
        return False
            
class Coordinates():
    current_map = None
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def manhattan_distance(self, other):
        return abs(self.x - other.get_x()) + abs(self.y - other.get_y())
    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)
    def copy(self):
        return copy.deepcopy(self)
    def set_current_map(self, new_map):
        Coordinates.current_map = new_map
    def is_neigbour(self, neighbour):
        return self.current_map.get_coord_value(neighbour) != WALL
    def get_neigbours(self):
        neigbours = []
        x = self.x
        y = self.y
        a = Coordinates(x+1, y)
        if self.is_neigbour(a):
            neigbours.append(a)
        a = Coordinates(x-1, y)
        if self.is_neigbour(a):
            neigbours.append(a)
        a = Coordinates(x, y+1)
        if self.is_neigbour(a):
            neigbours.append(a)
        a = Coordinates(x, y-1)
        if self.is_neigbour(a):
            neigbours.append(a)
        
        return neigbours
    def __eq__(self, other):
        
        if self.x == other.x and self.y == other.y:
            return True
        return False

def get_raw_input():
    
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break;
        lines.append(line)
    for line in lines:
        line.splitlines()
    return lines
def reconstruct_path_recursive(prev_table, x):
    if prev_table[str(x)] is None:
        a = [x]
        return a
    
    b = reconstruct_path(prev_table, prev_table[str(x)])
    b.append(x)
    return b
def reconstruct_path(prev_table, x):
    path = []
    coord = x
    while not prev_table[str(coord)] is None:
        path.insert(0, coord)
        coord = prev_table[str(coord)]
    path.insert(0, coord)
    return path
        
def load_map():
    return Map()
def divide_input(raw_input):
    bludiste = []
    start_info = ''
    end_info = ''
    for line in raw_input:
        if WALL in line:
            bludiste.append(line)
        elif "start" in line:
            start_info = line
        elif 'end' in line:
            end_info = line
    return (bludiste, start_info, end_info)
    
def create_bludiste_field(bludiste):
    field = []
    
    for line in bludiste:
        row = []
        for letter in line:
            row.append(letter)
        field.append(row)
    return field

def parse_string_to_coordinates(line):
    line = line.split()
    x = 0
    y = 0
    for i in range(len(line)):
        if ',' in line[i]:
            x = int(line[i].strip(','))
            y = int(line[i+1])
            break
    return Coordinates(x, y)

# reads the whole input and then returns the map of the bludiste
# the start coordinates and the end coordinates
# the inputed starts and end must be in format "string num1, num2 string"
# otherwise it wont work
def parse_input():
    raw_input = get_raw_input()
    bludiste_string, start_string, end_string = divide_input(raw_input)
    bludiste = create_bludiste_field(bludiste_string)
    start = parse_string_to_coordinates(start_string)
    end = parse_string_to_coordinates(end_string)

    
    return (bludiste, start, end)
