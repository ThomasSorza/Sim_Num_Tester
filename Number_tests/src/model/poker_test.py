from numpy import mean, var
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import re

class PokerTest:
    """
    Clase que implementa la Prueba de Poker para una secuencia de números generados.
    """
    def __init__(self, ri_nums):
        """
        Inicializa una instancia de PokerTest.

        :param ri_nums: Lista de números generados.
        """
        self.ri_nums = ri_nums
        # Probabilidades de cada mano, según una tabla de poker o un libro de estadísticas.
        self.prob = [0.3024, 0.504, 0.108, 0.072, 0.009, 0.0045, 0.0001]
        # Categorías: oi, prob, ei, (oi-ei)^2/ei
        self.oi = [0, 0, 0, 0, 0, 0, 0]
        self.ei = []
        self.eid = []
        self.passed = False
        self.n = len(ri_nums)
        self.total_sum = 0.0
        self.chi_reverse = st.chi2.ppf(1 - 0.05, 6)  # Valor crítico de chi-cuadrado

    def check_poker(self):
        """
        Realiza la Prueba de Poker y establece si ha sido superada.
        :return: True si la prueba es superada, False en caso contrario.
        """
        self.calculate_oi()
        self.calculate_ei()
        self.calculate_eid()
        self.calculate_total_sum()
        if self.total_sum < self.chi_reverse:
            self.passed = True
        else:
            self.passed = False
        return self.passed

    def calculate_total_sum(self):
        """
        Calcula la suma total de (ei - oi)^2 / ei.
        """
        for num in self.eid:
            self.total_sum += num

    def calculate_oi(self):
        """
        Calcula las frecuencias observadas para cada categoría de manos de poker.
        """
        for n in self.ri_nums:
            arr = str(n).split(".")
            num = arr[1]
            if self.all_diff(str(num)):  # Todas diferentes
                self.oi[0] += 1
            elif self.all_same(str(num)):  # Todas iguales
                self.oi[6] += 1
            elif self.four_of_a_kind(str(num)):  # Cuatro iguales
                self.oi[5] += 1
            elif self.one_three_of_a_kind_and_one_pair(str(num)):  # Tres iguales y un par (Full house)
                self.oi[4] += 1
            elif self.only_three_of_a_kind(str(num)):  # Solo tres iguales
                self.oi[3] += 1
            elif self.two_pairs(str(num)):  # Dos pares
                self.oi[2] += 1
            elif self.only_one_pair(str(num)):  # Solo un par
                self.oi[1] += 1

    def all_diff(self, numstr):
        """
        Comprueba si todos los dígitos son diferentes en una cadena de caracteres.
        :param numstr: Cadena de caracteres a evaluar.
        :return: True si todos son diferentes, False en caso contrario.
        """
        return len(numstr) == len(set(numstr))

    def all_same(self, numstr):
        """
        Comprueba si todos los dígitos son iguales en una cadena de caracteres.
        :param numstr: Cadena de caracteres a evaluar.
        :return: True si todos son iguales, False en caso contrario.
        """
        return len(set(numstr)) == 1

    def four_of_a_kind(self, numstr):
        """
        Comprueba si hay cuatro dígitos iguales en una cadena de caracteres.
        :param numstr: Cadena de caracteres a evaluar.
        :return: True si hay cuatro iguales, False en caso contrario.
        """
        count = {}
        for char in numstr:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        num_quads = sum(1 for freq in count.values() if freq == 4)

        return num_quads == 1

    def two_pairs(self, numstr):
        """
        Comprueba si hay dos pares de dígitos iguales en una cadena de caracteres.
        :param numstr: Cadena de caracteres a evaluar.
        :return: True si hay dos pares iguales, False en caso contrario.
        """
        count = {}
        for char in numstr:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        num_pairs = sum(1 for freq in count.values() if freq == 2)

        return num_pairs == 2

    def one_three_of_a_kind_and_one_pair(self, numstr):
        """
        Comprueba si hay tres dígitos iguales y un par en una cadena de caracteres (Full house).
        :param numstr: Cadena de caracteres a evaluar.
        :return: True si se cumple la condición, False en caso contrario.
        """
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
        """
        Comprueba si hay solo un par de dígitos iguales en una cadena de caracteres.
        :param numstr: Cadena de caracteres a evaluar.
        :return: True si hay solo un par igual, False en caso contrario.
        """
        count = {}
        for char in numstr:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        num_pairs = sum(1 for freq in count.values() if freq == 2)

        return num_pairs == 1

    def only_three_of_a_kind(self, numstr):
        """
        Comprueba si hay solo tres dígitos iguales en una cadena de caracteres.
        :param numstr: Cadena de caracteres a evaluar.
        :return: True si hay solo tres iguales, False en caso contrario.
        """
        count = {}
        for char in numstr:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        num_triples = sum(1 for freq in count.values() if freq == 3)

