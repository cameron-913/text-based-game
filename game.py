"""
Text Based Game
Y9 Design Class
By Cameron Samek
Teacher: Mr. Jugoon
"""

# Packages imported
# Sleep delays commands
from time import sleep
# Termcolor allows for coloured text in the terminal
from termcolor import colored
# Shuffle the order of lists
from random import shuffle

# ASCII Art text variables
adventure_mode_text = """
  __   ____  _  _  ____  __ _  ____  _  _  ____  ____    _  _   __  ____  ____              
 / _\ (    \/ )( \(  __)(  ( \(_  _)/ )( \(  _ \(  __)  ( \/ ) /  \(    \(  __)             
/    \ ) D (\ \/ / ) _) /    /  )(  ) \/ ( )   / ) _)   / \/ \(  O )) D ( ) _)    _  _  _   
\_/\_/(____/ \__/ (____)\_)__) (__) \____/(__\_)(____)  \_)(_/ \__/(____/(____)  (_)(_)(_)  
"""

learn_mode_text = """
 __    ____   __   ____  __ _    _  _   __  ____  ____ 
(  )  (  __) / _\ (  _ \(  ( \  ( \/ ) /  \(    \(  __)
/ (_/\ ) _) /    \ )   //    /  / \/ \(  O )) D ( ) _) 
\____/(____)\_/\_/(__\_)\_)__)  \_)(_/ \__/(____/(____)
"""

# Function to create typewriter/staggered text
def staggered(delay, phrase):
    for i in phrase:
        print(i, end='', flush=True)
        sleep(delay)
    print('')

