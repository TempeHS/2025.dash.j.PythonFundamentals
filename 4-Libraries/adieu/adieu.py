def main(names):
    if len(names) == 1:
        print(f"adieu, adieu {names[0]}")
    elif len(names) == 2:
        print(f"adieu, adiu {names[0]} and {names[0]}")
    else:
        farewell = ", ".join(names[:-1])
        farewell += f", and {names[-1]}"
        print(f"adieu, adieu {farewell}")


def Main2():
    print("enter names, one per line, control D to stop")
    names = []
    try:
        while True:
            name = input().strip()
            if name:
                names.append(name)
    except EOFError:
        pass
    main(names)


Main2()
