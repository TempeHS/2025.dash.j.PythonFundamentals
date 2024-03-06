def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    try:
        while True:
            Birth_Date = input("enter your birthdate in MM/DD/YYYY ").strip()
            try:
                month, day, year = map(int, Birth_Date.split("/"))
            except ValueError:
                try:
                    month_name, day, year = Birth_Date.split()
                    month = months.index(month_name) + 1
                except (ValueError, IndexError):
                    print(
                        "Invalid date format. Please enter the date in MM/DD/YYYY or Month Day, Year format."
                    )
                    continue
            formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
            print("Formatted date:", formatted_date)
    except EOFError:
        print("End of input.")


main()
