def main():
    equation = input("input an equation")
    (
        x,
        y,
        z,
    ) = equation.split
    x_f = float(x)
    z_f = float(z)
    if y == ("+"):
        print(x_f + z_f)
    elif x == ("/"):
        print("x_f / z_f")


main()
