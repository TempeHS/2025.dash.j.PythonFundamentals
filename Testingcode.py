def Main(names):
    if len(names) == 1:
        print(f"adieo, adieo {names[0]}")
    elif len(names) == 2:
        print(f"adieo, adieo {names[0]} and {names[1]}")
    else:
        farwell = ",".join(names[:-1])
        farwell += (f, "and {names[-1]}")
        print(f"adieu, adieu {farewell}")


def Main2():
    print("input names control D to stop")
    names = []
    try:
        while True:
            name = input().strip()
            if name:
                names.append(name)
    except EOFError:
        pass


Main2()
