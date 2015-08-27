import random
from termcolor import colored

correctness_needed = 75

d = {
"Demography":"the study of human populations, including their size, growth, density, and distribution, and statistics regarding birth, marriage, disease, and death",
"Migration":"a group of people that are moving together from one region or country to another",
"interaction":"the give-and-take action of two or more things that have an effect on each other and work together",
"fundamental":"relating to or affecting the underlying principles or structure of something",
"exploit":"to use or develop something in order to gain a benefit or advantage",
"pastoralism":"a way of life that depends on raising livestock and living on its milk and meat from goats, sheep, or cattle",
"emerge":"to appear out of or from behind something",
"exponentially":"rapidly becoming greater in size",
"green":"supporting or promoting the protection of the environment",
"ideologies":"a closely organized system of beliefs, values, and ideas forming the basis of a social, economic, or political philosophy or program",
"dissemination":"to distribute or spread something, especially information, widely, or become widespread",
"adaptation":"the process or state of changing to fit a new environment or different conditions or the resulting change",
"adopting":"to take up something such as a plan, idea, or practice and use or follow it",
"components":"forming part of a whole",
"novel":"new and different, often in an interesting, unusual or inventive way",
"governance":"the system or manner of government",
"processes":"a series of actions directed toward a specific aim or a series of natural occurrences that produce change or development",
"agrarian":"dominated by or relating to farming",
"mercantile":"used for trade or by merchants, or characteristic of merchants or trading",
"autocracies":"a government in which a person holds unlimited power",
"constitutional":"politics governed or regulated by a constitution",
"diplomacy":"the management of communication and relationships between nations",
"commercial(commerce)":"relating to the buying and selling of goods or services",
"capitalism":"an economic system based on the private ownership of the means of production and distribution of goods, characterized by a free competitive market and motivation by profit",
"socialism":"a political theory or system in which the means of production and distribution are controlled by the people and operated according to equity and fairness rather than market principles",
"associated":"connected with another person or event",
"household management":"the organizing and controlling of the affairs of a people who live together in a single home",
"coerced":"to make somebody do something against his or her will by using force or threats",
"institutions":"a large organization that is influential in the community",
"sustain":"to manage to withstand something and continue in spite of it",
"region":"a large land area that has geographic, political, or cultural characteristics that distinguish it from others, whether existing within one country or extending over several",
"diffusion":"the spread of tools, practices, or other features from one culture to the next",
"state formation":"the process by which country or nation develops or takes a particular shape",
"gender":"the sex of a person",
"kinship":"relationship by blood or marriage to another or others",
"racial":"existing or taking place between different races one of the groups into which the world's population can be divided on the basis of physical characteristics such as skin or hair color",
"ethnic":"relating to a person or to a large group of people who share a national, racial, linguistic, or religious heritage, whether or not they reside in their countries of origin",
"norms":"a standard pattern of behavior that is considered normal in a society",
"stratification":"formation into layers or groups such as caste or class",
"hierarchies":"an organization or group whose members are arranged in ranks",
"political economy":"the study of ways in which economics and government policies interact",
"human ecology":"the study of the relationships between human beings and their natural and social environments"
}

words = d.keys()
random.shuffle(words)
while len(d) > 0:
    for word in words:

        user_input = raw_input(colored('Define ', 'blue') + colored('"' + word + '": ', 'green'))

        user_input_list = user_input.lower().split(' ')

        answer_list = d[word].lower().split(' ')
        answer_word_count = len(answer_list)

        matching_words = []

        for user_word in user_input_list:
            if user_word in answer_list:
                answer_list.remove(user_word)
                matching_words.append(user_word)

        correctness = (float(len(matching_words)) / answer_word_count) * 100

        print "Matching words:", colored(' '.join(matching_words), 'green')
        print "Actual definition:", colored(d[word], 'green')
        if correctness < correctness_needed:
            color = 'red'
        else:
            color = 'green'
            d.pop(word, None)

        print "Correctness:", colored(str(correctness) + "%", color)
