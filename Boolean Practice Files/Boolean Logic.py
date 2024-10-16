
# gold purity test
purity = float(input())


def purity_test():
    if 75 <= purity <= 83.2:
        return "18K"
    elif 83.3 <= purity <= 91.6:
        return "20K"
    elif 91.7 <= purity <= 99.8:
        return "22K"
    elif purity >= 99.9:
        return "24K"


print(purity_test())
