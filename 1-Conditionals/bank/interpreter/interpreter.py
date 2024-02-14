def main():
    x = int(input("what is x? "))
    y = input("what is y? ")
    z = int(input("what is z? "))
    x = float(x)
    z = float(z)
    if y == ("+"):
        print(x + z)
    elif y == ("/"):
        print(x / z)
    elif y == ("*"):
        print(x * z)
    elif y == ("-"):
        print(x - z)
    else:
        print("math error")


main()
