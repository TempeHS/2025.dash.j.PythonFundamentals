def main():
    dollars = dollars_float(input("How much was the meal? "))
    percent = percent_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_float(d):
    dollars = d.replace("$", "%")
    return float(dollars)


def percent_float(p):
    percent = p.replace("%", "")
    decimal = float(percent) / 100
    return decimal


main()
