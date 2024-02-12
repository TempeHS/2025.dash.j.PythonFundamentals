def main():
    x = input("Hello please give us a greeting ").lower().strip()
    if x.startswith("hello"):
        print("$0")
    elif x.startswith("H"):
        print("$20")
    else:
        print("$100")


main()
