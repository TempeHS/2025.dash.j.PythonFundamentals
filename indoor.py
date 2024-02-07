# ask the input user to type some capslocks
word = input("type some words, ")

# remove whitespace from str and uncapitalise the letter for each word
word = word.casefold()

print("the output for these words are,", end="")
print(word)
