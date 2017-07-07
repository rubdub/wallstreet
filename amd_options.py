#Options calculator for building option price mapping
#Rubdub 7-6-17

from wallstreet import Stock, Call, Put
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss
import time

# Black and Scholes
def d1(S0, K, r, sigma, T):
    return (np.log(S0 / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))


def d2(S0, K, r, sigma, T):
    return (np.log(S0 / K) + (r - sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))


def BlackScholes(type, S0, K, r, sigma, T):
    if type == "C":
        return S0 * ss.norm.cdf(d1(S0, K, r, sigma, T)) - K * np.exp(-r * T) * ss.norm.cdf(d2(S0, K, r, sigma, T))
    else:
        return K * np.exp(-r * T) * ss.norm.cdf(-d2(S0, K, r, sigma, T)) - S0 * ss.norm.cdf(-d1(S0, K, r, sigma, T))

# Range of expiration strike prices
def price_range(low, high):
    price = low
    price_list = []
    price_list.append(low)
    while price < high:
        price += .5
        price_list.append(price)
    return price_list


stored_price_range = price_range(12, 16)

# c = Call('AMD', source='yahoo')
# print(c.expirations)

price = []
for strike_price in stored_price_range:
    g = Call('AMD', d=4, m=8, y=2017, strike=strike_price, source='yahoo')
    price.append(g.ask)

print(price)

plt.scatter(stored_price_range, price, color='red', marker='.', alpha=0.5, s=400)
plt.show()


S0 = 13.36
K = 17
r=0.15
sigma = 87.5
T = 32/365.0
Otype='C'



print("S0\tstock price at time 0:", S0)
print("K\tstrike price:", K)
print("r\tcontinuously compounded risk-free rate:", r)
print("sigma\tvolatility of the stock price per year:", sigma)
print("T\ttime to maturity in trading years:", T)


t=time.time()
c_BS = BlackScholes(Otype,S0, K, r, sigma, T)
elapsed=time.time()-t
print("c_BS\tBlack-Scholes price:", c_BS, elapsed)



