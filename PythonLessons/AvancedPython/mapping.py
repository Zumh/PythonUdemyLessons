# Create a mapping of states to their abbreviation

states = {
    'Oregon':'OR',
    'Florida': 'FL',
    'CALIFORNIA':'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    }

#create a basic set of staates and some cities in them

cities = {
    'CA':'San Francisco',
    'MI':'Detriot',
    'FL':'Jacksonville'
    }

#add more cities
cities['NY'] = 'New York'
cities['OR']= 'Portland'

#print out these cities
print('-'*10)
print("NY state has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-'*10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

print('-'*10)
for states, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (states, abbrev, cities[abbrev]))

