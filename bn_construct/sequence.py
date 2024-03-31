import random
import numpy as np
import pandas as pd
from pgmpy.estimators import K2Score
from pgmpy.models import BayesianModel


class GeneticAlgorithm:
    def __init__(self, data, scoring_method, max_iter=300):
        self.data = data
        self.scoring_method = scoring_method
        self.max_iter = max_iter
        self.population_size = 100  # 可以根据需要调整
        self.tournament_size = 5  # 锦标赛选择的大小
        self.mutation_rate = 0.1  # 变异概率
        self.population = self.initialize_population()

    def initialize_population(self):
        # 初始化种群
        population = []
        for _ in range(self.population_size):
            individual = list(self.data.columns)
            np.random.shuffle(individual)
            population.append(individual)
        return population

    def fitness(self, individual):
        # 定义适应度函数，即使用K2Score评分
        model = BayesianModel([(individual[i], individual[i + 1]) for i in range(len(individual) - 1)])
        score = self.scoring_method(model)
        return score

    def select(self, population):
        # 选择函数，这里使用锦标赛选择
        selected = []
        for _ in range(self.tournament_size):
            selected.append(population[np.random.randint(len(population))])
        selected.sort(key=self.fitness, reverse=True)
        return selected[0]

    def pmx(parent1, parent2):
        length = len(parent1)
        # 随机选择交叉点
        crossover_point1, crossover_point2 = sorted(random.sample(range(length), 2))
        # 初始化子代为None
        child1, child2 = [None]*length, [None]*length
        
        # 部分复制父代段到子代
        child1[crossover_point1:crossover_point2+1] = parent1[crossover_point1:crossover_point2+1]
        child2[crossover_point1:crossover_point2+1] = parent2[crossover_point1:crossover_point2+1]
        
        # 为子代填充剩余部分
        for i in range(length):
            if not child1[i]:
                if parent2[i] not in child1:
                    child1[i] = parent2[i]
                else:
                    # 查找映射
                    mapping = parent2[i]
                    while mapping in parent1[crossover_point1:crossover_point2+1]:
                        mapping_index = parent1.index(mapping)
                        mapping = parent2[mapping_index]
                    child1[i] = mapping
            
            if not child2[i]:
                if parent1[i] not in child2:
                    child2[i] = parent1[i]
                else:
                    # 查找映射
                    mapping = parent1[i]
                    while mapping in parent2[crossover_point1:crossover_point2+1]:
                        mapping_index = parent2.index(mapping)
                        mapping = parent1[mapping_index]
                    child2[i] = mapping
                    
        return child1, child2

    def cycle_crossover(parent1, parent2):
        length = len(parent1)
        child1, child2 = [None] * length, [None] * length
        cycle_num = 0
        while None in child1:  # 检查子代1中是否还有未填充的位置
            if cycle_num % 2 == 0:  # 如果是偶数循环，从parent1到child1
                start_index = child1.index(None)
                index = start_index
                while True:
                    child1[index] = parent1[index]
                    index = parent2.index(parent1[index])
                    if index == start_index:
                        break
            else:  # 如果是奇数循环，从parent2到child1
                start_index = child1.index(None)
                index = start_index
                while True:
                    child1[index] = parent2[index]
                    index = parent1.index(parent2[index])
                    if index == start_index:
                        break
            cycle_num += 1
        
        # 填充child2的空缺
        for i in range(length):
            if child1[i] == parent1[i]:
                child2[i] = parent2[i]
            else:
                child2[i] = parent1[i]
                
        return child1, child2

    def order_crossover(parent1, parent2):
        length = len(parent1)
        # 随机选择两个交叉点
        crossover_point1, crossover_point2 = sorted(random.sample(range(length), 2))

        # 创建子代个体的框架
        child1, child2 = [None] * length, [None] * length

        # 将父代个体中位于交叉点间的部分直接复制到子代个体中
        child1[crossover_point1:crossover_point2] = parent1[crossover_point1:crossover_point2]
        child2[crossover_point1:crossover_point2] = parent2[crossover_point1:crossover_point2]

        # 填充剩余部分，保持父代个体中的顺序
        def fill_remaining(parent, child):
            current_pos = crossover_point2
            for gene in parent:
                if gene not in child:
                    if current_pos >= length:
                        current_pos = 0
                    child[current_pos] = gene
                    current_pos += 1

        # 填充两个子代个体的剩余部分
        fill_remaining(parent2, child1)
        fill_remaining(parent1, child2)

        return child1, child2

    def mutate(self, individual):
        # 变异函数
        for i in range(len(individual)):
            if np.random.rand() < self.mutation_rate:
                swap_idx = np.random.randint(len(individual))
                individual[i], individual[swap_idx] = individual[swap_idx], individual[i]
        return individual

    def run(self):
        # 执行遗传算法
        for generation in range(self.max_iter):
            new_population = []
            for _ in range(self.population_size):
                parent1 = self.select(self.population)
                parent2 = self.select(self.population)
                offspring = self.pmx(parent1, parent2)
                offspring = self.mutate(offspring)
                new_population.append(offspring)
            self.population = new_population
        # 这里仅返回种群中评分最高的个体作为结果
        best_individual = max(self.population, key=self.fitness)
        return best_individual













