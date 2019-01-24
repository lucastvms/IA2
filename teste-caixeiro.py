# -*- coding: utf-8 -*-
import random

# cidades: a, b, c, d
# arcos: 1- a,b ; 2- a,c ; 3- a,d ; 4- b,a ; 5- b,c ; 6- b,d ; 7- c,a ; 8- c,b ; 9- c,d ; 10- d,a ; 11- d,b ; 12- d,c

#1. Geração de população
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
def adaptar(m):
    matriz = [] # lista de cromossomos criados aleatoriamente

    for i in range(0,10):
        lista = [] # arcos existentes no cromossomo
        for j in range(0, 12):
            if m[i][j] == 1:
                lista.append(j)
        matriz.append(lista)

    return matriz

#200. Main
m = gerar(10, 12)
print m
print adaptar(m)
#201. Testes

#print m[0][1]
#for i in range (0, 10):    print i



