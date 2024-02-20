import enchant
import random

def get_starter_word():
    # Naively choosing from list of 4 letter words
    starter_words = ["ball", "fail", "take", "tail", "cute", "damn", 
                    "ease", "goat", "heal", "icon", "just", "kite",
                    "loot", "mosh", "none", "open", "pass", "quit",
                    "robe", "stow", "ugly", "vows", "walk", "xray",
                    "yams", "zero"]   

    return starter_words[random.randrange(len(starter_words))]

def get_users_word():
    
    return input("Enter word:")

def is_dictionary_word(word):
    # Return true if the word is in the dictionary. Falser otherwise.
    d = enchant.Dict("en_US")    
    return d.check(word)

def display_intro_info(word):

    intro_info = "Welcome to Word Dodgeball! The game is simple. \n Take the original word," + \
    "swap one of its letters to create a new word and repeat. Do this is as many times as you can. \n" + \
    "When you run out of words, type 'forfeit' and I will share your score. Good luck! \n" + \
    "The start word is {}".format(word)

    print(intro_info)

def display_score(score):

    score_info = "Your score is {}. \n" + \
    "I am not sure if that is good or bad, but I am sure you tried your best :)"
    print(score_info)


def main():

    # Starter variables
    score = 0
    seen_words = set()
    new_word = ""
    
    # Generate a random word
    starter_word = get_starter_word()
    seen_words.add(starter_word)
    
    # Display introduction information
    display_intro_info(starter_word)
    # Ask user for new word
    new_word = get_users_word()
    
    # While new_word does not exist or has already been seen, keep asking for new word
    # If the new word is "forfeit" then exit and output score
    while new_word != "forfeit":
        
        if new_word in seen_words:
            print("Word has been seen before. Please try again.")
        elif not is_dictionary_word(new_word):
            print("Word is not a dictionary word. Please try again.") 
        elif len(new_word) > 4:
            print("Word is too long. Please try again.")
        else:
            print("Great work! Find another word.")
            score += 1
            seen_words.add(new_word)
        
        new_word = get_users_word()

    # Display score
    display_score(score)



if __name__ == '__main__':

    main()
