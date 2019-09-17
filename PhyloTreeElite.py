import numpy as np


def random():
    return np.random.rand()


#  +++ DISCOVER PHYLO TREE +++


def create_species():
    species = np.array(np.empty([_SPE_SIZE, _SPE_SIZE], dtype=float), subok=True)

    for i in range(_SPE_SIZE):
        species[i] = np.random.randint(2, size=_SPE_SIZE)

    return species


def represent_species():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    letters_species = []

    for i in range(_SPE_SIZE):
        letters_species.append(letters[i])

    return letters_species


def create_distance(species):
    distance = np.array(np.zeros([_SPE_SIZE, _SPE_SIZE], dtype=float), subok=True)

    start = -1
    for i in range(_SPE_SIZE):
        start += 1
        for j in range(start, _SPE_SIZE):
            distance[i][j] = _NULL_VALUE

    for i in range(_SPE_SIZE):
        for j in range(_SPE_SIZE):
            for k in range(_SPE_SIZE):
                if i > j:
                    if species[i][k] != species[j][k]:
                        distance[i][j] += 1

    return distance


def discover_similar(distance, size):
    min_distance = np.amin(distance)
    min_ind = np.where(distance == min_distance)
    min_row, min_col = min_ind[0][0], min_ind[1][0]
    min_value = distance[min_ind[0][0]][min_ind[1][0]]

    for i in range(size):
        for j in range(size):
            if i > j:  # only the lower half of the matrix
                if i == min_col:  # if it's the minor row
                    if distance[i][j] != _NULL_VALUE:  # and a valid value
                        distance[i][j] = (distance[min_col][j] + distance[min_row][j]) / 2

                else:  # if not the minor row of the union
                    if i != min_row:  # and not the bigger, so, the other rows
                        if j == min_col:  # where the column of the line is equal the minor column of the union
                            distance[i][j] = (distance[i][min_col] + distance[i][min_row] +
                                              distance[min_col][i] + distance[min_row][i] - 2 * _NULL_VALUE) / 2

    new_distance = np.array(np.delete(np.delete(distance, min_row, axis=1), min_row, axis=0), subok=True)

    return new_distance, min_row, min_col, min_value


def discover_tree(distance, letters, distance_path, letters_path):
    size = _SPE_SIZE
    similar = distance

    for size in range(_SPE_SIZE, 1, -1):
        #  calculates the distance calling the function discover_similar
        print("STEP #", _SPE_SIZE - size, "\n", similar)
        similar, min_row, min_col, min_value = discover_similar(similar, size)
        distance_path.append(min_value)

        #  mounts the tree
        letters_path.append([letters[min_col], letters[min_row], letters[min_col] + letters[min_row]])
        letters[min_col] = letters[min_col] + letters[min_row]
        letters.remove(letters[min_row])

    return similar


def create_tree_fitness(letters_path):
    species_fitness = []
    for sublist in letters_path:
        for string in sublist:
            for letter in string:
                species_fitness.append(letter)

    return species_fitness


#  +++ ELITIST GENETIC ALGORITHM +++


def create_random_forest(tree_size):  # "Create Random Pop"
    random_species = np.empty([_FOREST_SIZE, tree_size], dtype=int)
    random_forest = []

    letters = represent_species()

    for i in range(_FOREST_SIZE):
        random_tree = []
        random_species[i] = np.random.randint(_SPE_SIZE, size=tree_size)

        for j in range(tree_size):
            random_tree.append(letters[random_species[i][j]])

        random_forest.append(random_tree)

    return random_forest


def fitness(correct_tree, random_tree):
    correct = 0

    for i in range(len(correct_tree)):
        if random_tree[i] == correct_tree[i]:
            correct += 1

    return correct


def reproduction_prob(correct_tree, random_forest):
    total_fit = sum(fitness(correct_tree, random_forest[i]) for i in range(len(random_forest)))

    reproduction_chance = np.empty([_FOREST_SIZE, 1])

    for i in range(len(random_forest)):
        reproduction_chance[i] = fitness(correct_tree, random_forest[i]) / total_fit

    return reproduction_chance


def selection(reproduction_chance):
    return np.argmax(reproduction_chance)


def cut_index():
    for i in range(_FOREST_SIZE):
        prob = random()

        if prob <= _PROB_CUT:
            return i

    return _SPE_SIZE / 2


def crossover(dad, mom):
    tree_size = len(dad)
    cut = cut_index()

    crossed_son = [dad[i] if i <= cut else mom[i] for i in range(tree_size)]
    crossed_daughter = [mom[i] if i <= cut else dad[i] for i in range(tree_size)]

    yield crossed_son
    yield crossed_daughter


