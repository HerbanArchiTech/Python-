from random import randrange
from random import choice
import string 
from time import sleep
from sys import exit


#this will is just a rudimentary password picker with the with Python theme

data_Structures = ['Linked Lists' ,'Dictinaries', 'Lists' , 'Tuples',
        'Sets', ]

python_frameworks = ['Django', 'Flask', 'Web2Py ' 'Pyramid', 'Dash']

control_Structures = ['conditionals', 'statements', 'loops', 'functions', 'exception handling' ]

numbers = randrange(1,100)

#sCharacters =punctuation + choice


special_char = [choice(string.punctuation)]

python_frameworksRan = choice(python_frameworks)

control_StructuresrRAN = choice(control_Structures)

print("This is the password chooser it will offer you a passwowrd if you can\'t think of one ")

def threeMoreSec():
    
    sleep(1)
    threeSecs = sleep(1)*3

    
    
while True:
    special_char = choice(string.punctuation)

    python_frameworksRan = choice(python_frameworks)

    control_StructuresrRAN = choice(control_Structures)   

    password = special_char + str(numbers) + control_StructuresrRAN

    print('Password generating.....\n')
    threeMoreSec
    print('Your password created is \n:',password)
    


    reply = input('Do you want to create more passwords ? : (y/n)\n')

    if(reply =='n'):
        break
        exit
