spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    new_list = []
    for item in spicy_foods:
        new_list.append(item['name'])
    return(new_list)

def get_spiciest_foods(spicy_foods):
    return [item for item in spicy_foods if item['heat_level'] > 5]


def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print(item['name'] + ' (' + item['cuisine'] + ') | Heat Level: ' + '🌶'*item['heat_level'] )

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if(item['cuisine'] == cuisine):
            return item

def print_spiciest_foods(spicy_foods):
    print_spicy_foods([item for item in spicy_foods if item['heat_level'] > 5])

def get_average_heat_level(spicy_foods):
    sum_heat = 0
    for item in spicy_foods:
        sum_heat = sum_heat + item['heat_level']
    return(sum_heat / len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    new_list = [item for item in spicy_foods]
    new_list.append(spicy_food)
    return(new_list)
