import math,random,sys

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

print('enter a number to compute collatz')
while True:
    try:
        userInter = int(input('please enter a number: '))
        break
    except:
        print(' user please enter a number not a string')
        continue

collatzNumber = collatz(userInter)


while collatzNumber != 1:
    collatzNumber = collatz(int(collatzNumber))
else:
    print('collatz found')
