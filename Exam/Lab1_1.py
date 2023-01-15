Budget = 500
Economy = 750
Vip = 2000
Bag_included = 200
Meal_included = 150
print('Tickets typs: ')
print('1. Budget  ( 500)')
print('2. Economy ( 750)')
print('3. VIP     (2000)')
print('\t')
Added_bag = 0
Added_meal = 0
ticket = int(input('Input ticket type >> '))
print('\t')
while True:
    print('Currently you have:')
    print(f'    {Added_bag} bag(s) registered')
    print(f'    {Added_meal} meals(s) registered')
    print('\t')
    print('Here are your options:')
    print('1. Add bag (max 1)')
    print('2. Add meal (max 1)')
    print('3. Remove bag')
    print('4. Remove meal')
    print('5. Finalize ticket')
    options = int(input('Your choice >> '))
    print('\t')
    if options == 1:
        Added_bag = 1
    elif options == 2:
        Added_meal = 1
    elif options == 3:
        Added_bag = 0
    elif options == 4:
        Added_meal = 0
# budget ticket
    elif options == 5 and Added_bag == 0 and Added_meal == 0 and ticket == 1:
        total = Budget + Added_bag + Added_meal
        print('Receipt:')
        print(f'Ticket :  {Budget}kr')
        print('        -------')
        print(f'Total  :  {total}kr')
        break
    elif options == 5 and Added_bag == 1 and Added_meal == 0 and ticket == 1:
        total_1 = Budget + Bag_included
        print('Receipt:')
        print(f'Ticket :  {Budget}kr')
        print(f'Bag    :  {Bag_included}kr')
        print('        -------')
        print(f'Total  :  {total_1}kr')
        break
    elif options == 5 and Added_bag == 0 and Added_meal == 1 and ticket == 1:
        total_2 = Budget + Meal_included
        print('Receipt:')
        print(f'Ticket :  {Budget}kr')
        print(f'Meal   :  {Meal_included}kr')
        print('        -------')
        print(f'Total  :  {total_2}kr')
        break
    elif options == 5 and Added_bag == 1 and Added_meal == 1 and ticket == 1:
        total_3 = Bag_included + Meal_included + Budget
        print('Receipt:')
        print(f'Ticket :  {Budget}kr')
        print(f'Bag    :  {Bag_included}kr')
        print(f'Meal   :  {Meal_included}kr')
        print('        -------')
        print(f'Total  :  {total_3}kr')
        break
# economy ticket
    elif options == 5 and Added_bag == 0 and Added_meal == 0 and ticket == 2:
        total_2_1 = Economy + Added_bag + Added_meal
        print('Receipt:')
        print(f'Ticket :  {Economy}kr')
        print('        -------')
        print(f'Total  :  {total_2_1}kr')
        break
    elif options == 5 and Added_bag == 1 and Added_meal == 0 and ticket == 2:
        total_2_2 = Economy + Bag_included
        print('Receipt:')
        print(f'Ticket :  {Economy}kr')
        print(f'Bag    :  {Bag_included}kr')
        print('        -------')
        print(f'Total  :  {total_2_2}kr')
        break
    elif options == 5 and Added_bag == 0 and Added_meal == 1 and ticket == 2:
        total_2_3 = Economy + Meal_included
        print('Receipt:')
        print(f'Ticket :  {Economy}kr')
        print(f'Meal   :  {Meal_included}kr')
        print('        -------')
        print(f'Total  :  {total_2_3}kr')
        break
    elif options == 5 and Added_bag == 1 and Added_meal == 1 and ticket == 2:
        total_2_3 = Bag_included + Meal_included + Economy
        print('Receipt:')
        print(f'Ticket :  {Economy}kr')
        print(f'Bag    :  {Bag_included}kr')
        print(f'Meal   :  {Meal_included}kr')
        print('        -------')
        print(f'Total  :  {total_2_3}kr')
        break
# Vip ticket
    elif options == 5 and Added_bag == 0 and Added_meal == 0 and ticket == 3:
        total_3 = Vip + Added_bag + Added_meal
        print('Receipt:')
        print(f'Ticket : {Vip}kr')
        print('        -------')
        print(f'Total  : {total_3}kr')
        break
    elif options == 5 and Added_bag == 1 and Added_meal == 0 and ticket == 3:
        total_3_1 = Vip + Bag_included
        print('Receipt:')
        print(f'Ticket :  {Vip}kr')
        print(f'Bag    :  {Bag_included}kr')
        print('        -------')
        print(f'Total  :  {total_3_1}kr')
        break
    elif options == 5 and Added_bag == 0 and Added_meal == 1 and ticket == 3:
        total_3_2 = Vip + Meal_included
        print('Receipt:')
        print(f'Ticket :  {Vip}kr')
        print(f'Meal   :  {Meal_included}kr')
        print('        -------')
        print(f'Total  :  {total_3_2}kr')
        break
    elif options == 5 and Added_bag == 1 and Added_meal == 1 and ticket == 3:
        total_3_3 = Vip + Meal_included + Bag_included
        print('Receipt:')
        print(f'Ticket : {Vip}kr')
        print(f'Bag    :  {Bag_included}kr')
        print(f'Meal   :  {Meal_included}kr')
        print('        -------')
        print(f'Total  : {total_3_3}kr')
        break
