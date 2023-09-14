from statistics import mean
from math import sqrt
from typing import Any
from scipy.stats import norm
import matplotlib.pyplot as plt

class AverageTest:
    def __init__(self, ri_nums):
        self.ri_nums = ri_nums
        self.average = 0
        self.alpha = 0.05
        self.acceptation = 0.95
        self.passed = False
        self.n = len(ri_nums)
        self.z = 0.0
        self.superior_limit = 0.0
        self.inferior_limit = 0.0

    def calcAverage(self):
        if self.n != 0:
            self.average = mean(self.ri_nums)

    def calculateZ(self): # Z value must be between inferior and superior limit to pass the test
        self.z = norm.ppf(1 - (self.alpha / 2))

    def calculateSuperiorLimit(self):
        if self.n > 0:
            self.superior_limit = (1/2) + (self.z * (1 / sqrt(12 * self.n)))

    def calculateInferiorLimit(self):
        if self.n > 0:
            self.inferior_limit = (1/2) - (self.z * (1 / sqrt(12 * self.n)))
    
    def checkTest(self):
        self.calcAverage()
        self.calculateZ()
        self.calculateSuperiorLimit()
        self.calculateInferiorLimit()
        if self.inferior_limit <= self.average <= self.superior_limit:
            self.passed = True
        else:
            self.passed = False
    
    def checkIfPassed(self): #check if the test is passed
        if self.inferior_limit <= self.average <= self.superior_limit:
            self.passed = True
        else:
            self.passed = False
        return self.passed
    
    def clear(self):
        self.average = 0
        self.alpha = 0.05
        self.acceptation = 0.95
        self.passed = False
        self.z = 0.0
        self.superior_limit = 0.0
        self.inferior_limit = 0.0

    def plotLimitsAndAverage(self):
        x = ["Inferior Limit", "Average", "Superior Limit"]
        y = [self.inferior_limit, self.average, self.superior_limit]

        fig, ax = plt.subplots()
        bars = plt.bar(x, y, color=['red', 'blue', 'green'])
        plt.title('Inferior Limit, Variance and Superior Limit comparison')
        plt.xlabel('Category')
        plt.ylabel('Value')

        # Agregar etiquetas de valor en las barras
        for bar, value in zip(bars, y):
            ax.annotate(str(value), xy=(bar.get_x() + bar.get_width() / 2, value), xytext=(0, 1),
                        textcoords='offset points', ha='center', va='bottom')
        plt.show()

def main():
    ri_nums = [
    0.79817, 0.68468, 0.58381,
    0.11612, 0.32584, 0.15024,
    0.28316, 0.61384, 0.44471,
    0.90924, 0.39663, 0.12679,
    0.19981, 0.08535, 0.05599
    ]
    test = AverageTest(ri_nums)
    test.calcAverage()
    test.calculateZ()
    test.calculateSuperiorLimit()
    test.calculateInferiorLimit()
    test.checkIfPassed()
    print("Z:", test.z)
    print("Inferior Limit:", test.inferior_limit)
    print("Superior Limit:", test.superior_limit)
    print("Passed:", test.passed)
    print("Average:", test.average)
    print("N:", test.n)
    print("Alpha:", test.alpha)
    print("Acceptation:", 1 - test.alpha / 2)
    test.plotLimitsAndAverage()

if __name__ == "__main__":
    main()
