from random import randint, choices


class Gene:
    def __init__(self):
        self.__condition = randint(0, 1)

    """
    Mutation of gene
    """

    def mutate(self):
        if randint(0, 1):  # 50% chance to mutate
            self.__condition = (self.__condition + 1) % 2  # 1 -> 0; 0 -> 1

    """
    Standard getter
    """

    def get_condition(self):
        return self.__condition


class Chromosome:
    def __init__(self, genome_list):
        if len(genome_list) != 10:
            raise ValueError("Genome is corrupted")
        self.__genome = genome_list

    """
    Randomly mutation
    """

    def mutate(self):
        for gene in choices(self.__genome):  # random amount of random numbers
            gene.mutate()

    def get_genome(self):
        return self.__genome


class Dna:
    def __init__(self, chromosome_list):
        if len(chromosome_list) != 10:
            raise ValueError("Chromosomes are corrupted")
        self.__chromosomes = chromosome_list

    """
        Randomly mutation
    """

    def mutate(self):
        for chromosome in choices(self.__chromosomes):  # random amount of random numbers
            chromosome.mutate()

    """
    Standard getter
    """

    def get_chromosomes(self):
        return self.__chromosomes


class Organism:
    def __init__(self, name, dna):
        self.__name = name
        self.__dna = dna
        self.__environment_to_mutate = None

    """
    Standard getters
    """

    def get_name(self):
        return self.__name

    def get_dna(self):
        return self.__dna

    """
    Standard setters
    """

    def set_dna(self, dna):
        self.__dna = dna

    def set_environment(self, current_environment):
        self.__environment_to_mutate = current_environment

    def print_table_of_genes(self):
        spaces_num = [0, 1, 2, 3, 5, 5, 3, 2, 1, 0]  # style
        dash_num = [10, 8, 6, 4, 0, 0, 4, 6, 8, 10]  # style
        print('-' * 40, sep='')  # style
        print(f"This is DNA of {type(self).__name__.lower()} \"{self.__name}\":")  # style
        print(' ' * 20, '\t', chr(9679), '-' * 10, chr(9711), sep='')  # style
        for i, c in enumerate(self.__dna.get_chromosomes()):
            print(*(gene.get_condition() for gene in c.get_genome()),
                  f"\t{' ' * spaces_num[i]}"  # style 
                  f"{chr(9679) if sum(map(Gene.get_condition, c.get_genome())) <= 6 else chr(9711)}"  # style 
                  f"{'-' * dash_num[i]}"  # style 
                  f"{chr(9711) if sum(map(Gene.get_condition, c.get_genome())) <= 6 else chr(9679)}")  # style
        print(' ' * 20, '\t', chr(9711), '-' * 10, chr(9679), sep='')  # style
        print('-' * 40, sep='a')  # style

    """
    Find sum of conditions of all genes, of all chromosomes in DNA 
    """
    def get_sum_of_genes(self):
        return sum(sum(map(Gene.get_condition, chromosome.get_genome()))
                   for chromosome in self.get_dna().get_chromosomes())


class Gremlin(Organism):
    def __init__(self, name, dna):
        super().__init__(name, dna)
        self.__environment_to_mutate = "water"

    def get_environment(self):
        return self.__environment_to_mutate


def organism_to_mutate(organism, transitions_grade, environment):
    if organism.get_environment() == environment:
        generations = 0
        organism.print_table_of_genes()
        while organism.get_sum_of_genes() < transitions_grade:
            organism.get_dna().mutate()
            generations += 1
        print(f"After {generations} generations of cells, {type(organism).__name__.lower()} \"{organism.get_name()}\""
              f" mutated in a {environment} to transition's grade: "
              f" {organism.get_sum_of_genes()}-'1' and {100 - organism.get_sum_of_genes()}-'0'")
        organism.print_table_of_genes()


#  -----------------------------------------------------------------------------------------------
stripe = Gremlin('Stripe', Dna([Chromosome([Gene() for _ in range(10)]) for _ in range(10)]))
mohawk = Gremlin('Mohawk', Dna([Chromosome([Gene() for _ in range(10)]) for _ in range(10)]))
mugger = Gremlin('Mugger', Dna([Chromosome([Gene() for _ in range(10)]) for _ in range(10)]))

organism_to_mutate(stripe, 72, "water")
print("****************************************************************************************************")
organism_to_mutate(mohawk, 71, "water")
print("****************************************************************************************************")
organism_to_mutate(mugger, 70, "water")
