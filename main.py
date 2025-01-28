def calculate_area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

def calculate_area_of_square(side):
    area = side * side
    return area

def calculate_area_of_rectangle(length, width):
    area = length * width
    return area

# Exemple de calculs d'aire avec des lignes dupliquées
radius = 5
area_circle = calculate_area_of_circle(radius)

# Lignes dupliquées
pi = 3.14
area_circle_duplicate = pi * radius * radius  # Duplication de la logique

side = 4
area_square = calculate_area_of_square(side)

# Lignes dupliquées
area_square_duplicate = side * side  # Duplication de la logique

length = 6
width = 3
area_rectangle = calculate_area_of_rectangle(length, width)

# Lignes dupliquées
area_rectangle_duplicate = length * width  # Duplication de la logique

print(f"Aire du cercle : {area_circle}")
print(f"Aire du carré : {area_square}")
print(f"Aire du rectangle : {area_rectangle}")
