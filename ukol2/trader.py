import random
import re
from common_utils import *
from hungry_search import hungry_search

class Gene():
    total_unfitness = 0
    total_fitness = 0
    def __init__(self, gene):
        self.gene = gene.copy()
        self.fitness = 0
        self.weight = 0
        self.unfitness = 0
        self.length = len(gene)
    def create_fitness(self):
        Gene.total_fitness -= self.fitness
        self.fitness = self.total_unfitness - self.unfitness
        Gene.total_fitness += self.fitness
    def set_unfitness(self, unfitness):
   #     print(self.unfitness)
    #    print(self.total_unfitness)
        Gene.total_unfitness -= self.unfitness
        self.unfitness = unfitness
        Gene.total_unfitness += unfitness
    #    print("unfitness: ")
     #   print(self.total_unfitness)
      #  print(self.unfitness)
    def create_weight(self):
        self.weight = self.fitness/float(self.total_fitness)
    def get_weight(self):
        return self.weight
    def get_fitness(self):
        return self.fitness
    def get_gene(self):
        return self.gene.copy()
    def switch_genes(self, index1, index2):
        temp = self.gene[index1]
        self.gene[index1] = self.gene[index2]
        self.gene[index2] = temp
    def mutate(self):
    
        gene_choices = list(range(len(self.gene)))
        index1 = random.choice(gene_choices)
        gene_choices.remove(index1)
        index2 = random.choice(gene_choices)
        self.switch_genes(index1, index2)
    def get_length(self):
        return self.length
    def index(self, char):
        return self.gene.index(char)
    def __getitem__(self, index):
        return self.gene[index]
    def __str__(self):
        return (str(self.gene)+ ' ' + str(self.unfitness)+ ' ' + str(self.total_unfitness)+ ' ' +
        str(self.fitness) + ' ' + str(self.total_fitness) + ' ' + str(self.weight))
    @staticmethod
    def clear():
        Gene.total_unfitness = 0
        Gene.total_fitness = 0
def convert_matrice_tostr(matrice):
    for line in matrice:
        for i in range(len(line)):
            line[i] = float(line[i])
def read_matrice():
    lines = []
    print("Write the matrix")
    
    while True:
        try:
            line = input()
        except EOFError:
            break;
        lines.append(line)
    for line in lines:
        line.splitlines()
        
    for i in range(len(lines)):
        lines[i] = re.split(' |,',lines[i])
    print(lines)
    print("Liiiiines")
    convert_matrice_tostr(lines)
    return lines
def get_matrice():
    matrice = read_matrice()
    convert_matrice_tostr(matrice)
    return matrice
#generates a population of randomly put together series of towns
def create_population(length_of_gene, population_size):
    towns = list(range(length_of_gene))
    population = []
   # print("gene lenght: " + str(length_of_gene) + "population_size " + str(population_size))
    for i in range(population_size):
        instance = []
        priv_towns = towns.copy()
        while len(priv_towns) > 0:
            a = random.choice(priv_towns)
            instance.append(a)
            priv_towns.remove(a)
        population.append(Gene(instance))
    return population
def how_unfit(path, matrice):
    unfitness = 0
    length = len(path)
    #print(path)
    for i in range(length):
        unfitness += matrice[path[i]][path[i-1]]
    return unfitness
def add_unfitness(population, matrice):
    for item in population:
        item.set_unfitness(how_unfit(item.get_gene(), matrice))
def add_fitness(population):
    for item in population:
        item.create_fitness()
def add_weights(population):
    for item in population:
        item.create_weight()
def add_classifiers(population, matrice):
    Gene.clear()
    add_unfitness(population, matrice)
    #print(population[0])
    add_fitness(population)
    #print(population[0])
    add_weights(population)
def random_selection(population):
    variable = random.random()
    selected = None
    for item in population:
        selected = item
        variable -= selected.get_weight()
        if variable < 0:
            break
    return selected
def find_best(new_population):
    best_member = new_population[0]
    for member in new_population:
        if member.get_fitness() > best_member.get_fitness():
            best_member = member
    return best_member
def ox_crossover(parent1, parent2):
    child = [];
    cross_point1 = random.choice(range(len(parent1.get_gene())))
    cross_point2 = random.choice(range(cross_point1, parent1.get_length()))
    
    for i in range(cross_point1, cross_point2+1):
        child.append(parent1[i])
    #child_set = set(child)
    remaining_genes = [x for x in parent2.get_gene() if x not in child]
    for i in range(cross_point1):
        child.insert(i, remaining_genes.pop(0))
    child.extend(remaining_genes)
        
    return Gene(child)

