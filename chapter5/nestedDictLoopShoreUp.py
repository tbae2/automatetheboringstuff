allGuests = {
    'bob': {
        'apples':5,
        'pretzels': 10
    },
    'ashley': {
        'ham': 2,
        'apples' : 4
    },
    "susan": {
        'apples': 2,
        'steak': 3
    }
}

def itemsBrought(guestsdict,itemtocheck):
    itemCount = 0
    for key, value in guestsdict.items():
        itemCount += value.get(itemtocheck,0)
    return itemCount


print('Number of things being brought')
print('- apples    ' + str(itemsBrought(allGuests,'apples')))
print('- pretzels: ' + str(itemsBrought(allGuests,'pretzels')))
print('- steak:    ' + str(itemsBrought(allGuests,'steak')))