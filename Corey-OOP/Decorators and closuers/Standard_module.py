

# finding the serach in our list or anywhere

print('imported my module')

def search_index(to_search, target):
    "This is module to serach the text or list"

    for i, value in enumerate (to_search):
        if value == target:
            return i

    return -1
