import random

target = "HELLO"
population_size = 100
mutation_rate = 0.1

def create_population(size, length):
    return [''.join(chr(random.randint(65,91)) for _ in range(length)) for _ in range(size)]

def fitness(solution):
    return sum(s == t for s, t in zip(solution, target))

def mutate(solution):
    ind = random.randint(0, len(solution) - 1)
    return solution[:ind] + chr(random.randint(65, 90)) + solution[ind:]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    return parent1[:point] + parent2[point:]

population = create_population(population_size, len(target))

for gen in range(population_size):
    population.sort(key=lambda x: -fitness(x))

    if fitness(population[0]) == len(target):
        print(f"found {gen}, {population[0]}")
        break

    top_15 = population[:15]

    new_population = []
    
    for _ in range(population_size):
        parent1, parent2 = random.choices(top_15, k=2)
        child = crossover(parent1,parent2)

        new_population.append(child)
    population = new_population
