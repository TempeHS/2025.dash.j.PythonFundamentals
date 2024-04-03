def main():
    with open("myText.txt", "r") as file:
        for line in file:
            num = int(line)
            new = num + 1

    with open("myText.txt", "w") as file:
        file.write(f"{new}")


main()
