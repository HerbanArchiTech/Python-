


def check_anwer(guess, answer):
    ''' This is created to check whether player's input is correct
    '''
    global score 

    answer = answer.upper()
    if guess == answer:
        print('Well Done!')

        score += 1
    else:
        print('Sorry wrong answer!')

score = 0

print('Try to Guess this green plant !')

guess1 = input(' Known for it\'s medicinal versality and it\'s great use of fragrance, it also used for tummy troubles and acid reflux\n \
 A) Roseroot\t\n  B) Aloe Vera\t\n C) Mint\t\n  D) Licorice\t\n E) Eucalyptus\t\n F) Rosemary\n ')

check_anwer (guess1,'D')


guess2 = input('Usually enjoyed as a snack by Koalas and it a native plant of Australia , but it found it can found all of house of many US homes\n \
A) Roseroot\n B) Eucalyptus\n C) D) Rosemary\n E) Licorice\n F) Mint\n ') 
check_anwer(guess2, 'E')

guess3 = input('This plant spans the gamut when it comes to remedies for the skin , as beauty product it is often packaged as skins lotions and creams\n \
A) Eucalyptus\n B) Roseroot\n C) Mint\n D) Licorice\n E) Rosemary\n  F) Aloe Vera\n ')

guess4 = input('This plant has has properties like rosmarinic acid or menthtol, and helps with irritable bowel syndrome , colds ,and ulcers and much more\n \
A) Mint\n B) Eucalyptus\n C) Licorice\n D) Roseroot\n E) Aloe Vera\n F) Roseroot\n ')
check_anwer(guess4, 'C')

guess5 = input(' The therapeautic properties of this plant includes improvment of mental functioning. Other applications are : treating burns, ingestions. anit-inflammatroy problems\n \
A) Aloe Vera\n B) Rosemary\n C) Licorice\n D) Eucalyptus\n E) Roseroot\n F) Mint\n ')

check_anwer(guess5, 'E')

guess6 = input('Althogh this plant has a pungent smell, it\'s medicinal properties are great ! This includes anti-bacterial properties, anti-inflammatory properties, if applied topically\n \
A) Eucalyptus\n B) Rosemary\n C) Roseroot\n D) Aloe Vera\n E) Licorice\n F) Mint\n') 

check_anwer(guess6, 'B') 

print(' Your resutls are in ! You have scored  ' +   str(score))
