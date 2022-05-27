import random

def start():
    file = open('scores.txt' , 'w')
    file.write('This is your dice roller history')
    user = input('What is your name?')
    file.write('\nWelcome' + user)
    print ('These are your scores:')
    file.close()
    
def d_roller():
    play = 1
    Round = 0
    while play == 1:
        begin = input ('\nWould you like to play dice roller? Y or N :')
        if begin == 'N':
            history()
            play = 2
        elif begin == 'Y':
            
            Round = Round + 1
            print('Ok lets get started')
            print('You will get to role 3 dice. The goal is for all three to add up and to have the highest score.\n\n')
            role1 = random.randint(1,6)
            role2 = random.randint(1,6)
            role3 = random.randint(1,6)
            
            print('Your scores were:')
            print(role1)
            print(role2)
            print(role3)
            total = role1 + role2 + role3
            print('\n Your total was: ')
            print(total)
            
            file = open('scores.txt' , 'a')
            file.write('\n\nRound: ')
            file.write(str(Round))
            file.write('\nYour scores were: ')
            file.write(str(role1))
            file.write(' , ')
            file.write(str(role2))
            file.write(' , ')
            file.write(str(role3))
            file.write('\nYour total was: ')
            file.write(str(total))
            file.close()
            
def history():
    read_h = input('\nWould you like to see your game scores? Y or N: ')
    if read_h == 'Y':
        file = open('scores.txt', 'r')
        previous_scores = file.read()
        print(previous_scores)
        file.close
        
    else:
        print('OK thanks for playing')
        
def main():
    start()
    d_roller()
    
main()