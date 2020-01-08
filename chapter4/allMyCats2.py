# good example of input and list concat 


cats = []

while True:
    print('enter the cat name' + str(len(cats)+1) + 
    '(or enter nothing to stop this script.):')
    name = input()
    if name == '':
        break
    #cats = cats + [name] #concatenating list like example but could just use .append()
    cats.append(name) # this is much shorter
print('The Cat Names entered are: ')
for catname in cats:
    print(' ' + catname)
