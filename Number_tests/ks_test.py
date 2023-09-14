from statistics import mean
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

class KsTest:
    def __init__(self, ri_nums =[], n_intervals = 10):
        self.ri = ri_nums
        self.n = len(ri_nums)
        self.average = 0
        self.d_max = 0
        self.d_max_p = 0
        self.min = 0
        self.max = 0
        self.oi = []
        self.oia = []
        self.prob_oi = []
        self.oia_a = []
        self.prob_esp = []
        self.diff = []
        self.passed = False
        self.alpha = 0.05
        self.intervals = []
        self.n_intervals = n_intervals
    
    def calculate_oia(self):
        cum_freq = 0

        for freq in self.oi:
            cum_freq += freq
            self.oia.append(cum_freq)
            
    def calculate_min(self):
        if self.n != 0:
            self.min = min(self.ri)

    def calculate_max(self):
        if self.n != 0:
            self.max = max(self.ri)
    
    def calculateAverage(self):
        if self.n != 0:
            self.average = mean(self.ri)
    
    def checkTest(self):
        self.calculate_min()
        self.calculate_max()
        self.calculateAverage()
        self.calculate_intervals()
        self.calculate_oi()
        self.calculate_oia()
        self.calculate_prob_oi()
        self.calculate_oia_a()
        self.calculate_prob_esp()
        self.calculate_diff()
        self.d_max = max(self.diff)
        self.calculate_KS()
        if self.d_max <= self.d_max_p:
            self.passed = True
        else:
            self.passed = False
    
    def calculate_KS(self):
        alpha = self.alpha
        n = self.n
        if self.n <= 50 and self.n > 0:
            # Calcular el valor crítico usando la función scipy.stats.ksone.ppf()
            critical_value = stats.ksone.ppf(1 - alpha / 2, n) 
            # OJO: Usamos 1 - alpha / 2 para una prueba bilateral
        if self.n > 50:
            # Calcular el valor crítico usando la función scipy.stats.kstwobign.isf()
            critical_value = stats.kstwobign.isf(alpha) / np.sqrt(n)
        self.d_max_p = critical_value
                
    def calculate_prob_esp(self):
        for i in range(len(self.oia_a)):
            self.prob_esp.append(self.oia_a[i] / self.n)
            
    def calculate_diff(self):
        for i in range(len(self.prob_esp)):
            self.diff.append(abs(self.prob_esp[i] - self.prob_oi[i]))
        
    def calculate_oia_a(self):
        n1 = self.n/self.n_intervals
        for i in range(self.n_intervals):
            self.oia_a.append(n1*(i+1))
        
    def calculate_prob_oi(self):
        for i in range(len(self.oia)):
            self.prob_oi.append(self.oia[i] / self.n)
    
    def calculate_oi(self):
        self.ri.sort()
        self.oi = [0] * self.n_intervals  
        # Iterar a través de los valores de ri y contar en qué intervalo caen
        for valor in self.ri:
            for i, intervalo in enumerate(self.intervals):
                if intervalo[0] <= valor < intervalo[1]:
                    self.oi[i] += 1
                    break  # No es necesario seguir buscando en otros intervalos

        return self.oi
        
    
    def calculate_intervals(self):
        n_intervals = self.n_intervals
        interval_size = (self.max - self.min) / n_intervals
        initial = self.min
        for _ in range(n_intervals):
            new_interval = (initial, initial + interval_size)
            self.intervals.append(new_interval)
            initial = new_interval[1]
            
    def plotDs(self):
        x = ["D max (calculated)", "Dmax p (KS -> Table)"]
        y = [self.d_max, self.d_max_p]

        fig, ax = plt.subplots()
        bars = plt.bar(x, y, color=['red', 'blue'])
        plt.title('D max and Dmax p comparison')
        plt.ylabel('Values')

        # Agregar etiquetas de valor en las barras
        for bar, value in zip(bars, y):
            ax.annotate(str(value), xy=(bar.get_x() + bar.get_width() / 2, value), xytext=(0, 1),
                        textcoords='offset points', ha='center', va='bottom')
        plt.show()

    def plotIntervals(self):
        #TODO:plot all intervals
        pass
            
def main():
    ks_test = KsTest([
    0.991508, 0.790864, 0.603322, 0.913592, 0.63023,
    0.976403, 0.522136, 0.295652, 0.960994, 0.903749,
    0.762234, 0.906482, 0.612438, 0.633764, 0.825681,
    0.021075, 0.018624, 0.924127, 0.861208, 0.861556,
    0.41393, 0.551733, 0.80481, 0.042195, 0.64914,
    0.349604, 0.095385, 0.267151, 0.435061, 0.901198,
    0.820168, 0.555224, 0.861995, 0.965973, 0.735315,
    0.858775, 0.379762, 0.508588, 0.907571, 0.038967,
    0.211966, 0.212726, 0.777375, 0.803119, 0.900774,
    0.821933, 0.619674, 0.893804, 0.109495, 0.033824
])
    ks_test.checkTest()
    print(ks_test.d_max)
    print(ks_test.d_max_p)
    print(ks_test.passed)
    ks_test.plotDs()

if __name__ == "__main__":
    main()