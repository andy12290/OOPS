import Standard_module as mm

import sys

# first we will see the module we have imported in our editor

courses = ['Aniket', 'Kale', 'Karjat']

index = mm.search_index(courses,'Karjat')
#print(index)

# Where progs will search the files
print(sys.path)