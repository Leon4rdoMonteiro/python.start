# DICTIONARIES

people = dict(Leonardo='Son', Claudia='Mother', Oziel='Father')

family = {
    'Leonardo': 'Son',
    'Oziel': 'Father',
    'Claudia': 'Mother'
}

if 'Leonardo' in people:
    print(people['Leonardo'])

print('People:', people)
print('Family', family)

# ITERATING DICTIONARIES 

cars = {}

cars['corola'] = 'red'
cars['fit'] = 'black'
cars['320'] = 'green'

print('Cars:', cars)

for key, value in cars.items():
    print(key + ' = ' + value)