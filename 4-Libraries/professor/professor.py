import random


def getLevel():
    while True:
        try:
            level = int(input("select a level 1,2,3"))
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except EOFError:
            print("invalid number redo")


def generate_integer(level):
    return random.randint(10 ** (level - 1), 10 ** (level - 1))


def main():
    level = getLevel()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        tries = 0
        while tries < 3:
            user_answer = input(f"what is the answer to {x} + {y}? ")
            tries += 1
            try:
                user_answer = int(user_answer)
                correct_answer = int(correct_answer)
                if user_answer == correct_answer:
                    print("correct")
                    score += 1
                    break
                else:
                    print("incorrect")
            except ValueError:
                print("invalid retry")
        if tries == 3:
            print(f"out of tries,correct answer is {correct_answer}")
            break
    print(f"your score is {score}/10")


main()
