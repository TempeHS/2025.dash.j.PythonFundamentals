def camel_to_snake(name):
    result = ""
    for char in name:
        result += "_" + char.lower()
    else:
        result += char
    return result


def main():
    camel_case_name = input("Enter a variable name in camel case: ")
    snake_case_name = camel_to_snake(camel_case_name)
    print("Snake case name:", snake_case_name)


main()
