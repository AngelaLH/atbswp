def food(listvalue)
  for i in range(len(listvalue)):
    print(listvalue[i] + ', ', end="")
    if listvalue[i] == listvalue[-2]:
      print('and ' + listvalue[-1], end="")
      break
      
angela = ['carrots','masala','tofu','broccoli']
food(angela)


# revised version with input

def lst(in):
    list_string=','.join(in[0:-1])+' and '+str(in[-1])
    print(list_string)

spam=[]
while True:
    print('Enter the list item of index '+str(len(spam))+' (or enter nothing to stop)')
    item=input()
    if item=='':
        break
    spam= spam+[item]
print('The items are arranged as:')
lst(spam)
