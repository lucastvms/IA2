import random
from operator import itemgetter

# http://www.dainf.ct.utfpr.edu.br/~tacla/IA/016a-AlgGeneticos.pdf
# https://pythonhelp.wordpress.com/2012/06/15/por-que-__name__-__main__/


# Geração
def gerar(n_linhas, n_colunas):
    pop = []
    cromossomo = []

    # Gera cromossomos aleatórios e binários
    while n_linhas != len(pop):
        n = random.randint(0, 1)
        cromossomo.append(n)

        if len(cromossomo) == n_colunas:
            pop.append(cromossomo)
            cromossomo = []

    # for i in range(0, len(pop)):
    #     print("\n", pop[i])

    return pop


# Adaptação
def adaptar(pop, pesos, origem, destino, cidades):
    fitness = []

    for i in range(0, 10):
        peso = 0
        lista_origem = []
        lista_destino = []

        # Cria caminho
        for j in range(0, 12):
            if pop[i][j] == 1:
                peso += pesos[j]
                lista_origem.append(origem[j])
                lista_destino.append(destino[j])

        # Verifica se há penalidade máxima >>> FALTA CONTADOR PARA VER SE PASSOU EM TODAS AS CIDADES
        for j in range(0, len(lista_destino)):
            if lista_destino.count(lista_origem[j]) > 0: lista_destino.remove(lista_origem[j])

        if lista_destino:
            peso = 10000

        print(lista_origem)
        print(lista_destino)

        fitness.append(peso)

    # Ordenação

    print(fitness, "\n")
    print('POP: \n', pop)
    fitness = list(fitness)
    fitness, pop[:] = zip(*sorted(zip(fitness, pop[:])))

    print(fitness, '\n')
    print('POP: \n', pop)


    return fitness


# Variáveis do problema

cidades = ['a', 'b', 'c', 'd']
origem = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd']
destino = ['b', 'c', 'd', 'a', 'c', 'd', 'a', 'b', 'd', 'a', 'b', 'c']
pesos = [1, 5, 4, 1, 2, 6, 5, 2, 3, 4, 6, 3]

# Chamada das funções

pop = gerar(10, 12)
adaptar(pop, pesos, origem, destino, cidades)


