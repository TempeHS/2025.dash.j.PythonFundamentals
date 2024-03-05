def main():
    plates = input("enter plate: ")
    if is_valid(plates):
        print("valid")
    else:
        print("invalid try again")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        print("invalid plate try again")
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    if s[2:].isdigit() and s[2] != "0":
        return True
    else:
        return False


main()