# Start of teh adevnture part of the game
def adventureMode():
    staggered(0.002, adventure_mode_text)

    # Character selection part
    print('')
    print(f'Would you like to play as: \n a) {colored("Jabari", "blue")} \n b) {colored(f"his sister", "yellow")} \n c) {colored("his dad", "magenta")} ')
    print('')

    character_chosen = False
    chosen_character = None
    while not character_chosen:
        character = input('')
        print('')
        character = character.lower()

        # Player selects Jabari
        if character == 'a':
            character_chosen = True
            chosen_character = 'jabari'
            print('You are playing as Jabari.')

        # Player selects Jabari's sister
        elif character == 'b':
            character_chosen = True
            chosen_character = 'jabari_sister'
            print("You are playing as Jabari's sister.")

        # Player selects Jabari's dad
        elif character == 'c':
            character_chosen = True
            chosen_character = 'jabari_dad'
            print("You are playing as Jabari's dad.")

        # Player makes an invalid selection and it loops back
        else:
            print(colored('Sorry, that is not a valid option. Try again.', 'red'))
            print('')

        # Jabari adevnture starts here
        if chosen_character == 'jabari':
            print('"Jabari! Wake up!", calls your dad.')
            staggered(0.1, 'You are very tired though...')
            print('')
            print(f'What do you do: \n a) {colored("get up", "blue")} \n b) {colored("go back to sleep", "yellow")}')

            # User given a choice of wether they want to sleep in or not
            sleep_choice_chosen = False
            while not sleep_choice_chosen:
                print('')
                sleep_choice = input('')
                print('')
                sleep_choice = sleep_choice.lower()

                # User chooses to get up
                if sleep_choice == 'a':
                    sleep_choice_chosen = True
                    print('You go downstairs.')
                    print('"Good morning Jabari." says your dad.')
                    print('"Goodmorning" you say back.')

                    sleep(4)
                    print('')
                    print(f'"I am making some pancakes. Do you want any?" asks your dad. \n a) {colored("yes", "blue")} \n b) {colored("no", "yellow")}')
                    print('')

                    # User choice on wether or not they want to have pancakes
                    eat_choice = False
                    while not eat_choice:
                        print('')
                        eat_pancakes = input('')
                        print('')
                        eat_pancakes = eat_pancakes.lower()
                        
                        # User chooses to have pancakes
                        if eat_pancakes == 'a':
                            eat_choice = True
                            print('The pancakes were delicious. You ate so many you felt like throwing up.')
                            print('"Dad, what are we going to do today?" you asked.')
                            print('"I don\'t know. You choose with your sister."')
                            print('"AMUSEMENT PARK. AMUSEMENT PARK." yells your sister.')

                            print('')
                            print(f'Choose where you are going to go: \n a) {colored("amusement park", "blue")} \n b) {colored("museum", "yellow")} \n c) {colored("aquarium", "magenta")} \n d) {colored("pool", "blue")}')
                            
                            # User chooses what activity they want to do
                            activity_chosen = False
                            while not activity_chosen:
                                print('')
                                activity = input('')
                                print('')
                                activity = activity.lower()

                                # Chooses amusement park activty
                                if activity == 'a':
                                    activity_chosen = True
                                    print('You are going to the amusement park.')
                                    print('"I\'m going to do that one." you said, pointing at the largest, scariest ride.')
                                    print(f'Your dad asks if you are sure. That ride is very scary. \n a) {colored("yes", "green")} \n b) {colored("no", "red")}')

                                    # Asks user if they want to do the big scary rollercoaster
                                    ride_confirmtion = False
                                    while not ride_confirmtion:
                                        print('')
                                        confirmed_ride = input('')
                                        print('')
                                        confirmed_ride = confirmed_ride.lower()

                                        # User chooses to do roller coaster
                                        if confirmed_ride == 'a':
                                            ride_confirmtion = True
                                            print('You go into the line of the ride. You are very nervous.')
                                            print(f'What should you do when you are nervous? \n a) {colored("Take deep, long breaths.", "blue")} \n b) {colored("Tell yourself to stop being a loser.", "yellow")}')

                                            # Question on what to do when you are nervous
                                            nervous_correct = False
                                            while not nervous_correct:
                                                print('')
                                                nervous_answer = input('')
                                                print('')
                                                nervous_answer = nervous_answer.lower()

                                                # User answered correctly
                                                if nervous_answer == 'a':
                                                    nervous_correct = True
                                                    print('That is a great strategy to deal with your nerves!')
                                                    sleep(1)
                                                    print('')
                                                    
                                                    print('The roller coaster goes up')
                                                    staggered(0.2, 'and up...')
                                                    staggered(0.2, 'and up...')
                                                    staggered(0.2, 'and up...')
                                                    print('Then, you are at the top facing down now, you can see the huge sharp drop below you.')

                                                    # Adventure ends, game ends
                                                    print('')
                                                    print('The cart begins to pick up speed and it is an awesome ride.')
                                                    print('You are very happy you took the risk.')
                                                
                                                # User answers incorrectly on what to do when nervous
                                                else:
                                                    print(colored('Sorry, that is incorrect. Try again.', 'red'))

                                        # User chooses not to do the ride
                                        elif confirmed_ride == 'b':
                                            ride_confirmtion = True
                                            print('It is okay. Sometimes people are nervous to do things.')
                                            print(f'What should you do when you are nervous? \n a) {colored("Take deep, long breaths.", "blue")} \n b) {colored("Tell yourself to stop being a loser.", "yellow")}')

                                            # User is asked the same nervousness question
                                            nervous_correct = False
                                            while not nervous_correct:
                                                print('')
                                                nervous_answer = input('')
                                                print('')
                                                nervous_answer = nervous_answer.lower()

                                                if nervous_answer == 'a':
                                                    nervous_correct = True
                                                    print('That is a great strategy to deal with your nerves!')
                                                
                                                else:
                                                    print(colored('Sorry, that is incorrect. Try again.', 'red'))

                                            print('You can try it again tomorrow.')
                                            print('Nonetheless, you still had great fun at the amusement park!')

                                        else:
                                            print(colored('Sorry, that is not a valid option. Try again.', 'red'))
                                            print('')
                                
                                # User chooses to go to the museum
                                elif activity == 'b':
                                    activity_chosen = True
                                    # Quick part as this is not the main event
                                    print('You are going to the museum.')
                                    print('You get there and buy the tickets. It was a lot more boring than you expected.')
                                    print('You saw some dinosaur skeletons.')
                                    print('After a couple minutes you were bored and tired of standing around.')
                                    print('You would rather do your homework.')

                                # User chooses to go to the aquarium
                                elif activity == 'c':
                                    activity_chosen = True
                                    # Quick part as this is not the main event
                                    print('You are going to the aquarium.')
                                    print('You get there and buy the tickets. It was a lot more boring than you expected.')
                                    print('You saw some sharks.')
                                    print('After a couple minutes you were bored and tired of standing around.')
                                    print('You would rather do your homework.')

                                # User chooses to go to the pool
                                elif activity == 'd':
                                    activity_chosen = True
                                    print('You are going to the pool.')
                                    sleep(1)
                                    print('At the pool you see some kids jumping off a very tall diving board.')
                                    print('You point at the diving board and say, "I\'m going to jump off that tall tall diving board!"')
                                    print(f'Your dad asks if you are sure. That jump is very scary. \n a) {colored("yes", "green")} \n b) {colored("no", "red")}')

                                    # User is asked wether or not they want to go on the diving board
                                    jump_confirmtion = False
                                    while not jump_confirmtion:
                                        print('')
                                        confirmed_jump = input('')
                                        print('')
                                        confirmed_jump = confirmed_jump.lower()

                                        # User says yes to going on the diving board
                                        if confirmed_jump == 'a':
                                            jump_confirmtion = True
                                            print('You go into the line for the diving board. You are very nervous.')
                                            print(f'What should you do when you are nervous? \n a) {colored("Take deep, long breaths.", "blue")} \n b) {colored("Tell yourself to stop being a loser.", "yellow")}')
                                            
                                            # Asked a question about what to do when nervous
                                            nervous_correct = False
                                            while not nervous_correct:
                                                print('')
                                                nervous_answer = input('')
                                                print('')
                                                nervous_answer = nervous_answer.lower()

                                                # User answers question correctly
                                                if nervous_answer == 'a':
                                                    nervous_correct = True
                                                    print('That is a great strategy to deal with your nerves!')
                                                    sleep(1)
                                                    print('')
                                                    
                                                    print('The line gets shorter and shorter until it is your turn.')
                                                    input('What trick do you want to do when you jump: ')

                                                    print('You jump and go down')
                                                    staggered(0.2, 'and down...')
                                                    staggered(0.2, 'and down...')
                                                    print(""" _______  _______  _        _______  _______           _ 
(  ____ \(  ____ )( \      (  ___  )(  ____ \|\     /|( )
| (    \/| (    )|| (      | (   ) || (    \/| )   ( || |
| (_____ | (____)|| |      | (___) || (_____ | (___) || |
(_____  )|  _____)| |      |  ___  |(_____  )|  ___  || |
      ) || (      | |      | (   ) |      ) || (   ) |(_)
/\____) || )      | (____/\| )   ( |/\____) || )   ( | _ 
\_______)|/       (_______/|/     \|\_______)|/     \|(_)""")

                                                    print('')
                                                    print('It was so fun jumping off the diving board.')
                                                    print('You are very happy you took the risk.')
                                                
                                                # User answers question incorrectly
                                                else:
                                                    print(colored('Sorry, that is incorrect. Try again.', 'red'))

                                        # User says they don't want to do the diving board
                                        elif confirmed_jump == 'b':
                                            jump_confirmtion = True
                                            print('It is okay. Sometimes people are nervous to do things.')
                                            print(f'What should you do when you are nervous? \n a) {colored("Take deep, long breaths.", "blue")} \n b) {colored("Tell yourself to stop being a loser.", "yellow")}')

                                            # Asked same question about what to do when nervous
                                            nervous_correct = False
                                            while not nervous_correct:
                                                print('')
                                                nervous_answer = input('')
                                                print('')
                                                nervous_answer = nervous_answer.lower()

                                                # Correct answers
                                                if nervous_answer == 'a':
                                                    nervous_correct = True
                                                    print('That is a great strategy to deal with your nerves!')
                                                
                                                # Wrong answer
                                                else:
                                                    print(colored('Sorry, that is incorrect. Try again.', 'red'))

                                            print('You can try it again tomorrow.')
                                            print('Nonetheless, you still had great fun at the pool!')
                                            print('You swam in the nice refreshing water on a hot day.')
                                            staggered(0.2, 'except...')
                                            print('When swimming, all those pancakes you ate didn\'t feel so good anymore.')
                                            staggered(0.2, 'and you puked...')

                                        else:
                                            print(colored('Sorry, that is not a valid option. Try again.', 'red'))
                                            print('')
                                else:
                                    print(colored('Sorry, that is not a valid option. Try again.', 'red'))
                                    print('')

                        # Exact same things happen here as above except the user doesn't puke at the end
                        elif eat_pancakes == 'b':
                            eat_choice = True
                            print('You opted for a bowl of cereal instead of the pancakes.')
                            print('"PANCAKES! I love pancakes. YAY!" screamed your sister.')
                            print('"Dad, what are we going to do today?" you asked.')
                            print('"I don\'t know. You choose with your sister."')
                            print('"AMUSEMENT PARK. AMUSEMENT PARK." yells your sister.')

                            print('')
                            print(f'Choose where you are going to go: \n a) {colored("amusement park", "blue")} \n b) {colored("museum", "yellow")} \n c) {colored("aquarium", "magenta")} \n d) {colored("pool", "blue")}')

                            activity_chosen = False
                            while not activity_chosen:
                                print('')
                                activity = input('')
                                print('')
                                activity = activity.lower()

                                if activity == 'a':
                                    activity_chosen = True
                                    print('You are going to the amusement park.')
                                    print('"I\'m going to do that one." you said, pointing at the largest, scariest ride.')
                                    print(f'Your dad asks if you are sure. That ride is very scary. \n a) {colored("yes", "green")} \n b) {colored("no", "red")}')

                                    ride_confirmtion = False
                                    while not ride_confirmtion:
                                        print('')
                                        confirmed_ride = input('')
                                        print('')
                                        confirmed_ride = confirmed_ride.lower()

                                        if confirmed_ride == 'a':
                                            ride_confirmtion = True
                                            print('You go into the line of the ride. You are very nervous.')
                                            print(f'What should you do when you are nervous? \n a) {colored("Take deep, long breaths.", "blue")} \n b) {colored("Tell yourself to stop being a loser.", "yellow")}')

                                            nervous_correct = False
                                            while not nervous_correct:
                                                print('')
                                                nervous_answer = input('')
                                                print('')
                                                nervous_answer = nervous_answer.lower()

                                                if nervous_answer == 'a':
                                                    nervous_correct = True
                                                    print('That is a great strategy to deal with your nerves!')
                                                    sleep(1)
                                                    print('')
                                                    
                                                    print('The roller coaster goes up')
                                                    staggered(0.2, 'and up...')
                                                    staggered(0.2, 'and up...')
                                                    staggered(0.2, 'and up...')
                                                    print('Then, you are at the top facing down now, you can see the huge sharp drop below you.')

                                                    print('')
                                                    print('The cart begins to pick up speed and it is an awesome ride.')
                                                    print('You are very happy you took the risk.')
                                                
                                                else:
                                                    print(colored('Sorry, that is incorrect. Try again.', 'red'))

                                        elif confirmed_ride == 'b':
                                            ride_confirmtion = True
                                            print('It is okay. Sometimes people are nervous to do things.')
                                            print(f'What should you do when you are nervous? \n a) {colored("Take deep, long breaths.", "blue")} \n b) {colored("Tell yourself to stop being a loser.", "yellow")}')

                                            nervous_correct = False
                                            while not nervous_correct:
                                                print('')
                                                nervous_answer = input('')
                                                print('')
                                                nervous_answer = nervous_answer.lower()

                                                if nervous_answer == 'a':
                                                    nervous_correct = True
                                                    print('That is a great strategy to deal with your nerves!')
                                                
                                                else:
                                                    print(colored('Sorry, that is incorrect. Try again.', 'red'))

                                            print('You can try it again tomorrow.')
                                            print('Nonetheless, you still had great fun at the amusement park!')

                                        else:
                                            print(colored('Sorry, that is not a valid option. Try again.', 'red'))
                                            print('')

                                elif activity == 'b':
                                    activity_chosen = True
                                    print('You are going to the museum.')
                                    print('You get there and buy the tickets. It was a lot more boring than you expected.')
                                    print('You saw some dinosaur skeletons.')
                                    print('After a couple minutes you were bored and tired of standing around.')
                                    print('You would rather do your homework.')

                                    sleep(1)
                                    print('')
                                    staggered(0.2, 'and that is what you do...')
                                    sleep(1)
                                    learnMode()

                                elif activity == 'c':
                                    activity_chosen = True
                                    print('You are going to the aquarium.')
                                    print('You get there and buy the tickets. It was a lot more boring than you expected.')
                                    print('You saw some sharks.')
                                    print('After a couple minutes you were bored and tired of standing around.')
                                    print('You would rather do your homework.')

                                    sleep(1)
                                    print('')
                                    staggered(0.2, 'and that is what you do...')
                                    sleep(1)
                                    learnMode()

                                elif activity == 'd':
                                    activity_chosen = True
                                    print('You are going to the pool.')
                                    sleep(1)
                                    print('At the pool you see some kids jumping off a very tall diving board.')
                                    print('You point at the diving board and say, "I\'m going to jump off that tall tall diving board!"')
                                    print(f'Your dad asks if you are sure. That jump is very scary. \n a) {colored("yes", "green")} \n b) {colored("no", "red")}')

                                    jump_confirmtion = False
                                    while not jump_confirmtion:
                                        print('')
                                        confirmed_jump = input('')
                                        print('')
                                        confirmed_jump = confirmed_jump.lower()

                                        if confirmed_jump == 'a':
                                            jump_confirmtion = True
                                            print('You go into the line for the diving board. You are very nervous.')
                                            print(f'What should you do when you are nervous? \n a) {colored("Take deep, long breaths.", "blue")} \n b) {colored("Tell yourself to stop being a loser.", "yellow")}')

                                            nervous_correct = False
                                            while not nervous_correct:
                                                print('')
                                                nervous_answer = input('')
                                                print('')
                                                nervous_answer = nervous_answer.lower()

                                                if nervous_answer == 'a':
                                                    nervous_correct = True
                                                    print('That is a great strategy to deal with your nerves!')
                                                    sleep(1)
                                                    print('')
                                                    
                                                    print('The line gets shorter and shorter until it is your turn.')
                                                    input('What trick do you want to do when you jump: ')

                                                    print('You jump and go down')
                                                    staggered(0.2, 'and down...')
                                                    staggered(0.2, 'and down...')
                                                    print(""" _______  _______  _        _______  _______           _ 
(  ____ \(  ____ )( \      (  ___  )(  ____ \|\     /|( )
| (    \/| (    )|| (      | (   ) || (    \/| )   ( || |
| (_____ | (____)|| |      | (___) || (_____ | (___) || |
(_____  )|  _____)| |      |  ___  |(_____  )|  ___  || |
      ) || (      | |      | (   ) |      ) || (   ) |(_)
/\____) || )      | (____/\| )   ( |/\____) || )   ( | _ 
\_______)|/       (_______/|/     \|\_______)|/     \|(_)""")

                                                    print('')
                                                    print('It was so fun jumping off the diving board.')
                                                    print('You are very happy you took the risk.')
                                                
                                                else:
                                                    print(colored('Sorry, that is incorrect. Try again.', 'red'))

                                        elif confirmed_jump == 'b':
                                            jump_confirmtion = True
                                            print('It is okay. Sometimes people are nervous to do things.')
                                            print(f'What should you do when you are nervous? \n a) {colored("Take deep, long breaths.", "blue")} \n b) {colored("Tell yourself to stop being a loser.", "yellow")}')

                                            nervous_correct = False
                                            while not nervous_correct:
                                                print('')
                                                nervous_answer = input('')
                                                print('')
                                                nervous_answer = nervous_answer.lower()

                                                if nervous_answer == 'a':
                                                    nervous_correct = True
                                                    print('That is a great strategy to deal with your nerves!')
                                                
                                                else:
                                                    print(colored('Sorry, that is incorrect. Try again.', 'red'))

                                            print('You can try it again tomorrow.')
                                            print('Nonetheless, you still had great fun at the pool!')
                                            print('You swam in the nice refreshing water on a hot day.')

                        else:
                            print(colored('Sorry, that is not a valid option. Try again.', 'red'))
                            print('')

                # The user chooses to sleep in
                elif sleep_choice == 'b':
                    sleep_choice_chosen = True
                    print('You get another 10 minutes of beautiful, sweet sleep, until your dad comes in.')
                    print('"Jabari, this is the 3rd time you have ignored me. You know what? We are not going to have fun today. You are going to do your homework. Go read that book Jabari Jumps and answer the questions on it."')
                    print('You plead with your dad but it is no use. Your saturday is ruined.')
                    print('Your dad goes to the pool with your sister.')

                    sleep(1)
                    staggered(0.2, 'now you mustt do your homework...')
                    # Brings the user to the learn mode to do "homework"
                    learnMode()

                # User enters an invalid option
                else:
                    print(colored('Sorry, that is not a valid option. Try again.', 'red'))
                    print('')
        
        # A user chooses to play as Jabari's dad or sister here which is not done yet
        else:
            print('Sorry you can\'t play as Jabari\'s dad or sister right now.')

