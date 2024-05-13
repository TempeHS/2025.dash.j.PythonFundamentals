from datetime import datetime


def main(age_in_min):
    years = age_in_min // (365 * 24 * 60)
    days = (age_in_min % (365 * 24 * 60)) // (24 * 60)
    print(f"you are {(int(years))} years {(int(days))} min ")


def USER_INPUT():
    birth_date = input("YYYY/MM/DD ").split("/")
    birth_datetime = datetime.strptime("/".join(birth_date), "%Y/%m/%d")
    age_in_min = (datetime.now() - birth_datetime).total_seconds() / 60
    return age_in_min


if __name__ == "__main__":
    age_in_min = USER_INPUT()
    main(age_in_min)
