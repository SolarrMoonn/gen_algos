import random
target = "HELLOWORLD"
mutation_rate = 0.1
population_size = 150

def create_population(size, length):
    return [''.join(chr(random.randint(65,90)) for _ in range(length)) for _ in range(size)]

def fitness(solution):
    return sum(s == t for s, t in zip(solution, target))

def mutate(solution):
    ind = random.randint(0, len(solution) - 1)
    return solution[:ind] + chr(random.randint(65, 90)) + solution[ind+ 1: ]
    
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    return parent1[:point] + parent2[point:]

population = create_population(population_size, len(target))

for gen in range(population_size):
    population.sort(key=lambda x: -fitness(x))

    if fitness(population[0]) == len(target):
        print(f"found {gen}, {population[0]}")
        break

    top_15 = population[:20]

    new_population = []
    
    for _ in range(population_size):
        canditdates = random.choices(top_15, k =4)
        parent1 = max(canditdates[:2], key=fitness)
        parent2 = max(canditdates[2:], key=fitness)
        child = crossover(parent1, parent2)
        if random.random() < mutation_rate:
            child = mutate(child)
        new_population.append(child)
    population = new_population
else:
    print(f"Best after 100 gens: '{population[0]}' (fitness={fitness(population[0])})")