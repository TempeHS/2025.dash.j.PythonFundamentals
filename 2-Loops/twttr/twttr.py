def remove_vowels(tweet):
    vowels = "aeiouAEIOU"
    without_vowels = ""
    for char in tweet:
        if char not in vowels:
            without_vowels += char
    return without_vowels


def tweet():
    tweet = input("write a tweet, ")
    result = remove_vowels(tweet)
    print(result)


tweet()
