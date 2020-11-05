"""
    DocString:
    
    A) Introduction:
    The idea of the game is to help a lost camper in forest to reach civilisation by moving overcoming troubles in forest
    
    Round 1: Decide whether or not to approach the bridge.
    Round 2: Cross the water bridge with help of dryad
    Round 3: choose the path that leads to the civilisation and reach nearby town
    
    B) Known Bugs and/or Errors:
    None.
    
"""
""

from sys import exit
import random

def start():
    print("""
         You get stuck in a forest and need to find your way back to civilisation
         Infront of you there are 2 paths one leads to civilisation and one leads to beginning of game 
         """)
    input("<Press enter to continue>\n")
    starting_path()

def starting_path():
    print("""
    As the Survivor  what would you like to do?
    1) Take path left
    2) Stay and find the Door for journey".
    3) Take Right
    """)
    
    choice = input(">  \n")

    if "1" in choice or "approach" in choice or "left" in choice:
        print("\nYou took the left path !\n")
        input("<Press enter to continue>\n")
        Left_path()
    
    elif "2" in choice or "rest" in choice or "later" in choice:
        print("""\nSince you want to find food, what would you like to do?.""")
        input("<Press enter to continue>\n")
        starting_path()
    
    elif "3" in choice or "right" in choice:
        print("\nYou fell into a water stream!")
        input("<Press enter to continue>\n")
        starting_path()
    
    else:
        print("Invalid command. Please try again.")
        input("<Press enter to continue>\n")
        starting_path()


def Left_path():
    print("""
As you're about to start the journeyto escape the forest, a dryad appears in front of you 
and asks:
              
              "Who are you poor soul and what are you doing in my forest all by yourself ?" 
        
In this, you must answer the question truthfully.
          """)
    
    question_list = ['What... is your name?',
                     'What... is your goal?',
                     'where... do you wanna go?']
                     
    questions = 3
    
    while questions > 0:
        question = random.choice(question_list)
        input("<Press enter for your question>\n")
        print(question)
        print(" ")
        
        if question == question_list[0]:
            print("You can input anything and you're ok.")
            name = input("Your name: \n")
            print(f"DRYAD: Nice to meet you {name}!")
            questions -=1
            
        elif question == question_list[1]:
            print("1) I am trying to get out of forest")
            print("2) I am trying to destroy forest.")
            print("3) I dont know.")
            
            quest = input("> \n")
            
            if quest == '1':
                print("Don't worry human i can show you the way to civilisation crosses a water bridge\n")
                questions -=1
            
            else: 
                print("You're unworthy to stay here throws you to your death by a wildbeast")
                fail()
                
        
        elif question == question_list[2]:
            print("1) I wan to go back to city")
            print("2) I want to go back to nearby town")
            print("3) I forgot.")
            
            quest = input("> \n")
            

            if quest == '1':
                print("Don't worry human you will get back to your home soon\n")
                questions -=1
            
            else: 
                print("Don't worry human you will find people soon\n")
                questions -=1

       
     
    print("You made it Halfway to civilisation!\n")
    input("<Press enter to continue>\n")
    further_path()

def further_path():
    print("""
You are across the bridge and on your way to the civilisation when there are
\two paths infront of you.
""")
    print("What do you do?")
    print("1) take Left")
    print("2) Take right")
    
    further = input("> \n")
    
    if '1' in further or 'attack' in further or 'sword' in further:
        print("You found a small road in forest with tire marks.")
        print("You found a vehicle of forest official with him in it.\n")
        print('You reached back to nearby town and found your camping group')
        input("<Press enter to continue>\n")
        grail()
        
    
    elif '2' in further or 'run' in further:
        print('You end up walking into forest fires and dies')
        fail()


def grail():
    print("""
You have completed your quest for the Civilisation and found your camping group! Great job!
          """)
    input("<Press enter to exit, you champion!>\n")
    
    
def fail():
    print('\nYou have failed in your quest for the Civilisation.')
    input('<Game Over>')
    

start()