def pmx_crossover(parent1, parent2):
    cross_point1 = random.choice(range(len(parent1.get_gene())))
    cross_point2 = random.choice(range(cross_point1, parent1.get_length()))
    
    child = []
    for i in range(cross_point1, cross_point2+1):
        child.append(parent1[i])
    for i in range(cross_point1):
        if parent2[i] not in child:
            child.insert(i, parent2[i])
        else:
            noad = parent2[parent1.index(parent2[i])]
            while noad in child:
                noad = parent2[parent1.index(noad)]
            child.insert(i, noad)
    for i in range(cross_point2+1, parent1.get_length()):
        if parent2[i] not in child:
            child.append(parent2[i])
        else:
            noad = parent2[parent1.index(parent2[i])]
            while noad in child:
                noad = parent2[parent1.index(noad)]
            child.append(noad)

    return Gene(child)
    
    
def reproduce(parent1, parent2, algorithm):
    if algorithm == 0:
        return ox_crossover(parent1, parent2)
    else:
        return pmx_crossover(parent1, parent2)
def print_pop(population):
    for i in population:
        print(i)

def max_first(positions):
    max_val = 0
    for a in positions:
        if a[0] > max_val:
            max_val = a[0]
    return max_val

def max_second(positions):
    max_val = 0
    for a in positions:
        if a[1] > max_val:
            max_val = a[1]
    return max_val
def print_current_look(travel, town_positions):
    print(travel)
    print(town_positions)
    max_x = max_first(town_positions)
    max_y = max_second(town_positions)
    print(max_x)
    print(max_y)
    map_template = []
    boundary_row = ['#']*(max_x+2)
    map_template.append(boundary_row)
    for i in range(max_y):
        row = []
        row.append('#')
        for j in range(max_x):
            row.append(' ')
        row.append('#')
        map_template.append(row)
    map_template.append(boundary_row)
        
    paths = []
    for i in range(len(town_positions)):
        paths.extend(hungry_search(Map(map_template.copy(), 
                                       new_start=Coordinates(town_positions[travel[i-1]][0], town_positions[travel[i-1]][1]), 
                                       new_end=Coordinates(town_positions[travel[i]][0], town_positions[travel[i]][1]))))
    
    for path in paths:
        map_template[path.get_y()][path.get_x()] = '.'
    for position in town_positions:
        map_template[position[1]][position[0]] = 'M'
    
    for i in range(max_y+2):
        for j in range(max_x+2):
            print(map_template[i][j], end='')
        print()
def genetic_algorithm(population, matrice, unchanged_limit, mutation_chance, algorithm, positions):
    #sets random variable of population as best_member
    # wont realy affect anythin
    same_values = 0
    #print(matrice)
    #print(population[0].get_gene())
    add_classifiers(population, matrice)
   # print_pop(population)
    best_member = find_best(population)
    while same_values < unchanged_limit:
        new_population = []
        for i in range(len(population)):
            parent1 = random_selection(population)
            parent2 = random_selection(population)
            child = reproduce(parent1, parent2, algorithm)
            #print(child)
            if (random.random() < mutation_chance):
                child.mutate()
            new_population.append(child)
            
        add_classifiers(new_population, matrice)

        new_best_member = find_best(new_population)
        if new_best_member.unfitness < best_member.unfitness:
            best_member = new_best_member
            same_values = 0
        else:
            same_values += 1
        population = new_population
        print('Distance')
        print(best_member.unfitness)
        #print_current_look(best_member, positions)
    return best_member.get_gene()


def get_positions(fileName):
    positions = open(fileName, 'r')
    
    lines = positions.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        lines[i] = lines[i].split(',')
        lines[i][0] = int(lines[i][0])
        lines[i][1] = int(lines[i][1])
    return lines
    
    
def main():
    size_of_population = 1000
    unchanged_limit = 20
    mutation_chance = 0.3
    algorithm = 1
    matrice = get_matrice()
    assert(len(matrice) != 0)
    gene_length = len(matrice[0])
    if gene_length == 1:
        print(matrice[0])
        return 0
    
    population = create_population(gene_length, size_of_population)
    positions = get_positions('mapa10.txt')
    best_way = genetic_algorithm(population, 
                                 matrice, 
                                 unchanged_limit, 
                                 mutation_chance, 
                                 algorithm, 
                                 positions)
    print(best_way)
if __name__ == '__main__':
    main()    