# Questions for the learn section here
# List of questions with dicts inside
# Each has a question key
# An answer key which has a list of answers which are dicts
# Which have 2 keys, the word/text for that option and a boolean key saying wether that option is correct or wrong
# Each of the dicts inside of the questions list which have topics so they can be sorted into seperate learning sections
questions = [
    {   
        'question': 'What was the first thing Jabari told his dad when they got to the pool?',
        'answers': [
            {'answer': 'a) ' + colored('The pancakes you made this morning were delicious.', 'blue'), 'correct': False},
            {'answer': 'b) ' + colored('I love you.', 'yellow'), 'correct': False},
            {'answer': 'c) ' + colored('I\'m jumping off the diving board today.', 'magenta'), 'correct': True},
            {'answer': 'd) ' + colored('I love to swim.', 'blue'), 'correct': False}
        ],
        'topic': 'plot'
    },
    {
        'question': 'Why was today the day when Jabari was going to jump off the diving board?',
        'answers': [
            {'answer': 'a) ' + colored('He just felt like today was the day.', 'blue'), 'correct': False},
            {'answer': 'b) ' + colored('He had just finished his swimming lessons and had passed his swim test.', 'yellow'), 'correct': True},
            {'answer': 'c) ' + colored('He was finally old enough to jump off.', 'magenta'), 'correct': False},
        ],
        'topic': 'plot'
    },
    {
        'question': 'Jabari said he was not at all scared to jump. Why was that?',
        'answers': [
            {'answer': 'a) ' + colored('He was a great jumper.', 'blue'), 'correct': True},
            {'answer': 'b) ' + colored('His dad and sister were there supporting him.', 'yellow'), 'correct': False},
            {'answer': 'c) ' + colored('He had jumped off the diving board before.', 'magenta'), 'correct': False},
        ],
        'topic': 'plot'
    },
    {
        'question': 'Before Jabari was about to climb his ladder he forgot something. What did he forget?',
        'answers': [
            {'answer': 'a) ' + colored('He forgot to do his stretches.', 'blue'), 'correct': True},
            {'answer': 'b) ' + colored('He forgot to hug his dad.', 'yellow'), 'correct': False},
            {'answer': 'c) ' + colored('He forgot to bring his goggles for the jump.', 'magenta'), 'correct': False},
            {'answer': 'd) ' + colored('He forgot to get a snack.', 'blue'), 'correct': False},
        ],
        'topic': 'plot'
    },
    {
        'question': 'True or false: Jabari was scared/nervous to jump off the diving board.',
        'answers': [
            {'answer': 'a) ' + colored('True', 'green'), 'correct': True},
            {'answer': 'b) ' + colored('False', 'red'), 'correct': False},
        ],
        'topic': 'plot'
    },
    {
        'question': 'True or false: Jabari\'s dad said that he never feels scared. He told Jabari to just jump already.',
        'answers': [
            {'answer': 'a) ' + colored('True', 'green'), 'correct': False},
            {'answer': 'b) ' + colored('False', 'red'), 'correct': True},
        ],
        'topic': 'plot'
    },
    {
        'question': 'Does Jabari love surprises?',
        'answers': [
            {'answer': 'a) ' + colored('No, he hates them!', 'blue'), 'correct': False},
            {'answer': 'b) ' + colored('Yes, he loves them!', 'yellow'), 'correct': True},
            {'answer': 'c) ' + colored('Sometimes he likes them.', 'magenta'), 'correct': False},
            {'answer': 'd) ' + colored('Usually, he does not like surprises.', 'blue'), 'correct': False}
        ],
        'topic': 'plot'
    },
    {
        'question': 'Does Jabari eventually jump off the diving board?',
        'answers': [
            {'answer': 'a) ' + colored('Yes, he jumps off!', 'blue'), 'correct': True},
            {'answer': 'b) ' + colored('No, he does not jump off.', 'yellow'), 'correct': False},
        ],
        'topic': 'plot'
    },
    {
        'question': 'Do you think this book wants you to: ',
        'answers': [
            {'answer': 'a) ' + colored('Eat more pancakes', 'blue'), 'correct': False},
            {'answer': 'b) ' + colored('Tackle your fears', 'yellow'), 'correct': True},
            {'answer': 'c) ' + colored('Jabari has a nice dad', 'magenta'), 'correct': False},
        ],
        'topic': 'meaning'
    },
    {
        'question': 'How does Jabari overcome his fear? What strategies cna you do to overcome your fears?',
        'answers': [
            {'answer': 'a) ' + colored('He let his dad help him.', 'blue'), 'correct': False},
            {'answer': 'b) ' + colored('He forced himself to jump off even though he did not want to.', 'yellow'), 'correct': False},
            {'answer': 'c) ' + colored('He took serveral deep breaths.', 'magenta'), 'correct': True}
        ],
        'topic': 'meaning'
    },
    {
        'question': 'Which of these goals is not part of the UN\'s list of Sustainable Development Goals?',
        'answers': [
            {'answer': 'a) ' + colored('Clean water and sanitation.', 'blue'), 'correct': False},
            {'answer': 'b) ' + colored('End poverty in all its forms.', 'yellow'), 'correct': False},
            {'answer': 'c) ' + colored('Gender equality', 'magenta'), 'correct': False},
            {'answer': 'd) ' + colored('Ensure that all people have access to tasty snacks.', 'blue'), 'correct': True}
        ],
        'topic': 'meaning'
    },
    {
        'question': 'Which UNSDG\'S connects most to the story Jabari Jumps? (this is a tricky question)',
        'answers': [
            {'answer': 'a) ' + colored('Clean water and sanitation.', 'blue'), 'correct': True},
            {'answer': 'b) ' + colored('End poverty in all its forms.', 'yellow'), 'correct': False},
            {'answer': 'c) ' + colored('Gender equality', 'magenta'), 'correct': False},
            {'answer': 'd) ' + colored('Climate action', 'blue'), 'correct': False}
        ],
        'topic': 'meaning'
    }
]

