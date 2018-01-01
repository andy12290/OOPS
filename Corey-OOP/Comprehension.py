names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

#mu_dict = {}


#for name, heros in zip(names,heros):
#    mu_dict[name] = heros

#print(mu_dict)

# comp
my_dict = {name: hero for name, hero in zip (names, heros)}
print(my_dict)