def food(listvalue)
  for i in range(len(listvalue)):
    print(listvalue[i] + ', ', end="")
    if listvalue[i] == listvalue[-2]:
      print('and ' + listvalue[-1], end="")
      break
      
angela = ['carrots','masala','tofu','broccoli']
food(angela)
