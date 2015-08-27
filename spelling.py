import os
import random
from termcolor import colored

words = [
'sense',
'plenty',
'enemy',
'welcome',
'swept',
'edit',
'tennis',
'meant',
'health',
'breath',
'shelter',
'sweater',
'wealth',
'quest',
'feather',
'treasure',
'bedspread',
'chess',
'strengthen',
'shelf'
]

encouragements = [
'nice job!',
'good job!',
'well done!',
'correct!',
'you are awesome!'
]

incorrect_encouragements = [
'try again!',
'nope!',
'that is wrong',
'that is incorrect',
'sorry, that was incorrect',
'incorrect!'
]

word_correct = {}
for word in words:
    word_correct[word] = False

while False in word_correct.values():
    for word in word_correct.keys():
        if word_correct[word] == False:
                spelling = ""
                while len(spelling) == 0:
                    os.system("say '" + word + "'")
                    spelling = raw_input(colored("Spell the word: ", "blue"))
                if spelling == word:
                    encouragement = random.choice(encouragements)
                    os.system("say '{}'".format(encouragement.replace("'", "\\'")))

                    word_correct[word] = True
                else:
                    os.system("say 'incorrect!'")

os.system("say 'Good job! We are all done!'")