# Function for displaying questions and checking if right or wrong
def questionLogic(list):
    streak = 0
    total = 0
    score = 0

    for q in list:
        answer_correct = False
        while not answer_correct:
            total += 1
            print(f'{score + 1}. {q["question"]}')
            for a in q['answers']:
                print(' ' + a['answer'])
                if a['correct'] == True:
                    correct_answer = a['answer'][0]
            print('')

            answer = input('')
            print('')
            answer = answer.lower()

            if answer == correct_answer:
                answer_correct = True
                print(colored('Great job! That is correct.', 'green'))
                score += 1 
                streak += 1
                print('')
            else:
                print(colored('Nice try. Unfortunately, that is incorrect.', 'red'))
                print('')
                streak = 0
        
        print(f'You have a streak of {streak}.')
        print(f'You have a mark of {score}/{total}')
        print('')

    print('You are going back to the main page now.')
    sleep(1)
    learnMode()

# Function where the user is taken to if they choose to learn the plot
# They will see the intro ASCII Art
# This function will then filter through the questions list above taking out all the dicts that have a topic of plot
# Then it combines all those into a list
# It then shuffles the list so that questions are in semi-random order
# Then calls logic function above with that shuffled list as a parameter
def learnPlot():
    learning_plot_text = """
     __    ____   __   ____  __ _  __  __ _   ___    ____  _  _  ____    ____  __     __  ____  _   
(  )  (  __) / _\ (  _ \(  ( \(  )(  ( \ / __)  (_  _)/ )( \(  __)  (  _ \(  )   /  \(_  _)/ \  
/ (_/\ ) _) /    \ )   //    / )( /    /( (_ \    )(  ) __ ( ) _)    ) __// (_/\(  O ) )(  \_/  
\____/(____)\_/\_/(__\_)\_)__)(__)\_)__) \___/   (__) \_)(_/(____)  (__)  \____/ \__/ (__) (_)
    """
    staggered(0.002, learning_plot_text)

    plot_questions = []
    question = 0

    for q in questions:
        if q['topic'] == 'plot':
            plot_questions.append(questions[question])
        question += 1

    shuffle(plot_questions)
    questionLogic(plot_questions)

