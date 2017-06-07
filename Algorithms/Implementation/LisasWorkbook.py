#!/bin/python3
import sys

nb_chapters, nb_problems_per_page = [int(_) for _ in input().strip().split(' ')]
nb_problems = [int(c_temp) for c_temp in input().strip().split(' ')]

nb_specials = 0
current_page = 1
for i_chapter in range(0, nb_chapters):
    current_nb_exercices_on_page = 0
    for i_problem in range(1, nb_problems[i_chapter] + 1):
        #print("page: {} chapter: {} exercise: {}".format(current_page, i_chapter+1, i_problem))
        nb_specials += current_page == i_problem
        current_nb_exercices_on_page += 1
        if current_nb_exercices_on_page == nb_problems_per_page:
            current_page += 1
            current_nb_exercices_on_page = 0
    if current_nb_exercices_on_page > 0 and current_nb_exercices_on_page != nb_problems_per_page:
        current_page += 1
        
print(nb_specials)
