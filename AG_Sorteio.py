import numpy as np

"""
            ## DICTIONARY ##
ch = chromosome
ch_size = chromosome size
pop = population
pop_size = population size
prob_cut = probability to cut the chromosome for crossover
prob_mut = probability to cut the chromosome for mutation
prob = random prob for tests (Parent, Cut, Mutation)
total_fit = sum of the values of the fitness from all the population
parents = vector that contains the probability of every chromosome becoming a parent for new chromosomes
iter = number of populations created before ending the program

#FUNC: fitness(chromosome) 1 0 1 1 0 => 1*(5*5) + 0*(4*4) + 1*(3*3) + 1*(2*2) + 0*(1*1)
"""

#GLOBAL
ch_size = 5
pop_size = 5
prob_cut = 0.25
prob_mut = 0.10
iter = 2

#RANDOM
def random():
    return np.random.rand()

#CREATE CRHOMOSOME
def gen_chromosome(ch_size):
    ch = np.random.randint(2, size=ch_size)

    return ch

#CREATE FIRST_POP
def gen_first_pop():
    pop = np.empty([pop_size, ch_size])

    for i in range(pop_size):
        pop[i] = gen_chromosome(ch_size)

    return pop

#FITNESS
def fitness(ch):
    return sum([(i+1)*(i+1)*ch[ch_size-i-1] for i in range(ch_size)])

#DEFINE PARENT_CHANCE
def parents_prob(pop):
    total_fit = sum(fitness(pop[i]) for i in range(pop_size))

    parents = np.empty([pop_size, 1])

    for i in range(pop_size):
        parents[i] = fitness(pop[i]) / total_fit

    """ # FIRST TEST
    print("pop:", pop, "\n pop_size: ", pop_size, " total_fit: ", total_fit, "\n")
    for i in range (pop_size):        print(i, ": fitness", fitness(pop[i]), ": p_percentage", parents[i])
    """

    return parents

#SELECT THE PARENT
def selection(pop, parents):
    prob = random()

    for i in range(1, pop_size):
        parents[i] += parents[i-1]

    for i in range(1, pop_size):
        if prob>parents[i-1] and prob<parents[i]:
            return i

    return 0

#SELECT WHERE TO CUT
def cut_index():
    for i in range(pop_size):
        prob = random()
        if prob <= prob_cut:
            return i

    return pop_size/2

#CROSSOVER
def crossover(dad, mom):
    cut = cut_index()
    crossed_son = [dad[i] if i <= cut else mom[i] for i in range(ch_size)]
    crossed_daughter = [mom[i] if i <= cut else dad[i] for i in range(ch_size)]

    yield crossed_son
    yield crossed_daughter

#MUTATION
def mutation(ch):
    mutated_ch = np.empty(ch_size)
    prob = random()

    for i in range(ch_size):
        if prob <= prob_mut:
            mutated_ch[i] = 0 if ch[i] == 1 else 1
        else:
            mutated_ch[i] = ch[i]

    return mutated_ch


#MAIN

pop = gen_first_pop()
parents = parents_prob(pop)

print("FIRST POP\n", pop,"\n", parents, "\n")

for i in range(iter):
    new_pop = np.empty([pop_size, ch_size])

    for j in range(pop_size // 2):
        dad_i = selection(pop, parents)
        mom_i = selection(pop, parents)

        while(dad_i == mom_i):
            mom_i = selection(pop, parents)

        dad = pop[dad_i]
        mom = pop[mom_i]

        crossed_son, crossed_daughter = crossover(dad, mom)

        mutated_son = mutation(crossed_son)
        mutated_daughter = mutation(crossed_daughter)

        new_pop[2*j] = mutated_son
        new_pop[2*j - 1] = mutated_daughter

    pop = new_pop
    parents = parents_prob(pop)
    print("NEW POP #",i+1,"\n", pop, "\n", parents, "\n")
