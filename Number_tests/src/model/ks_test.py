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
        if self.n != 0:
            n_intervals = self.n_intervals
            interval_size = (self.max - self.min) / n_intervals
            initial = self.min
            for _ in range(n_intervals):
                new_interval = (initial, initial + interval_size)
                self.intervals.append(new_interval)
                initial = new_interval[1]
            
    def plotDs(self):
        x = ["D max (error calculado)", "Dmax p (valor KS maximo -> Tabla)"]
        y = [self.d_max, self.d_max_p]

        fig, ax = plt.subplots()
        bars = plt.bar(x, y, color=['red', 'blue'])
        plt.title('Tabla comparacion D max y Dmax p (Error y error maximo)')
        plt.ylabel('Values')
        plt.xlabel('Errores')

        # Agregar etiquetas de valor en las barras
        for bar, value in zip(bars, y):
            ax.annotate(str(value), xy=(bar.get_x() + bar.get_width() / 2, value), xytext=(0, 1),
                        textcoords='offset points', ha='center', va='bottom')
        plt.show()

    def plotIntervals(self):
        # Create a list to store interval labels
        interval_labels = []
        
        # Create lists to store observed and expected frequencies
        observed_frequencies = []
        expected_frequencies = []

        for i, interval in enumerate(self.intervals):
            # Define the label for the interval
            label = f"Interval {i + 1}: [{interval[0]:.3f}, {interval[1]:.3f})"
            interval_labels.append(label)

            # Append observed and expected frequencies to their respective lists
            observed_frequencies.append(self.prob_esp[i])
            expected_frequencies.append(self.prob_oi[i])

        # Create an array of x positions for the bars
        x = np.arange(len(interval_labels))

        # Create a bar chart
        width = 0.35  # Width of the bars
        fig, ax = plt.subplots()
        observed_bars = ax.bar(x - width / 2, observed_frequencies, width, label='Probabilidad Frecuencia Obtenida')
        expected_bars = ax.bar(x + width / 2, expected_frequencies, width, label='Probabilidad Frecuencia Esperada')

        # Add labels, title, and legend
        ax.set_xlabel('Intervalos')
        ax.set_ylabel('Frequencias')
        ax.set_title('Frecuencias Probabilidad Obtenida y Probabilidad Esperada')
        ax.set_xticks(x)
        ax.set_xticklabels(interval_labels, rotation=45, ha='right')
        ax.legend()
        plt.tight_layout()
        plt.show()

    def plotIntervalsFreq(self):
        # Create a list to store interval labels
        interval_labels = []

        # Create lists to store observed and expected frequencies
        observed_frequencies = []

        for i, interval in enumerate(self.intervals):
            # Define the label for the interval
            label = f"Interval {i + 1}: [{interval[0]:.3f}, {interval[1]:.3f})"
            interval_labels.append(label)

            # Append observed frequencies to the list
            observed_frequencies.append(self.oi[i])

        # Create an array of x positions for the bars
        x = np.arange(len(interval_labels))

        # Create a bar chart
        width = 0.35  # Width of the bars
        fig, ax = plt.subplots()
        # Add labels, title, and legend
        ax.set_xlabel('Intervalos')
        ax.set_ylabel('Frequencia de numeros en cada intervalo')
        ax.set_title('Frecuencias de numeros Obtenida para cada intervalo')
        ax.set_xticks(x)
        ax.set_xticklabels(interval_labels, rotation=45, ha='right')

        # Plot the observed frequencies as bars
        bars = ax.bar(x, observed_frequencies, width, label='Frecuencia Observada')

        # Add values on top of the bars
        for bar, oi in zip(bars, observed_frequencies):
            height = bar.get_height()
            ax.annotate(f'{oi}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

        ax.legend()
        plt.tight_layout()
        plt.show()


            
def main():
    ks_test = KsTest([
    0.442222, 0.998804, 0.71769, 0.269853, 0.568477,
    0.36, 0.411249, 0.778008, 0.009591, 0.912916,
    0.779474, 0.31009, 0.91997, 0.080992, 0.232559,
    0.609389, 0.053358, 0.851224, 0.778083, 0.652102,
    0.978415, 0.219255, 0.865409, 0.610148, 0.378051,
    0.711247, 0.569673, 0.159811, 0.523811, 0.903988,
    0.495915, 0.050326, 0.260573, 0.009727, 0.759171,
    0.842146, 0.702157, 0.697722, 0.661416, 0.998833,
    0.282094, 0.366486, 0.205575, 0.798332, 0.279457,
    0.332125, 0.422582, 0.105727, 0.537386, 0.091692
])
    ks_test.checkTest()
    print(ks_test.d_max)
    print(ks_test.d_max_p)
    print(ks_test.passed)
    print(ks_test.intervals)
    print(ks_test.oi)
    print(ks_test.prob_oi)
    ks_test.plotDs()
    ks_test.plotIntervals()
    ks_test.plotIntervalsFreq()

if __name__ == "__main__":
    main()