def learnMeaning():
    learning_meaning_text = """
     __    ____   __   ____  __ _  __  __ _   ___    ____  _  _  ____    _  _  ____   __   __ _  __  __ _   ___  _   
(  )  (  __) / _\ (  _ \(  ( \(  )(  ( \ / __)  (_  _)/ )( \(  __)  ( \/ )(  __) / _\ (  ( \(  )(  ( \ / __)/ \  
/ (_/\ ) _) /    \ )   //    / )( /    /( (_ \    )(  ) __ ( ) _)   / \/ \ ) _) /    \/    / )( /    /( (_ \\_/  
\____/(____)\_/\_/(__\_)\_)__)(__)\_)__) \___/   (__) \_)(_/(____)  \_)(_/(____)\_/\_/\_)__)(__)\_)__) \___/(_) 
    """

    staggered(0.002, learning_meaning_text)

    meaning_questions = []
    question = 0

    for q in questions:
        if q['topic'] == 'meaning':
            meaning_questions.append(questions[question])
        question += 1

    shuffle(meaning_questions)
    questionLogic(meaning_questions)

# Does same thing as the function above except it filters all of the questions that have a topic of meaning
def learnOwnQuestion():
    print('Sorry, this topic has not been added yet...')

def makeQuestion():
    print('Sorry, this topic has not been added yet...')

