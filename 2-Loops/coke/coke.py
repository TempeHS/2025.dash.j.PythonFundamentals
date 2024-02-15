def coke():
    coke_price = 0.50
    total_money = 0

    print("a total coke bottle is $0.50")
    print("please input your money in $0.25 $0.10 $0.05")

    while total_money < coke_price:
        money = float(input("please input your money"))
        if money not in [0.25, 0.10, 0.05]:
            print("invalid money amount please re input")
            continue
        total_money += money
    change = total_money - coke_price
    if change > 0:
        print(f"Here is your coke and ${change:.2f} change.")
    else:
        print("here is your coke you got no change")


coke()
