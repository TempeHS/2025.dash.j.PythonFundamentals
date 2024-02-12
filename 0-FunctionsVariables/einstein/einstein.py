def calculate_energy(mass_kg):
    speed_of_light = 300000000
    return mass_kg * speed_of_light**2


def main():
    mass_kg = int(input("what is the mass in kg ? :"))
    energy_joules = calculate_energy(mass_kg)
    print("the equivalent mass in joules is,", energy_joules)


main()
