def convert(time_str):
    try:
        hours, minutes = map(int, time_str.split(".").split(":"))
        return hours + minutes / 60
    except ValueError:
        print(
            "Invalid input format. Please enter the time in 24-hour format as 'HH:MM'."
        )
        return None


def main():
    user_input = input("what is the time in 24 hour format? ")
    time = convert(user_input)
    breakfast_start = 6.0
    breakfast_end = 11.0
    lunch_start = 12.0
    lunch_end = 14.0
    dinner_start = 18.0
    dinner_end = 20.0
    if breakfast_start <= time <= breakfast_end:
        print("it is breakfast")
    elif lunch_start <= time <= lunch_end:
        print("it is lunch")
    elif dinner_start <= time <= dinner_end:
        print("it is dinner")


main()
