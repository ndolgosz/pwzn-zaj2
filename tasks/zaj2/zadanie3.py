# -*- coding: utf-8 -*-

import math


class Integrator(object):

    """
    Klasa która implementuje całki metodą Newtona Cotesa z użyciem interpolacji
    N-tego stopnia :math:`n\in<2, 11>`.

    .. note::

        Używamy wzorów NC nie dlatego że są super przydatne (zresztą gorąco
        zniechęcam Państwa przed pisaniem własnych podstawowych algorytmów
        numerycznych --- zbyt łatwo o głupi błąd) ale dlatego żebyście
        jescze raz napisali jakiś algorytm w którym nie opłaca się zrobić 11
        ifów.

    """
 
    @classmethod
    def get_level_parameters(self, level):
        """

        :param int level: Liczba całkowita większa od jendości.
        :return: Zwraca listę współczynników dla poszczególnych puktów
                 w metodzie NC. Na przykład metoda NC stopnia 2 używa punktów
                 na początku i końcu przedziału i każdy ma współczynnik 1,
                 więc metoda ta zwraca [1, 1]. Dla NC 3 stopnia będzie to
                 [1, 3, 1] itp.
        :rtype: List of integers
        """
        if level == 2:
		self.wspolczynnik = 2
                return [1,1]
        elif level == 3:
		self.wspolczynnik = 3
                return [1,4,1]
        elif level == 4:
		self.wspolczynnik = 8/3.
                return [1,3,3,1]
	elif level == 5:
		self.wspolczynnik = 45/2.
                return [7,32,12,32,7]

    def __init__(self, level):
        """
        Funkcja ta inicjalizuje obiekt do działania dla danego stopnia metody NC
        Jeśli obiekt zostanie skonstruowany z parametrem 2 używa metody trapezów.
        :param level: Stopień metody NC
        """
	if level in range(2,6):
                self.level = level
        else: print("Wrong level number - choose between 2 and 5")

    def integrate(self, func, func_range, num_evaluations):
        """
        Funkcja dokonuje całkowania metodą NC.

        :param callable func: Całkowana funkcja, funkcja ta ma jeden argument,
                              i jest wołana w taki sposób: `func(1.0)`.
        :param Tuple[int] func_range: Dwuelementowa krotka zawiera początek i koniec
                                 przedziału całkowania.
        :param int num_evaluations: Przybliżona lość wywołań funkcji ``func``,
            generalnie algorytm jest taki:

            1. Dzielimy zakres na ``num_evaluations/self.level`` przdziałów.
               Jeśli wyrażenie nie dzieli się bez reszty, należy wziąć najmiejszą
               liczbę całkowitą większą od `num_evaluations/self.level``. 
            2. Na każdym uruchamiamy metodę NC stopnia ``self.level``
            3. Wyniki sumujemy.

            W tym algorytmie wykonamy trochę więcej wywołań funkcji niż ``num_evaluations``,
            dokłanie ``num_evaluations`` byłoby wykonywane gdyby keszować wartości
            funkcji na brzegach przedziału całkowania poszczególnych przedziałów.

        :return: Wynik całkowania.
        :rtype: float
        """
	
        params = self.get_level_parameters(self.level)
	print params
 
        h = (func_range[1]-func_range[0])/(num_evaluations*(self.level-1))
	print "h i wspolczynnik"
      	print h, self.wspolczynnik
        sum = 0
	x = func_range[0]
	for i in range(num_evaluations):
                for p in params:
                        sum = sum + p*func(x)
			print sum
                        x=x+h
	print "WYNIK:"
	print sum*h/self.wspolczynnik
	return sum*h/self.wspolczynnik
              


if __name__ == '__main__':
    i = Integrator(5)
    print(i.integrate(math.cos, (0, 2*math.pi), 30))
    #print(i.integrate(lambda x: x*x, (0, 1), 30))
