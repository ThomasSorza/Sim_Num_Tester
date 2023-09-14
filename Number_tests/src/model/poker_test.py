from numpy import mean, var
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import re

class PokerTest:
    def __init__(self, ri_nums):
        self.ri_nums = ri_nums
        #probabilidades de la cada mano, segun tabla de poker o un libro de estadistica :)
        self.prob = [0.3024, 
                        0.504,
                        0.108,
                        0.072,
                        0.009,
                        0.0045,
                        0.0001
        ]
        #cat: oi, prob, ei, (oi-ei)^2/ei
        self.oi = [0,0,0,0,0,0,0]
        self.ei = []
        self.eid = []
        self.passed = False
        self.n = len(ri_nums)
        self.total_sum = 0.0
        self.chi_reverse = st.chi2.ppf(1 - 0.05, 6)

    def check_poker(self):
        self.calculate_oi()
        self.calculate_ei()
        self.calculate_eid()
        self.calculate_total_sum()
        if (self.total_sum < self.chi_reverse):
            self.passed = True
        else:
            self.passed = False
        return self.passed
    
    def calculate_total_sum(self):
        for num in self.eid:
            self.total_sum += num
    
    def calculate_chi_reverse(self):
        #seis grados de libertad (porque Grados --> 7 manos -1 = 6)
        #alpha = 0.05
        st.chi2.ppf(1 - 0.05, 6)

    def calculate_oi(self):
        
        for n in self.ri_nums:
            arr = str(n).split(".")
            num = arr[1]
            if self.all_diff(str(num)):  # all different
                self.oi[0] += 1
            elif self.all_same(str(num)):  # all same
                self.oi[6] += 1
            elif self.four_of_a_kind(str(num)):  # four of a kind
                self.oi[5] += 1
            elif self.one_three_of_a_kind_and_one_pair(str(num)):  # one three of a kind and one pair (Full house)
                self.oi[4] += 1
            elif self.only_three_of_a_kind(str(num)):  # only three of a kind
                self.oi[3] += 1
            elif self.two_pairs(str(num)):  # two pairs
                self.oi[2] += 1
            elif self.only_one_pair(str(num)):  # only one pair
                self.oi[1] += 1
    
    def  all_diff(self, numstr):
        return len(numstr) == len(set(numstr))
    
    def all_same(self, numstr):
        return len(set(numstr)) == 1
    
    def four_of_a_kind(self, numstr):
        count = {}
        for char in numstr:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        num_quads = sum(1 for freq in count.values() if freq == 4)

        return num_quads == 1
    
    def two_pairs(self, numstr):
        count = {}
        for char in numstr:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        num_pairs = sum(1 for freq in count.values() if freq == 2)

        return num_pairs == 2
    
    def one_three_of_a_kind_and_one_pair(self, numstr):
        count = {}
        for char in numstr:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        num_pairs = sum(1 for freq in count.values() if freq == 2)
        num_triples = sum(1 for freq in count.values() if freq == 3)

        return num_pairs == 1 and num_triples == 1

    def only_one_pair(self, numstr):
        count = {}
        for char in numstr:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        num_pairs = sum(1 for freq in count.values() if freq == 2)

        return num_pairs == 1

    def only_three_of_a_kind(self, numstr):
        count = {}
        for char in numstr:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        num_triples = sum(1 for freq in count.values() if freq == 3)

        return num_triples == 1
    
    def calculate_ei(self):
        for i in range(0, 7):
            self.ei.append(self.prob[i] * self.n)

    def calculate_eid(self):
        for i in range(0, len(self.oi)):
            if (self.prob[i] * self.n) != 0:
                self.eid.append(((self.oi[i] - self.prob[i] * self.n) ** 2) / (self.prob[i] * self.n))
            
    import matplotlib.pyplot as plt

    def plot_totalSum_vs_chiReverse(self):
        if self.n != 0:
            x = ['SUM (Ei - Oi)2 / Ei', 'Chi2_reverse']  
            y = [self.total_sum, self.chi_reverse]    
            colors = ['purple', 'yellow']
            fig, ax = plt.subplots()
            bars = plt.bar(x, y, color=['purple', 'yellow'])
            plt.bar(x, y, edgecolor='black', color=colors)
            plt.xlabel('Índices')
            plt.ylabel('Valores')
            plt.title('Gráfico de Barras: chi_reverse vs. total_sum')
            for bar, value in zip(bars, y):
                ax.annotate(str(value), xy=(bar.get_x() + bar.get_width() / 2, value), xytext=(0, 1),
                            textcoords='offset points', ha='center', va='bottom')
            # Mostrar el gráfico
            plt.show()
    
    def plot_oi_vs_ei(self):
        if self.n != 0:
            # Datos de ejemplo para las 7 barras delanteras y traseras
            hands = ['D', 'O', 'T', 'K', 'F', 'P', 'Q'] #TODO: cambiar a manos
            oi = self.oi #obtenidas
            ei = self.ei #esperadas

            # Ajuste para desplazar ligeramente las barras
            ancho_barra = 0.35
            indice = np.arange(len(hands))
            ancho_total = 0.4  # Ancho total de ambas barras

            # Crear el gráfico de barras desplazadas
            fig, ax = plt.subplots()
            oi = ax.bar(indice - ancho_barra / 2, oi, ancho_barra, label='optenidas')
            ei = ax.bar(indice + ancho_barra / 2, ei, ancho_barra, label='esperadas', alpha=0.7)

            ax.set_xlabel('Hands')
            ax.set_ylabel('Frecuency')
            ax.set_title('Hands vs Frecuency (Obtained vs Expected)')
            ax.set_xticks(indice)
            ax.set_xticklabels(hands)
            ax.legend()

            plt.show()
        
    def __str__(self):
        return f"PokerTest(ri_nums={self.ri_nums}, prob={self.prob}, oi={self.oi}, ei={self.ei}, eid={self.eid}, passed={self.passed}, n={self.n}, total_sum={self.total_sum}, chi_reverse={self.chi_reverse})"

    
def main():
        poker = PokerTest([
    0.79817, 0.68468, 0.58381,
    0.11612, 0.32584, 0.15024,
    0.28316, 0.61384, 0.44471,
    0.90924, 0.39663, 0.12679,
    0.19981, 0.08535, 0.05599])
        poker.check_poker()
        print(poker.oi)
        print(poker.ei)
        print(poker.eid)
        print(poker.total_sum)
        print(poker.chi_reverse)
        print(poker.passed)
        poker.plot_totalSum_vs_chiReverse()
        poker.plot_oi_vs_ei()
        

if __name__ == "__main__":
        main() 
