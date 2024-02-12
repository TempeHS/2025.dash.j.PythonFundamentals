life = input("whats the answer for the great question of life ")

match life:
    case "42" | "forty-two" | "forty two":
        print("yes")
    case _:
        print("no")
