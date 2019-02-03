import time
import random
playerhp = int(15)
mercenaryhp = int(11)
archerhp = int(9)
playerpunch = int(5)
playersword = int(7)
# playerkick = random.randint (2, 8)
time.sleep(2)
print ('What is your name?')
Name = input()
print (str('Welcome, ') + (Name))
print ("Welcome to this adventure. Your best friend has been taken by an evil creature underground. It's YOUR job to rescue him!")
time.sleep(2)
print (str('Boss Battle! ') + (Name) + (' vs MERCENARY'))
time.sleep(2)
print ('Punch always does 5 damage. Kick can do anywhere between 2 and 8 damage. Choose wisely!')
time.sleep(2)
#Creating loop here
while mercenaryhp > 0 and playerhp > 0:
    playerkick = random.randint (2, 8)
    mercenaryattack = random.randint (2, 5)
    print (Name, 'has', playerhp, 'HP and MERCERNARY has', mercenaryhp, 'HP')
    time.sleep(2)
    print ('Type one of the following moves')
    time.sleep(1)
    move = input('Punch, Kick: ')
    if move.upper() == 'KICK' or 'PUNCH' :
        if move.upper() == 'KICK':
            print ('You chose', move,'.', 'you did', playerkick, 'damage!'  )
            print ('MERCENARY has', mercenaryhp-playerkick, 'HP remaining')
            mercenaryhp = mercenaryhp-playerkick
            time.sleep(1)
        if move.upper() == 'PUNCH':
            print ('You chose', move,'.', 'you did', playerpunch, 'damage!'  )
            print ('MERCENARY has', mercenaryhp-playerpunch, 'HP remaining')
            mercenaryhp = mercenaryhp-playerpunch
            time.sleep(1)
    if mercenaryhp > 0:
        print ('Boss Attack!!', mercenaryattack, 'Damage to', Name)
        playerhp = playerhp-mercenaryattack
        time.sleep(1)
    if mercenaryhp < 1:
        print ('Congratulations', Name, ', you have defeated MERCENARY!')
        time.sleep(1)
        print ('Mercenary dropped wooden sword. Wooden sword is now an optional attack.')
    if playerhp < 1:
        print ('Sorry', Name, ', you have been defeated by MERCENARY!')
print ('Boss battle!', Name, 'vs ARCHER')
time.sleep(1)
print ('Punch always does 5 damage. Kick can do anywhere between 2 and 8 damage. Sword does 7 damage, but you get hit with 1 damage as recoil. Choose wisely!')
time.sleep(1)
playerhp = int(15)
while archerhp > 0 and playerhp > 0:
    playerkick = random.randint (2, 8)
    archerattack = random.randint (6,8)
    print (Name, 'has', playerhp, 'HP and ARCHER has', archerhp, 'HP')
    time.sleep(2)
    print ('Type one of the following moves')
    time.sleep(1)
    move = input('Punch, Kick, Sword: ')
    if move.upper() == 'KICK' or 'PUNCH' or 'SWORD' :
        if move.upper() == 'KICK':
            print ('You chose', move,'.', 'you did', playerkick, 'damage!'  )
            print ('ARCHER has', archerhp-playerkick, 'HP remaining')
            archerhp = archerhp-playerkick
            time.sleep(1)
        if move.upper() == 'PUNCH':
            print ('You chose', move,'.', 'you did', playerpunch, 'damage!'  )
            print ('ARCHER has', archerhp-playerpunch, 'HP remaining')
            archerhp = archerhp-playerpunch
            time.sleep(1)
        if move.upper() == 'SWORD':
            print ('You chose', move,'.', 'you did', playersword, 'damage!'  )
            print ('ARCHER has', archerhp-playersword, 'HP remaining')
            archerhp = archerhp-playersword
            playerhp = playerhp-1
            print ('You have taken 1 HP damage recoil. You have', playerhp, ' HP remaining.')
            time.sleep(1)
    if archerhp > 0:
        print ('Boss Attack!!', archerattack, 'Damage to', Name)
        playerhp = playerhp-archerattack
        time.sleep(1)
    if archerhp < 1:
        print ('Congratulations', Name, ', you have defeated ARCHER!')
        time.sleep(1)
        print ('Archer dropped Armor. Armor gives you more HP at the beginning of your battles.')
    if playerhp < 1: 
        print ('Sorry', Name, ', you have been defeated by ARCHER!')
