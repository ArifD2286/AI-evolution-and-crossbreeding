import random
import string


GENES = string.ascii_letters + string.digits + " "

POPULATION_SIZE = 200
MUTATION_RATE = 0.20

def random_char():
    return random.choice(GENES)

def create_individual(length):
    """A random guess of the correct length."""
    return [random_char() for _ in range(length)]

def fitness(individual, target):
    """How many letters are in the correct position."""
    return sum(1 for a, b in zip(individual, target) if a == b)

def crossover(parent1, parent2):
    """Mix two parents letter by letter to make a child."""
    child = []
    for a, b, in zip(parent1, parent2):
        child.append(a if random.random() < 0.5 else b)
    return child

def mutate(individual):
    """Randomly change a few letters."""
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = random_char()
    return individual

def select_parent(population, target):
    """Pick a decent parent by comparing a few random candidates (tournament selection)."""
    contenders = random.sample(population, 5)
    contenders.sort(key=lambda ind: fitness(ind, target), reverse=True)
    return contenders[0]

def main():
    target = input("Enter the target phrase: ")
    target = list(target)
    length = len(target)

    population = [create_individual(length) for _ in range(POPULATION_SIZE)]

    generation = 0
    while True:
        generation += 1

        population.sort(key=lambda ind: fitness(ind, target), reverse=True)
        best = population[0]
        best_fitness = fitness(best, target)

        print(f"Gen {generation}: {''.join(best)} (fitness {best_fitness}/{length})")

        if best_fitness == length:
            print(f"\nSolved in {generation} generations!")
            break

        new_population = [best] # keep the best guess (elitism)
        while len(new_population) < POPULATION_SIZE:
            parent1 = select_parent(population, target)
            parent2 = select_parent(population, target)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population


if __name__ == "__main__":
    main()
