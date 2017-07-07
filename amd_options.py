#Options calculator for building option price mapping
#Rubdub 7-6-17

from wallstreet import Stock, Call, Put
import matplotlib.pyplot as plt

# g = Call('AMD', d=4, m=8, y=2017, strike=14, source='yahoo')

price = []


def price_range(low, high):
    price = low
    price_list = []
    price_list.append(low)
    while price < high:
        price += .5
        price_list.append(price)
    return price_list

stored_price_range = price_range(12, 16)

c = Call('AMD', source='yahoo')
print(c.expirations)

for strike_price in stored_price_range:
    g = Call('AMD',expiration='04-08-2017', strike=strike_price, source='yahoo')
    price.append(g.ask)

print(price)

plt.scatter(stored_price_range, price, color='red', marker='.', alpha=0.5, s=400)
plt.show()
