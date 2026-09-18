from math import ceil

def pizza(n_people, slices_per_pizza):
    return ceil(n_people / slices_per_pizza)