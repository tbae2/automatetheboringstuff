myFurballs = ['Evey','Quorra','Riddick','Tetris','Guinevere']
print('Enter a name of one of my pets if you know it ')
petname = input()
if petname not in myFurballs:
    print("I don't have a pet named" + petname)
else:
    print(petname + " is my pet")