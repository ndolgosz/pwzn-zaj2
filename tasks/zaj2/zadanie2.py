#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pickle
import pathlib

def load_animals(large_dataset=False):
    """

    :param bool large_dataset: Jeśli wartość to True zwraca 1E6 zwierząt, w
                               przeciwnym razie 1E5. Test będzie odbywał się
                               przy 1E6 zwierząt.

    :return: Lista zwierząt
    """
    
    file_name = 'animals-small.bin' if not large_dataset else 'animals.bin'
    file = pathlib.Path(__file__).parent / file_name
    with open(str(file), 'rb') as f:
        return pickle.load(f)


def filter_animals(animal_list):
    """
    Jesteś informatykiem w firmie Noe Shipping And Handling. Firma ta zajmuje
    się międzykontynentalnym przewozem zwierząt.

    Dostałeś listę zwierząt które są dostępne w pobliskim zoo do transportu.

    Mususz z tej listy wybrać listę zwierząt które zostaną spakowane na statek,

    Lista ta musi spełniać następujące warunki:

    * Docelowa lista zawiera obiekty reprezentujące zwierzęta (tak jak animal_list)
    * Z każdego gatunku zwierząt (z tej listy) musisz wybrać dokładnie dwa
      egzemplarze.
    * Jeden egzemplarz musi być samicą a drugi samcem.
    * Spośród samic i samców wybierasz te o najmniejszej masie.
    * Dane w liście są posortowane względem gatunku a następnie nazwy zwierzęcia

    Wymaganie dla osób aspirujących na ocenę 5:

    * Ilość pamięci zajmowanej przez program musi być stała względem
      ilości elementów w liście zwierząt.
    * Ilość pamięci może rosnąć liniowo z ilością gatunków.

    Nie podaje schematu obiektów w tej liście, musicie radzić sobie sami
    (można podejrzeć zawartość listy w interaktywnej sesji interpretera).

    Do załadowania danych z listy możesz użyć metody `load_animals`.

    :param animal_list:
    """
    lista = []
    mass_dict = {'kg' : 1000, 'mg' : 0.001, 'Mg' : 1e6, 'g' : 1}
    genus_dict = {}
    for animal in animal_list:
        if animal['genus'] not in genus_dict.keys():
            genus_dict[animal['genus']] = {animal['sex'] : animal}
        else:
            if animal['sex'] not in genus_dict[animal['genus']].keys():
                genus_dict[animal['genus']].update({animal['sex'] : animal})
            else:
                mass_old = genus_dict[animal['genus']][animal['sex']]['mass'][0]
                unit = mass_dict[genus_dict[animal['genus']][animal['sex']]['mass'][1]]
                if animal['mass'][0]*mass_dict[animal['mass'][1]] < mass_old*unit:
                    genus_dict[animal['genus']][animal['sex']] = animal
         
    for item in genus_dict:
        for el in genus_dict[item]:
                lista.append(genus_dict[item][el])

   
    def keyGenus(item):
        return item['genus']
    def keyName(item):
        return item['name']
    lista.sort(key = keyName)
    lista.sort(key = keyGenus)
    return lista
        

if __name__ == "__main__":
    animals = load_animals()

filter_animals(load_animals())