def mutation(random_tree):
    mutated_random_tree = []
    tree_size = len(random_tree)
    prob = random()
    letters = represent_species()

    for i in range(tree_size):
        if prob <= _PROB_MUT:
            mutated_letter = letters[np.random.randint(_SPE_SIZE)]

            while mutated_letter == random_tree[i]:
                mutated_letter = letters[np.random.randint(_SPE_SIZE)]

        else:
            mutated_letter = random_tree[i]

        mutated_random_tree.append(mutated_letter)

    return mutated_random_tree


def best_fit(correct_tree, random_forest):
    best = 0
    index = 0

    for i in range(len(random_forest)):
        fit = fitness(correct_tree, random_forest[i])
        if fit > best:
            index = i
            best = fit

    return index, best


#  FOR TESTS ONLY
#  MC = np.array([[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 1, 0]], float)
#  MD = np.array([[900, 900, 900, 900, 900], [20, 900, 900, 900, 900], [60, 50, 900, 900, 900], [100, 90, 40, 900, 900],
#               [90, 80, 50, 30, 900]], float)

#  GLOBAL VARIABLES
_SPE_SIZE = 5  # maximum = alphabet letters = 26
_FOREST_SIZE = 2*_SPE_SIZE
_NULL_VALUE = 900
_PROB_CUT = 0.20
_PROB_MUT = 0.20
_MAX_ITER = 10000
_EVOLUTION = 10


def main():
    species = create_species()
    distance = create_distance(species)
    letters = represent_species()
    distance_path = []
    letters_path = []

    # TESTS
    print("\n++ LET'S BEGIN THE SHOW ++")
    print("\n+ SPECIES: ", letters, "\n")
    print("\n", species)
    print("\n+ CALCULATING DISTANCE")

    discover_tree(distance, letters, distance_path, letters_path)

    print("\n+ L_PATH: ", letters_path)
    print("\n+ DISTANCE_PATH: ", distance_path)

    #  draw_tree(distance_path, letters_path, _SPE_SIZE) still needs fixes. it's in the notes below

    species_fitness = create_tree_fitness(letters_path)

    print("\n+ SPECIES_FITNESS: ", species_fitness)

    #  STARTING THE G.A.

    random_forest = create_random_forest(len(species_fitness))
    reproduction_chance = reproduction_prob(species_fitness, random_forest)

    print("\n+ ORIGINAL RANDOM FOREST: ")

    for i in range(len(random_forest)):
        print(random_forest[i], ": ", reproduction_chance[i])

    #  STARTING THE REPRODUCTION

    better = 0
    count = 0

    while better < _EVOLUTION:
        new_random_forest = []
        best_fit_value = best_fit(species_fitness, random_forest)[1]

        for j in range(_SPE_SIZE):
            dad_index = selection(reproduction_chance)
            dad = random_forest[dad_index]
            reproduction_chance[dad_index] = 0

            mom_index = selection(reproduction_chance)
            mom = random_forest[mom_index]
            reproduction_chance[mom_index] = 0

            crossed_son, crossed_daughter = crossover(dad, mom)

            mutated_son = mutation(crossed_son)
            mutated_daughter = mutation(crossed_daughter)

            if j % 2 == 0:
                new_random_forest.append(mutated_son)

            else:
                new_random_forest.append(mutated_daughter)

        for j in range(_SPE_SIZE, _SPE_SIZE*2):
            best_fit_index = best_fit(species_fitness, random_forest)[0]
            new_random_forest.append(random_forest[best_fit_index])
            reproduction_chance[best_fit_index] = 0

        random_forest = []
        for j in range(_FOREST_SIZE):
            random_forest.append(new_random_forest[j])

        reproduction_chance = reproduction_prob(species_fitness, random_forest)

        if best_fit(species_fitness, random_forest)[1] > best_fit_value:
            better += 1

        count += 1

        if count > _MAX_ITER:
            break

    print("\n+ NEW RANDOM FOREST #", count + 1, ":")    # If into the 'for' with the 'for' bellow we can see every NEW RANDOM TREE

    for j in range(len(random_forest)):
        print(random_forest[j], ": ", fitness(species_fitness, random_forest[j]))

    print("\n+ THE BEST RANDOM TREE:", random_forest[np.argmax(reproduction_chance)], best_fit(species_fitness, random_forest)[1])


#  +++ MAIN +++


if __name__ == '__main__':
    main()