def learnMode():
    print('')
    staggered(0.002, learn_mode_text)
    print('')
    print(f'What would you like to learn: \n a) {colored("The plot of the story", "blue")} \n b) {colored("The hidden meanings", "yellow")} \n c) {colored("Study your own questions", "magenta")} \n d) {colored("Make your own questions", "blue")}')
    print('')

    learn_topic_chosen = False
    while not learn_topic_chosen:
        learn_topic = input('')
        print('')
        learn_topic = learn_topic.lower()

        if learn_topic == 'a':
            learn_topic_chosen = True
            learnPlot()
        
        elif learn_topic == 'b':
            learn_topic_chosen = True
            learnMeaning()

        elif learn_topic == 'c':
            learn_topic_chosen = True
            learnOwnQuestion()
        
        elif learn_topic == 'd':
            learn_topic_chosen = True
            makeQuestion()

        else:
            print(colored('Sorry, that is incorrect. Try again.', 'red'))
            print('')

# Start of game

# This for loop creates some buffer from the top of the terminal to provide more legibility
for i in range(4):
    print('')
    sleep(0.5)

# User gets a choice as to wether they want to play the learn mode or the adventure mode
print('')
print(f'Would you like to play: \n a) {colored("Adventure", "blue")} \n b) {colored("Learn", "yellow")}')
print('To select an option type the letter to the corresponding option that you want.')
print('')

game_mode_chosen = False

while not game_mode_chosen:
    game_mode = input('')
    game_mode = game_mode.lower()

    # User selects adventure mode
    if game_mode == 'a': 
        game_mode_chosen = True
        adventureMode()

    # User selects learn mode
    elif game_mode == 'b': 
        game_mode_chosen = True
        learnMode() 

    # User selects and invalid option
    else: 
        print(colored('Sorry, that is not a valid option. Try again.', 'red'))
        print('')
