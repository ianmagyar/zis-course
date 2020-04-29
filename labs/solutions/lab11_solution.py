import random


POPULATION_SIZE = 10
INDIVIDUAL_LENGTH = 20
MUTATION_CHANCE = 0.1

TARGET_VALUE = 19


def fitness(individual):
    return sum(individual)


def generate_starting_generation():
    generation = []
    for _ in range(POPULATION_SIZE):
        individual = [random.choice([0, 1]) for _ in range(INDIVIDUAL_LENGTH)]
        generation.append(individual)
    return generation


def pair(generation):
    return [(generation[2 * i], generation[2 * i + 1])
            for i in range(POPULATION_SIZE // 2)]


def mate(individual1, individual2):
    return individual1[:INDIVIDUAL_LENGTH // 2] + individual2[INDIVIDUAL_LENGTH // 2:]


def mutate(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_CHANCE:
            individual[i] = 1 if individual[i] == 0 else 0


def rank_generation(generation):
    return sorted(generation, key=lambda ind: fitness(ind), reverse=True)


def generate_new_generation(generation):
    best = rank_generation(generation)[:POPULATION_SIZE // 2]

    children = []
    pairs = pair(generation)
    for parent1, parent2 in pairs:
        child = mate(parent1, parent2)
        children.append(child)

    new_gen = best + children
    for individual in new_gen:
        mutate(individual)

    return new_gen


if __name__ == '__main__':
    counter = 1
    current = generate_starting_generation()
    while fitness(rank_generation(current)[0]) < TARGET_VALUE:
        print("GENERATION", counter)
        print('best fitness:', fitness(rank_generation(current)[0]))
        print()
        current = generate_new_generation(current)
        counter += 1

    print(current)
    for individual in current:
        print(fitness(individual))
