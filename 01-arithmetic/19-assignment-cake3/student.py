def cake3(eggs, flour, butter, sugar):
    limited_eggs = eggs // 5 
    limited_flour = flour //  250
    limited_butter = butter // 200
    limited_sugar = sugar // 250
    return min(limited_eggs,limited_flour, limited_butter,limited_sugar)

