def main():
    grocery_counter = {}

    try:
        while True:
            item = input("whats your grocery list(control D to finish) ")
            if item:
                if item in grocery_counter:
                    grocery_counter[item] += 1
                else:
                    grocery_counter[item] = 1
    except EOFError:
        for item, count in sorted(grocery_counter.items()):
            print(f"grocery list is {count}{item.upper()}")


main()
