#!/usr/bin/env python

if __name__ == "__main__":
    user_input = input("Enter your favorie number: ")
    if user_input == '2':
        # hmmm, I'm not sure what's up with this valid_answer variable. Do you ever use it for anything?
        valid_answer = False
        while valid_answer == False:
            answer = input("Are you my father?")
            if answer == 'yes':
                print("Luke, I am your father!")
                valid_answer = True
            elif answer == 'no':
                print("Oh, well that\'s my dad\'s favorite number too.")
                valid_answer = True
            else:
                print("Please enter yes or no")
    else:
        print("You are not my father.")
    
