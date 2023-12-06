valid = False

def plate_validation(num):
    if len(num) == 8:
        if num[0].isalpha() and num[1].isalpha() and num[2].isdigit() and num[3].isdigit() and num[5].isalpha() and num[6].isalpha() and num[7].isalpha():
            return True
        else:
            print('Invalid Numberplate')

while valid is False:
    time_taken = input('Enter the time taken (s): ')
    plate_num = input('Enter your plate number: ')

    if time_taken.isdigit() is True and plate_validation(plate_num) is True:
        time_taken = int(time_taken) / 3600
        
        if int(time_taken) > 70:
            print('You are going',time_taken, 'mph which is breaking the speed limit')
        else:
            print('You are going',time_taken, 'mph which is not breaking the speed limit')
        valid = True