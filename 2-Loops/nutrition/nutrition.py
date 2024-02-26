def fruit():
    fruit = input("name a fruit ")
    fruits = {
        "apple": " 130 cal",
        "avocado": "30 cal",
        "banana": "110 cal",
        "Cantaloupe": "50 cal",
        "grapefruit": "60cal",
        "grapes": "90 cal",
        "honeydue Melon": "50 cal",
        "kiwi fruit": "90 cal",
        "lemon": "15 cal",
        "lime": "20 cal",
        "nectarine": "60 cal",
        "orange": "80 cal",
        "peach": "60 cal",
        "pear": "100 cal",
        "pineapple": "50 cal",
        "plums": "70 cals",
        "strawberrys": "50 cal",
        "sweet cherry": "100 cal",
        "tangerine": "50 cal",
        "watermelon": "80 cal",
    }
    if fruit in fruits:
        print(f" A {fruit} has {fruits [fruit]}")
    else:
        print("invalid")


fruit()
