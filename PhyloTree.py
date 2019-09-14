import numpy as np


def random():
    return np.random.rand()


def create_species(spe_size):
    species = np.array(np.empty([spe_size, spe_size], dtype=float), subok=True)

    for i in range(spe_size):
        species[i] = np.random.randint(2, size=(spe_size))

    return species


def represent_species(spe_size):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    letters_species = []

    for i in range(spe_size):
        letters_species.append(letters[i])

    return letters_species


def create_distance(species, spe_size):
    distance = np.array(np.zeros([spe_size, spe_size], dtype=float), subok=True)

    start = -1
    for i in range(spe_size):
        start += 1
        for j in range(start, spe_size):
            distance[i][j] = _NULL_VALUE

    for i in range(spe_size):
        for j in range(spe_size):
            for k in range(spe_size):
                if i > j:
                    if species[i][k] != species[j][k]:
                        distance[i][j] += 1

    return distance


def discover_similar(distance, spe_size):
    min_distance = np.amin(distance)
    min_ind = np.where(distance == min_distance)
    min_row, min_col = min_ind[0][0], min_ind[1][0]
    min_value = distance[min_ind[0][0]][min_ind[1][0]]

    for i in range(spe_size):
        for j in range(spe_size):
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


def discover_tree(distance, spe_size, distance_path, letters_path):
    size = spe_size
    similar = distance

    for size in range(spe_size, 1, -1):
        print("STEP #", spe_size - size, "\n", similar)
        similar, min_row, min_col, min_value = discover_similar(similar, size)
        distance_path.append(min_value)

    return similar


#  FOR TESTS ONLY
#  MC = np.array([[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 1, 0]], float)
#  MD = np.array([[900, 900, 900, 900, 900], [20, 900, 900, 900, 900], [60, 50, 900, 900, 900], [100, 90, 40, 900, 900],
#               [90, 80, 50, 30, 900]], float)

#  GLOBAL VARIABLES
_SPE_SIZE = 5  # maximum = alphabet letters = 26
_NULL_VALUE = 900


def main():
    distance_path = []
    letters_path = []
    species = create_species(_SPE_SIZE)
    distance = create_distance(species, _SPE_SIZE)
    letters = represent_species(_SPE_SIZE)

    # TESTS
    print("\n++ LET'S BEGIN THE SHOW ++")
    print("\n+ SPECIES: ", letters, "\n")
    print("\n", species)
    print("\n+ CALCULATING DISTANCE")

    discover_tree(distance, _SPE_SIZE, distance_path, letters_path)

    print("\n+ DISTANCE_PATH: ", distance_path)


if __name__ == '__main__':
    main()
