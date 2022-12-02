# TSP_genetic_algorithm
The genetic algorithm is a heuristic based search algorithm
on the mechanisms of natural selection and natural genetics. The basic concept
 inspired the emergence of the genetic algorithm is the theory of natural evolution
proposed by Charles Darwin. In this theory it is explained that on
natural evolutionary process, each individual must adapt to
the surrounding environment in order to survive (Kurnia et al., n.d.).

Genetic algorithms may not always achieve the best results, however
often solves the problem quite well. Genetic Algorithm
represents a solution to a problem as a chromosome. There is
Some important aspects in genetic algorithms include function definition
fitness, definition and implementation of genetic representation, definition and
implementation of genetic operations (Suprayogi & Mahmudy, n.d.).
D.E. Golberg in his book uses the Genetic Algorithm method
in solving optimization problems in the industry. GA method then
developed its use in various fields of science, one of them
applied in optimization of distribution network design (Budiastra et al., 2006).
The genetic algorithm in this case is almost similar to the Traveling case
Salesman Problem (TSP).

# Methode
## 1. Location
The floor plan or location representation is taken from Google Map imaging
for Wonotoro village. Sendang Siraman is on the right side of Hamlet
Wonotoro. Below is a picture of a house plan
marked with red nodes and water springs marked with
the cross marks as the potential for EBT Microhydro, while the red line is
a line that limits the area of the Wonotoro village itself

<img width="350" height="350" src="https://github.com/anamsigit/TSP_genetic_algorithm/blob/main/images/wonotoromap1.png">
<img width="750" height="350" src="https://github.com/anamsigit/TSP_genetic_algorithm/blob/main/images/wonotoromap2.png">
<img width="350" height="350" src="https://github.com/anamsigit/TSP_genetic_algorithm/blob/main/images/wonotoromap3.png">

## 2. Coordinate Determination
From data, the number of active houses is 86.
so there are 86 nodes that need to be connected. formed nodes
then transformed into Cartesian coordinates with
Geogebra which can be accessed online at https://www.geogebra.org/m/JMMKv7cx

![](images/to_matplotlib.png) 

So when plotted, you will get the image model below, with
node J as the location of Sendang Siraman (Water Spring).

## 3. Calculation of the distance of each node
Calculation of fitness is needed for the needs of the Algorithm
Genetics to find the best solution. Calculation of the distance between nodes
doing with the Euclide Distance Formula and the results are stored
into a matrix. Euclidean Distance Geometry is the study of
Euclidean geometry based on the concept of distance. Euclidian distance is useful
in some applications where the input data consists of a collection of distances, and
the output is the set of points in Euclidean space that gives
actual distance values (Liberti et al., 2014).

<img width="350" height="350" src="https://github.com/anamsigit/TSP_genetic_algorithm/blob/main/images/wonotoromap4.png">

extract coordinates told by geogbra and transfer to numpy array for plotting using matplotlib

<img width="400" height="200" src="https://github.com/anamsigit/TSP_genetic_algorithm/blob/main/images/euclidiandistance.png">

## 4. Genetics Algorithm Processing
The Genetic Algorithm used is similar to the Traveling case
Salesman Trouble (TSP) namely the process of crossover and mutation
there cannot be the same value or node/city on 1 chromosome.

### a. initiation
The number of genes or the number of nodes is 86 (n), the number of chromosomes
is 100 (m) and the number of Generations is 1000 (N) which means that
1 population contains 100 chromosomes (individuals). After each run
1000 generations, last generation will be saved as .CSV file, so
allows continuous training given the available resources
limited use.

### b. population generation
Generation of the initial population by generating chromosomes
filled by random permutations.

### c. fitness
Each population that is formed will calculate the fitness value for
each chromosome in the population. The fitness calculation is by
sums up all the Euclide Distance values of the nodes
prepared as a solution.

### d. crossover
Crossover occurs whenever two individuals are combined for
create new individuals and eventually they are copied into the population
new. The two selected populations are based on the random function and
this population works as the parent. Thus parents
create their children who are better than the parents themselves in
distance form and finally processing this population in next step (Sarkar, n.d.).
In this case the child is the offspring of 2 parents. child
is the result of combining the result of cross + parent 1 (when there is a
double the gene value, then it is removed then what is added
which is not in parent 2), here is an illustration


<img width="1000" height="250" src="https://github.com/anamsigit/TSP_genetic_algorithm/blob/main/images/crossover.png">

Genes and chromosomes were selected randomly. chromosomes are chosen at random
as many as 2 chromosomes, while 3 genes are selected to be
crossed from 2 selected chromosomes (parent 1 & parent 2).
done for each chromosome so that it will produce 1
new population (100 chromosomes or individuals). crossover
algorithm is needed so that the solution given is not stuck in the local
just the bare minimum.

### e. mutation
Mutations are part of the GA associated with
search space exploration. It has been observed that mutations are very
important for GA convergence while crossover is not. But roles
mutations are often underestimated in the field of Evolutionary Computing (de Falco et al.,
2002). The following is an illustration of the mutation application for this case

<img width="1000" height="100" src="https://github.com/anamsigit/TSP_genetic_algorithm/blob/main/images/mutation.png">

Mutations are carried out by replacing a gene with another gene in 1
chromosome type

### f. Population Aggregation

There were 3 populations, namely populations from random results (100
chromosomes), the population of the crossover results (100 chromosomes), and the population
from the mutation (100 chromosomes). When the populations are combined
so that the sum is 300 chromosomes (100 + 100 + 100). From 300
the best 100 chromosomes will be taken with
paying attention to the smallest fitness value with the sort method, as well
remove chromosomes that have the same solution as
another chromosome.

### g. running and plotting
Running this Algorithm for 36000+ generations for
get the optimal solution, the program is run requires
takes 1-2 days so it needs to be cut into pieces by storing
solution in the last generation into a .CSV file, so when you want
continue on to the next generation is to use
reference to the CSV file that has been saved.

for paper read at https://github.com/anamsigit/TSP_genetic_algorithm/blob/main/The_paper.pdf


