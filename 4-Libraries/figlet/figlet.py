import sys
from pyfiglet import Figlet


def main():
    figlet = figlet()
    fonts = Figlet.getFonts()
    try:
        if len(sys.argv) == 1:
            selected_font = fonts[random.randint(0, len(fonts) - 1)]
            text = input("Enter text: ")
            print(figlet.renderText(text, font=selected_font))
        elif (
            len(sys.argv) == 3
            and sys.argv[1] in ["-f", "--font"]
            and sys.argv[2] in fonts
        ):
            text = input("Enter text: ")
            print(figlet.renderText(text, font=sys.argv[2]))
    except IndexError:
        print("invalid")
        sys.exit


main()
