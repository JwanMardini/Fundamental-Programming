print('\t')
print('Welcome to the Money Bag Transport Calculator (M.B.t.C)')
print('-------------------------------------------------------')
print('\t')
controll = True
while controll:
    volume = int(input('What is the volume of the truck (>= 100L): '))
    if volume > 100:
        # Calculation of the Big bags
        Bags_80 = int(volume / 80)
        Remain_1 = int(Bags_80 * 80)
        Remain_1_2 = int(volume - Remain_1)
        # Calculation of the Medium bags
        Bags_50 = int(Remain_1_2 / 50)
        Remain_2 = int(Bags_50 * 50)
        Remain_2_2 = int(Remain_1_2 - Remain_2)
        # Calculation of the small bags
        Bags_20 = int(Remain_2_2 / 20)
        Remain_3 = int(Bags_20 * 20)
        Remain_3_2 = int(Remain_2_2 - Remain_3)
        # Calculating the total value
        total_val = int((Bags_80 * 60000)+(Bags_50 * 30000)+(Bags_20 * 10000))
        print('\t')
        print('Packing plan')
        print('------------')
        print(f'{Bags_80} big bags')
        print(f'{Bags_50} medium bags')
        print(f'{Bags_20} small bags\n')
        # Space left is the remainder after calculating small bags
        print(f'Space left : {Remain_3_2}L')
        print(f'Total value: {total_val}kr')
        print('\t')
        controll = False
    else:
        pass
