## practice fantasy game inventory 
## practice problem from the book 

#import pprint

playerInventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 23,
    'dagger': 15,
    'arrow': 12
}


def totalInventory(inventory):
    print('Inventory')
    #pprint.pprint(playerInventory)
    totalCount = 0
    for key,value in playerInventory.items():
        print(key + ' ' + str(value))
        totalCount += value
    print('total number of items: ' + str(totalCount))


totalInventory(playerInventory)

bossLoot = ['rope','rope','gold coin','gold coin']

def addLootToInventory(inventory, loot):
    for item in loot:
        inventory.get(item,0)
        inventory[item] += 1
        print(item + ' added to inventory')

addLootToInventory(playerInventory,bossLoot)
totalInventory(playerInventory)
