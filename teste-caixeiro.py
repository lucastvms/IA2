# -*- coding: utf-8 -*-
import random

# http://www.dainf.ct.utfpr.edu.br/~tacla/IA/016a-AlgGeneticos.pdf
# https://pythonhelp.wordpress.com/2012/06/15/por-que-__name__-__main__/

#1. Geração de população
#Matriz com os cromossomos sendo representados por listas, gerados de forma aleatória
def gerar(n_linhas, n_colunas):
    matriz = [] # Matriz
    linha = [] # Linha

    while n_linhas != len(matriz): # Quando o número de elementos da matriz(linhas) forem diferentes da quantidade máxima definida pelo usuário, ele ficará rodando.
        n = random.randint(0, 1) # Utilizei random para adicionar os valores
        linha.append(n) # Adiciono n à linha

        if len(linha) == n_colunas: # Se a quantidade de elementos for igual à quantidade de colunas definida pelo usuário :
            matriz.append(linha) # Adiciono a linha à matriz
            linha = [] # E zero a "linha" para adicionar outra à matriz

    return matriz # Retorno a mesma


#2. Adaptação
# avaliar o peso dos cromossomos, para saber o ranking deles
def adaptar(pop, pesos ,origem, destino):
    fitness = [] # lista do fitness/ranking dos cromossomos

    for i in range(0,10):
        peso = 0 # peso do cromossomo
        lista_caminho = [] # guarda as origens e os destinos

        for j in range(0, 12):
            if pop[i][j] == 1:
                peso += pesos[j]
                lista_caminho.append(origem[j])
                lista_caminho.append(destino[j])
                if(lista_caminho.count(origem[j]) > 2 or lista_caminho.count(origem[j]) > 2):
                    peso = 10000;
                    break;

        fitness.append(peso)

    return fitness







#200. Main

# cidades: a, b, c, d
# arcos: 1- a,b ; 2- a,c ; 3- a,d ; 4- b,a ; 5- b,c ; 6- b,d ; 7- c,a ; 8- c,b ; 9- c,d ; 10- d,a ; 11- d,b ; 12- d,c

pesos = [1, 5, 4, 1, 2, 6, 5, 2, 3, 4, 5, 3]
origem = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd']
destino = ['b', 'c', 'd', 'a', 'c', 'd', 'a', 'b', 'd', 'a', 'b', 'c']
pop = gerar(10, 12)
print (pop)
print (adaptar(pop, pesos, origem, destino))
#201. Testes

#print m[0][1]
#for i in range (0, 10):    print i


