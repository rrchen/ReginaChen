def draw_stars(list):
    for num in list:
        print "*" * num

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

def draw_char(list):
    for num in list:
        if type(num) is int:
            print "*" * num
        else:
            print num[0].lower() * len(num)

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_char(y)
