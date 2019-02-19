# name = input("What is your name? ")
# print(name [::-1])
# print(name [::1])

def palin(phrase):
    if len(phrase) == 0:
        return print("Please type something in.")
    elif phrase [::-1] == phrase [::1]:
        return print("This is a palindrome.")
    else:
        return print("This is NOT a palindrome.")

palin(input("What is your phrase? "))

# words = "the brown cows"
# print(words[-1:-5:-1])



