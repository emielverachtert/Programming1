from math import ceil

def buses_needed(people_count, bus_capacity):
    return ceil(people_count / bus_capacity)


