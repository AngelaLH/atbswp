#Fantasy Game

inventory = {}
while True:
    print('Enter an item: (blank to quit)')
    item = input()
    if item == (""):
        break
    else:
        print('Enter the amount')
        amount = input()
    
        inventory[item] = amount
print(inventory)
    
