import random


POPULATION_SIZE = 10
INDIVIDUAL_LENGTH = 20
MUTATION_CHANCE = 0.1

TARGET_VALUE = 19


def generate_starting_generation():
    generation = []
    # TODO: initialize first generation
    return generation


def fitness(individual):
    # TODO: return sum of values in individual
    return 0


def rank_generation(generation):
    return sorted(generation, key=lambda ind: fitness(ind), reverse=True)


def pair(generation):
    # TODO: return a list of couples, the input is an already sorted list
    return []


def mate(individual1, individual2):
    # TODO: return child
    # first half is copied from parent1 the rest from parent2
    return []


def mutate(individual):
    # TODO: mutate genes at each position with MUTATION_CHANCE probability
    pass


def generate_new_generation(generation):
    # TODO: generate new generation like so
    # keep the first half of the current population (the best individuals)
    # generate new children using pairing and mating
    return []


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
