import math
import random
import pydoc
import re

name = 'Gurdip Singh Jheeta'
nationality ='British'

print(name.capitalize())

print(name.upper())


print(math.pi)

print(random.choice([1,2,3,4,5,6]))

print name[:6]

print name + ' ' + nationality

mylist = list(name)

print mylist[3]

print name.find('J')

print name.replace('J','j')

print name

mysplit = (name.split(' '))

print mysplit[0]

print name.rstrip().upper()

print name.count('u')

M = ([1,2,3],[4,5,6],[7,8,9])

print M
print M[1]

col2 = [row[2] for row in M]
print col2

plus2 = [row[1] + 10 for row in M if row[1]>2]
print plus2


rowTotal = [sum (row) for row in M]
print rowTotal

print (map(sum,M))

dictionary = {}

dictionary['Pattern Owner'] = 'Michael Aguiling'
dictionary['Pattern'] = 'Machine Learning'

BigData_dict = dict(PatternOwner = 'Michael Aguiling', Pattern='Big Data', Archetype='Big Data Analytics', Platform='Private Cloud')

print BigData_dict
print BigData_dict['Archetype']

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print bob2

for key in sorted(BigData_dict):
    print (key, '----', BigData_dict[key])