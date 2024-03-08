def main():
    menu = {
        "Baja taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    total_cost = 0
    print("the menu is,", end="")
    print(menu)

    try:
        while True:
            item = (
                input(
                    "please choose what items you would like,(control d to finish ordering) "
                )
                .strip()
                .title()
            )
            if item in menu:
                total_cost += menu[item]
                print(f"total cost is ${total_cost}")
        else:
            print("invalid item")
    except EOFError:
        print(f"order complete your total is{total_cost}")


main()
