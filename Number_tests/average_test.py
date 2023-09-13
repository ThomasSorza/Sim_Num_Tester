from statistics import mean
from math import sqrt
from typing import Any
from scipy.stats import norm
import matplotlib.pyplot as plt

class AverageTest:
    def __init__(self, ri_nums):
        self.ri_nums = ri_nums
        self._average = None
        self.alpha = 0.05
        self.acceptation = 0.95
        self.passed = False
        self.n = len(ri_nums)
        self.z = 0.0
        self.superior_limit = 0.0
        self.inferior_limit = 0.0

    @property
    def average(self):
        if self._average is None:
            self._average = mean(self.ri_nums)
        return self._average

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = value

    @property
    def acceptation(self):
        return self._acceptation

    @acceptation.setter
    def acceptation(self, value):
        self._acceptation = value

    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        self._n = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    @property
    def superior_limit(self):
        return self._superior_limit

    @superior_limit.setter
    def superior_limit(self, value):
        self._superior_limit = value

    @property
    def inferior_limit(self):
        return self._inferior_limit

    @inferior_limit.setter
    def inferior_limit(self, value):
        self._inferior_limit = value

    def calculateZ(self): # Z value must be between inferior and superior limit to pass the test
        self.z = norm.ppf(1 - (self._alpha / 2))

    def calculateSuperiorLimit(self):
        if self.n > 0:
            self.superior_limit = (1/2) + (self.z * (1 / sqrt(12 * self.n)))

    def calculateInferiorLimit(self):
        if self.n > 0:
            self.inferior_limit = (1/2) - (self.z * (1 / sqrt(12 * self.n)))
    
    def checkIfPassed(self): #check if the test is passed
        if self.inferior_limit <= self.average <= self.superior_limit:
            self.passed = True
        else:
            self.passed = False
        return self.passed
    
    def clear(self):
        self._average = None
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
    0.94675, 0.14613, 0.03714, 0.02564, 0.59248, 0.97007, 0.88408, 0.98356, 0.88531, 0.20903,
    0.3646, 0.81139, 0.8297, 0.92341, 0.04724, 0.08755, 0.38528, 0.88296, 0.81756, 0.76944,
    0.45764, 0.17826, 0.03607, 0.92684, 0.82088, 0.60626, 0.34297, 0.48714, 0.60858, 0.09187,
    0.64766, 0.09686, 0.60099, 0.94386, 0.63456, 0.06797, 0.78311, 0.18581, 0.06715, 0.64841,
    0.55189, 0.55124, 0.27866, 0.53248, 0.51003, 0.98711, 0.50026, 0.6103, 0, 0.67105, 0.09698
    ]
    test = AverageTest(ri_nums)
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
