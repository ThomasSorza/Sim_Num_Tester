from numpy import mean, var

import scipy.stats as st
import matplotlib.pyplot as plt

class VarianceTest:
    def __init__(self, ri_numbers):
        self.ri_numbers = ri_numbers
        self.variance = 0.0
        self.alpha = 0.05
        self.average = 0.0
        self.acceptation = 0.95
        self.passed = False
        self.n = len(ri_numbers)
        self.superior_limit = 0.0
        self.inferior_limit = 0.0
        self.chi_square1 = 0.0
        self.chi_square2 = 0.0

    def calculateVariance(self):
        self.variance = var(self.ri_numbers)

    def calculateAverage(self):
        self.average = mean(self.ri_numbers)

    def calculateChiSquare1(self):
        self.chi_square1 = st.chi2.ppf(self.alpha/2,self.n-1)

    def calculateChiSquare2(self):
        self.chi_square2 = st.chi2.ppf(1-self.alpha/2, self.n-1)

    def calculateInferiorLimit(self):
        self.inferior_limit = self.chi_square1/(12*(self.n-1))

    def calculateSuperiorLimit(self):
        self.superior_limit = self.chi_square2/(12*(self.n-1))

    def checkTest(self):
        self.calculateAverage()
        self.calculateVariance()
        self.calculateChiSquare1()
        self.calculateChiSquare2()
        self.calculateSuperiorLimit()
        self.calculateInferiorLimit()
        if self.inferior_limit <= self.variance <= self.superior_limit:
            self.passed = True
        else:
            self.passed = False

    def plotLimitsAndVariance(self):
        x = ["Inferior Limit", "Variance", "Superior Limit"]
        y = [self.inferior_limit, self.variance, self.superior_limit]

        fig, ax = plt.subplots()

        bars = ax.bar(x, y, color=['red', 'blue', 'green'])
        plt.title('Inferior Limit, Variance, and Superior Limit')
        plt.xlabel('Medidas')
        plt.ylabel('Value')

        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.4f}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 1),
                        textcoords="offset points", ha='center', va='bottom')

        plt.show()

    def clear(self):
        self.variance = 0.0
        self.alpha = 0.05
        self.average = 0.0
        self.acceptation = 0.95
        self.passed = False
        self.superior_limit = 0.0
        self.inferior_limit = 0.0
        self.chi_square1 = 0.0
        self.chi_square2 = 0.0
    
def main():
        poker = VarianceTest([
    0.79817, 0.68468, 0.58381,
    0.11612, 0.32584, 0.15024,
    0.28316, 0.61384, 0.44471,
    0.90924, 0.39663, 0.12679,
    0.19981, 0.08535, 0.05599])
        poker.checkTest()
        print(poker.variance)
        print(poker.average)
        print(poker.chi_square1)
        print(poker.chi_square2)
        print(poker.superior_limit)
        print(poker.inferior_limit)
        print(poker.passed)
        poker.plotLimitsAndVariance()
        

if __name__ == "__main__":
        main() 
    