"""
1 Filogenia baseada em distância
A construção de uma árvore filogenética baseada em distância tem como entrada uma
matriz de distância, que são utilizadas para inferir árvores ultramétricas e árvores aditivas. O
Algoritmo Waterman é usado para construir árvores filogenéticas aditivas, enquanto que o
Algoritmo de Farach, Kannan e Warnow é utilizado para construir árvores ultramétricas
[GUSFIELD, 1997]; este estabelece que as distâncias medidas na árvore devem se encontrar em
um intervalo entre uma matriz de limite inferior (Ml) e outra de limite superior (Mh). De modo
que Mijl ≤ dij ≤ Mijh , onde dij é a distância média entre dois objetos i e j na árvore. Tal
propriedade torna o problema mais realista, visto que matrizes ultramétricas são raras

Lema 1: Uma matriz de estados M é aditiva se, e somente se, dados quaisquer quatro
objetos i, j, k e l de M, vale uma das seguintes propriedades:
(i) dik + djl = dil + djk (ii) dil + dkj = dij + dkl (iii) dik + djl = dij + dkl


"""
# Import modules
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO

# Read the sequences and align
aln = AlignIO.read('msa.phy', 'phylip')

# Print the alignment
print(aln)

# Calculate the distance matrix
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(aln)

# Print the distance Matrix
print('\nDistance Matrix\n===================')
print(dm)

# Construct the phylogenetic tree using UPGMA algorithm
constructor = DistanceTreeConstructor()
tree = constructor.upgma(dm)

# Draw the phylogenetic tree
Phylo.draw(tree)

# Print the phylogenetic tree in the terminal
print('\nPhylogenetic Tree\n===================')
Phylo.draw_ascii(tree)
