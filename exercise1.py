#Exercise 1
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'],
    'pocket' : ['seashell', 'strange berry', 'lint'],
}
print(inventory['backpack'])
inventory['backpack'].sort()
print(inventory['backpack'])
inventory['backpack'].remove('dagger')
print(inventory['backpack'])
inventory['gold'] += 50


print(inventory['gold'])

