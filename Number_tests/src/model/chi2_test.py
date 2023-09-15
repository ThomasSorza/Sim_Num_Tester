from scipy.stats import chi2
import numpy as np

class UniformDistributionMethod:
    def __init__(self, a, b, num_amount, intervals_amount):
        self.ri_values = []
        self.ni_values = []
        self.a = a
        self.b = b
        self.num_amount = num_amount
        self.intervals_amount = intervals_amount
        self.intervals_values = []
        self.frequency_obtained = []
        self.expected_frequency = []
        self.chi_squared_values = []

    def fillRiValues(self):
        for i in range(self.num_amount):
            random_value = np.random.random()
            self.ri_values.append(round(random_value, 5))

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

if __name__ == '__main__':
    udm = UniformDistributionMethod(8, 10, 15, 8)
    udm.fillRiValues()
    udm.fillNiValues()
    udm.sortNiArray()
    udm.fillIntervalsValuesArray()
    udm.fillFrequenciesArrays()
    udm.fillChiSquaredValuesArray()

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~ Ri Values ~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(len(udm.ri_values)):
        print(udm.ri_values[i])

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~ Ni Values ~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(len(udm.ni_values)):
        print(udm.ni_values[i])

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~ Table ~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(len(udm.intervals_values) - 1):
        print(str(udm.intervals_values[i]) + " --- " + str(udm.intervals_values[i + 1]) + " --- " +
            str(udm.frequency_obtained[i]) + " --- " + str(udm.expected_frequency[i])
            + " --- " + str(udm.chi_squared_values[i]))

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~ Totals ~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Cumulative Frequency Obtained -> " + str(udm.cumulativeObtainedFrequency()))
    print("Cumulative Expected Frequency -> " + str(udm.cumulativeExpectedFrequency()))
    print("Cumulative Chi-Squared Values -> " + str(udm.cumulativeChiSquaredValues()))
    print("Chi-Squared Test -> " + str(udm.chi_squared_test_value()))