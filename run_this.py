"""I think I need a shabang here or something
but I forget what's up with that."""


def start():
    user_input = input("Enter your favorie number: ")
    if user_input == '2':
        valid_answer = False
        while valid_answer == False:
            answer = input("Are you my father? ")
            if answer == 'yes':
                print("Luke, I am your father!")
                valid_answer = True
            elif answer == 'no':
                print("Oh, well that\'s my dad\'s favorite number too.")
                valid_answer = True
            else:
                print("Please enter yes or no")
    else:
        print("Lame. Goodbye.")
        print("alright, Ill give you one more chance.")
        start()
start()