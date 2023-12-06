import random
valid = False
credit = 100
outputs = ['🍒', '🍋', '🍊', '💀', '⭐', '🔔']

attempts = credit % 20

while valid is False:
    
    credit = credit - 20

    roll_1 = random.randint(0,5)
    roll_2 = random.randint(0,5)
    roll_3 = random.randint(0,5)
    
    print(outputs[roll_1], outputs[roll_2], outputs[roll_3])

    
    # If two are the sameye
    if roll_1 == roll_2 or roll_2 == roll_3:

        # If three are the same
        if roll_1 == roll_3:

            # 3 bell
            if roll_1 == 5:
                print('You won £5')
                credit += 500

            # 3 skull
            if roll_1 == 3:
                print('You lost everything! :(')
                credit = 0

            # 3 random
            if roll_1 != 3 and roll_1 !=5:
                print('You won £1')
                credit += 100
        
    # 2 skulls    
        if roll_1 == 3:
            print('You lost £1')
            credit += -100

        # 2 random
        else:
            ('You won 50p')
            credit += 50

    # no matches
    else:
            credit += -20

    if credit <= 0:
        print('You lost all your money')
        valid = True
        
    con = input('Would you like to roll again?')
    if con[0] == 'Y':
        print('Your winnings are £' + credit/100)

        valid = True
    else:
        valid = False

            

