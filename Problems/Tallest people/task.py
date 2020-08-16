def tallest_people(**kwargs):
    most_tall = max(kwargs.values())
    for k, v in sorted(kwargs.items()):
        if v == most_tall:
            print(k, ':', v)
