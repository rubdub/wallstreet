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


def future_option_price(option, tgt_days, tgt_price, tgt_iv):
    ask = option.ask
    price = option.underlying.price
    iv = option.implied_volatility()
    delta = option.delta()
    gamma = option.gamma()
    theta = option.theta()
    vega = option.vega()
    rho = option.rho()

    print(ask)
    print(iv)

    final_price_delta = delta * (tgt_price-price)
    final_price_gamma = (gamma*delta)*(tgt_price-price)
    final_price_theta = (-1)*tgt_days*theta
    final_price_vega = (tgt_iv-iv)*vega
    final_price_rho = 0 # Not sure how to get the "Risk-Free Rate Of Return" from yahoo finance"
    final_price = ask+final_price_delta+final_price_gamma+final_price_theta+final_price_vega+final_price_rho
    return final_price

# stored_price_range = price_range(12, 16)

# c = Call('AMD', source='yahoo')
# print(c.expirations)

# price = []
# for strike_price in stored_price_range:
#     g = Call('AMD', d=4, m=8, y=2017, strike=strike_price, source='yahoo')
#     price.append(g.ask)
#
# print(price)
#
# plt.scatter(stored_price_range, price, color='red', marker='.', alpha=0.5, s=400)
# plt.show()

fut_opt13 = Call('AMD', d=4, m=8, y=2017, strike=13, source='yahoo')

price = []
for i in range(10, 17):
    option_price = future_option_price(fut_opt13, 1, i, .8906)
    price.append(option_price)

plt.scatter(range(10, 17), price, color='red', marker='.', alpha=0.5, s=400)
plt.show()


# S0 = 13.36
# K = 17
# r=0.15
# sigma = 87.5
# T = 32/365.0
# Otype='C'
#
#
#
# print("S0\tstock price at time 0:", S0)
# print("K\tstrike price:", K)
# print("r\tcontinuously compounded risk-free rate:", r)
# print("sigma\tvolatility of the stock price per year:", sigma)
# print("T\ttime to maturity in trading years:", T)
#
#
# t=time.time()
# c_BS = BlackScholes(Otype,S0, K, r, sigma, T)
# elapsed=time.time()-t
# print("c_BS\tBlack-Scholes price:", c_BS, elapsed)



