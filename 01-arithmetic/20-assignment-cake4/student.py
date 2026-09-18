def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    aantal_eggs_per_cake = eggs // eggs_per_cake 
    aantal_flour_per_cake = flour // flour_per_cake
    aantal_butter_per_cake = butter // butter_per_cake
    aantal_sugar_per_cake = sugar // sugar_per_cake
    return min(aantal_eggs_per_cake,aantal_flour_per_cake,aantal_butter_per_cake,aantal_sugar_per_cake)
