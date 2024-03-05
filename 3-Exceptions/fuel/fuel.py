try:
    x = input("whats fuel amount format as 0/0? ")
    numerator, denominator = map(int, x.split("/"))
    if numerator <= 0 or denominator <= 0:
        print(
            ValueError(
                "numerator and or denominator can not be less than or equal to zero"
            )
        )
    if numerator > denominator:
        print(ValueError("the numerator must be equal to or less than the denominator"))
    percentage = (numerator / denominator) * 100

    if percentage <= 1:
        print("tank is almost empty")
    elif percentage >= 99:
        print("tank is almost full")
    else:
        print(f"tank is {round(percentage)}%")
except ValueError:
    print("invalid")
