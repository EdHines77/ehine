# GLOBAL VARIABLES
valid = False


# MAIN CODE

def checksum(card_no):
    total = 0
   
    for i in range(0, 16):
        digit = int(card_no[i])
        if i % 2 == 0:
            digit *= 2
            if digit >= 10:
                digit = digit // 10 + digit % 10
        total += digit
 
    if total % 10 == 0:
        return 'Valid number'
    else:
        return 'Invalid number'


card_number = input('Enter your card number: ')

while not valid:
 
    if len(card_number) == 16:
        try:
            int(card_number)
            valid = True
        except:
            print('Please enter an integer: ')
    else:
        print('Please enter a 16 digit number: ')
 
   
print(checksum(card_number))