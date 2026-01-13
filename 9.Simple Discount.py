def PRICE(p):
    p = float(p)
    if p >= 1000:
        p = p * (100 - 10) / 100
        print(f"Final Price = {p:.2f}")
    else:
        print("= No discount")


price = input("Price : ")
PRICE(price)
