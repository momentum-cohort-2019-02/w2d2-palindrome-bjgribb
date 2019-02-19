# name = input("What is your name? ")
# print(name [::-1])
# print(name [::1])

# phrase = input("what is your phrase")

# cleaned_phrase = re.sub(r"[^a-zA-Z0-9]","",phrase)

# print(cleaned_phrase)
# cleaned_phrase = input("type")
import re # imports regular expressions
# nospace_phrase = re.sub(' ','',cleaned_phrase)
# print(nospace_phrase)

def palindrome(phrase):
    """Takes a phrase cleans it to remove space and no 
    alpha-numeric characters and determines if its a palindrome or not"""
    phrase = re.sub(r"[^A-Za-z]", "", phrase.lower())
    if len(phrase) == 0:
        return print("Please type something in.")
    elif phrase [::-1] == phrase:
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")

palindrome(input("What is your phrase? "))

# words = "the brown cows"
# print(words[-1:-5:-1])

