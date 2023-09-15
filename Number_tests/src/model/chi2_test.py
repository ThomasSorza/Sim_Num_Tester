from typing import Any
from scipy.stats import chi2
import numpy as np
import matplotlib.pyplot as plt
class ChiTest:
    def __init__(self, ri_values =[], a=8, b=10, intervals_amount = 8):
        self.ri_values = ri_values
        self.ni_values = []
        self.a = a
        self.b = b
        self.num_amount = len(ri_values)
        self.intervals_amount = intervals_amount
        self.intervals_values = []
        self.frequency_obtained = []
        self.expected_frequency = []
        self.chi_squared_values = []
        self.passed = False

    def fillNiValues(self):
        for i in range(self.num_amount):
            value = self.a + (self.b - self.a) * self.ri_values[i]
            self.ni_values.append(value)

    def sortNiArray(self):
        self.ni_values.sort()

    def obtainMinNiValue(self):
        return min(self.ni_values)

    def obtainMaxNiValue(self):
        return max(self.ni_values)

    def fillIntervalsValuesArray(self):
        min_value = self.obtainMinNiValue()
        max_value = self.obtainMaxNiValue()
        self.intervals_values.append(min_value)

        for i in range(self.intervals_amount):
            value = round(self.intervals_values[i] + (max_value - min_value) / self.intervals_amount, 5)
            self.intervals_values.append(value)

    def fillFrequenciesArrays(self):
        expected_freq = round(float(len(self.ni_values)) / self.intervals_amount, 2)
        counter = 0

        for i in range(len(self.intervals_values) - 1):
            for j in range(len(self.ni_values)):
                if (self.ni_values[j] >= self.intervals_values[i]) and (self.ni_values[j] < self.intervals_values[i + 1]):
                    counter += 1
            self.frequency_obtained.append(counter)
            self.expected_frequency.append(expected_freq)
            counter = 0

    def fillChiSquaredValuesArray(self):
        for i in range(len(self.frequency_obtained)):
            value = round(((self.frequency_obtained[i] - self.expected_frequency[i]) ** 2) / self.expected_frequency[i], 2)
            self.chi_squared_values.append(value)

    def cumulativeObtainedFrequency(self):
        result = sum(self.frequency_obtained)
        return result

    def cumulativeExpectedFrequency(self):
        result = sum(self.expected_frequency)
        return result

    def cumulativeChiSquaredValues(self):
        result = sum(self.chi_squared_values)
        return result

    def chi_squared_test_value(self):
        margin_of_error = 0.05
        degrees_of_freedom = self.intervals_amount - 1

        chiSquared = chi2(degrees_of_freedom)
        return chiSquared.ppf(1.0 - margin_of_error)

    def check_test(self):
        self.fillNiValues()
        self.sortNiArray()
        self.fillIntervalsValuesArray()
        self.fillFrequenciesArrays()
        self.fillChiSquaredValuesArray()
        if self.cumulativeChiSquaredValues() <= self.chi_squared_test_value():
            self.passed = True
        else:
            self.passed = False
            
    def plotChi2(self):
        x = ["Sumatoria de Valores Chi2", "Valor de la prueba Chi2Inversa"]
        y = [self.cumulativeChiSquaredValues(), self.chi_squared_test_value()]

        fig, ax = plt.subplots()
        bars = plt.bar(x, y, color=['yellow', 'red'])
        plt.title('Tabla comparacion Chi2 margen de error calculado y Chi2Inversa')
        plt.ylabel('Values')
        plt.xlabel('Valores de Chi2')

        # Agregar etiquetas de valor en las barras
        for bar, value in zip(bars, y):
            ax.annotate(str(value), xy=(bar.get_x() + bar.get_width() / 2, value), xytext=(0, 1),
                        textcoords='offset points', ha='center', va='bottom')
        plt.show()
        
    def plotFrequencies(self):
        # Crear un rango de valores para el eje x (los intervalos)
        x = np.arange(len(self.intervals_values) - 1)

        # Ancho de las barras
        width = 0.35

        # Crear la figura y el eje
        fig, ax = plt.subplots()

        # Crear barras para las frecuencias observadas y esperadas
        bars_observed = ax.bar(x - width/2, self.frequency_obtained, width, label='Frecuencia Observada')
        bars_expected = ax.bar(x + width/2, self.expected_frequency, width, label='Frecuencia Esperada')

        # Etiquetas y leyenda
        ax.set_xlabel('Intervalos')
        ax.set_ylabel('Frecuencia')
        ax.set_title('Frecuencias Observadas y Esperadas en Cada Intervalo')

        # Construir las etiquetas de intervalos con el rango
        interval_labels = [f'Intervalo {i + 1}: [{self.intervals_values[i]:.3f}, {self.intervals_values[i+1]:.3f})' for i in range(len(x))]

        # Rotar las etiquetas de intervalos diagonalmente
        ax.set_xticks(x)
        ax.set_xticklabels(interval_labels, rotation=45, ha='right')

        ax.legend()

        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    udm = ChiTest([
    0.96383,
    0.71968,
    0.49937,
    0.39344,
    0.83499,
    0.72372,
    0.46416,
    0.89852,
    0.31497,
    0.34828,
    0.11213,
    0.67328,
    0.87569,
    0.72191,
    0.17735
    ],8, 10, 8)
    
    udm.check_test()
    print(udm.chi_squared_values)
    print(udm.intervals_values)
    print(udm.frequency_obtained)
    print(udm.passed)
    udm.plotChi2()
    udm.plotFrequencies()
    