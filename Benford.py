import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import random


class Benford:
    def __init__(self):
        self.distribution = None
        self.data_vector = None
        self.column = None
        self.title = None
        self.colours = ["#007f5f","#2b9348","#55a630","#80b918","#aacc00","#bfd200","#dddf00","#eeef20","#ffff3f"]

        self.expected = {}
        for d in range(1, 10):
            # Expected distribution given by the Benford's Law
            self.expected[d] = math.log10(1 + 1 / d)

    def analyze(self, dataset, column, title=None):
        df = pd.read_csv(dataset)
        self.column = column
        self.data_vector = df.loc[:, self.column].to_list()
        self.data_vector = [d for d in self.data_vector if d > 0]
        self.distribution = self.calculate(self.data_vector)
        self.title = title
        self.plotDistribuition(self.distribution)
        print(self.distribution)

    def manipulateV2(self, vect=None):
        if vect is None:
            vect = [1, 2, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 9, 8, 9, 9]
        self.data_vector = [random.choice(vect) * 1000 if random.randint(0, 10) % 2 == 0 else x for x in
                            self.data_vector if not math.isnan(x) and x > 0]
        self.title = 'Manipulated - ' + self.title

    def reanalyze(self):
        print(len(self.data_vector))
        self.distribution = self.calculate(self.data_vector)
        self.plotDistribuition(self.distribution)
        print(self.distribution)

    def calculateCorrelation(self):
        # Variables are the expected and the actual distribution frequencies
        N = len(self.data_vector)
        X = [N * self.expected[d] for d in range(1, 10)]
        Y = [N * self.distribution[d] for d in range(1, 10)]
        corr = np.corrcoef(X, Y)[0, 1]
        return corr

    def calculate(self, data):
        distribution = {}
        for k in range(1, 10):
            distribution[k] = self.countDigit(data, k) / len(data)
        return distribution

    def countDigit(self, data, digit):
        return len([x for x in data if not math.isnan(x) and x > 0 and int(str(x)[0]) is digit])

    def plotDistribuition(self, distribution):
        # Plotta distribuzione con histogramma e linea della legge
        values = distribution.values()
        plt.title(self.title)
        plt.xlabel('First digit')
        plt.ylabel('Frequency')
        plt.ylim([0, 0.35])
        vals = list(values).copy()
        vals.sort(key=float)
        cols = [self.colours[list(reversed(vals)).index(v)] for v in values]
        plot_bars = plt.bar(range(1, 10), values, tick_label=range(1, 10), color=cols)
        for bar in plot_bars:
            height = bar.get_height()
            plt.annotate(f'{height:9.3f}',
                         xy=(bar.get_x() - 0.15 + bar.get_width() / 2, height), fontsize=7,
                         xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')
        plt.show()

