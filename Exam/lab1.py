Budget = 500
Economy = 750
Vip = 2000
Bag_included = 200
Meal_included = 150

Added_bag = 0
Added_meal = 0
print('Tickets typs: ')
print(f'1. Budget : 500')
print(f'2. Economy: 750')
print(f'3. VIP    : 2000 ')
print('\t')
ticket_type = int(input('Input ticket type >> '))
print('\t')
if ticket_type == 1:
  while True:
   print('Currently you have:')
   print(f'    {Added_bag} bag(s) registered')
   print(f'    {Added_meal} meals(s) registered')
   print( )
   print('Here are your options:')
   print('1. Add bag (max 1)')
   print('2. Add meal (max1)')
   print('3. Remove bag')
   print('4. Remove meal')
   print('5. Finalize ticket')
   options = int(input('Your choice >> '))
   if options == 1:
    Added_bag += 1
   elif options == 2:
    Added_meal += 1
   elif options == 3:
    Added_bag -= 1
   elif options == 4:
    Added_meal -= 1
   else:
    Bag_price = Bag_included * Added_bag
    meal_price = Meal_included * Added_meal
    print('Receipt:')
    print(f'Ticket :  {Budget}kr')
    print(f'Bag    :  {Bag_price}kr')
    print(f'Meal   :  {meal_price}kr')
    print('         -------')
    total = Budget + meal_price + Bag_price
    print(f'Total  :  {total}kr')
    break  
elif ticket_type == 2:
   Added_bag_2 = 0
   Added_meal_2 = 0
   while True:
    print('Currently you have:')
    print(f'    {Added_bag_2} bag(s) registered')
    print(f'    {Added_meal_2} meals(s) registered')
    print( )
    print('Here are your options:')
    print('1. Add bag (max 1)')
    print('2. Add meal (max1)')
    print('3. Remove bag')
    print('4. Remove meal')
    print('5. Finalize ticket')
    options = int(input('Your choice >> '))
    print('\t')
    if options == 1:
      Added_bag_2 += 1
    elif options == 2:
      Added_meal_2 += 1
    elif options == 3:
      Added_bag_2 -= 1
    elif options == 4:
      Added_meal_2 -= 1
    else:
      Bag_price_1 = Bag_included * Added_bag_2
      meal_price_1 = Meal_included * Added_meal_2
      print('Receipt:')
      print(f'Ticket :  {Economy}kr')
      print(f'Bag    :  {Bag_price_1}kr')
      print(f'Meal   :  {meal_price_1}kr')
      print('         -------')
      total_1 = Economy + Bag_price_1 + meal_price_1
      print(f'Total  :  {total_1}kr')
      break
else:
    Added_bag_3 = 0
    Added_meal_3 = 0
    while True:
     print('Currently you have:')
     print(f'    {Added_bag_3} bag(s) registered')
     print(f'    {Added_meal_3} meals(s) registered')
     print( )
     print('Here are your options:')
     print('1. Add bag (max 1)')
     print('2. Add meal (max1)')
     print('3. Remove bag')
     print('4. Remove meal')
     print('5. Finalize ticket')
     options = int(input('Your choice >> '))
     if options == 1:
      Added_bag_3 += 1
     elif options == 2:
      Added_meal_3 += 1
     elif options == 3:
      Added_bag_3 -= 1
     elif options == 4:
      Added_meal_3 -= 1
     else:
      Bag_price_2= Bag_included * Added_bag_3
      meal_price_2 = Meal_included * Added_meal_3
      print('Receipt:')
      print(f'Ticket :  {Vip}kr')
      print(f'Bag    :  {Bag_price_2}kr')
      print(f'Meal   :  {meal_price_2}kr')
      print('         -------')
      total_3 = Vip + Bag_price_2 + meal_price_2
      print(f'Total  :  {total_3}kr')
      break