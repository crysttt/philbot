from flask import Flask, request
import re

no_food = ['alcohol', 'chocolate', 'coffee', 'caffeine', 'citrus', 'coconut', 'grapes', 'rasins', 'nuts', 'milk', 'dairy', 'onion', 'garlic', 'chives', 'raw meat', 'raw egg', 'salt', 'fat trimmings', 'avocado']
specific = {'dog': ['cinnamon', 'ice cream', 'medicine', 'cat food'], 'cat': ['tuna', 'dog food', 'liver'], 'dinosaur': ['marshmellows', 'birthday cake'] ,'bird': ['apple seeds', 'mushrooms', 'tomato leaves', 'dried beans']}
name = 'Toto'

def no_query_on_enter_state(context):
    return ""
def no_query_on_input(line, context):
    species = "dinosaur"
    match = re.search('can my pet eat (?P<food>.*)\?', line, re.IGNORECASE)
    if match:
        food = match.group(1)
        #acess database for species
        return ('FOOD_SPECIES', {"food" : food, "species": species}, None)

    match = re.search(f'can {name} eat (?P<food>.*)\?', line, re.IGNORECASE)
    if match:
        food = match.group(1)
        return ('FOOD_SPECIES', {"food" : food, "species": species}, None)

    match = re.search('can (?P<species>.*) eat (?P<food>.*)\?', line, re.IGNORECASE)
    if match:
        species = match.group(1)
        food = match.group(2)
        return ('FOOD_SPECIES', {'food' : food, "species": species}, None)

    else:
        return('NO_QUERY', {}, 'Sorry, I do not understand')

def food_species_on_enter_state(context):
    #pls fix this
    food = context['food']
    species = context['species']
    if food in no_food:
        return f'{name} cannot eat {food}.'
    elif species in specific:
        if food in specific[species]:
            return f'{name} cannot eat {food}.'
        else:
            return f'{name} can eat {food}.'
            
    else:
        return f'We do not have info on {food}.'


def food_species_on_input(line,context):
    return ('NO_QUERY', {}, None)
    
#def food_on_enter_state(context):
#    return ()
#def food_on_input(line,context):

ON_INPUT= {
    'NO_QUERY': no_query_on_input,
    'FOOD_SPECIES': food_species_on_input
}
ON_ENTER_STATE= {
    'NO_QUERY': no_query_on_enter_state,
    'FOOD_SPECIES': food_species_on_enter_state
}