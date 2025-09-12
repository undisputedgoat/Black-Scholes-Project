from math import exp, sqrt, log
import numpy as np
import streamlit as st
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

class BlackScholes:
  def __init__(self, current_price, strike_price, time, interest_rate, volatility):
    self.current_price = current_price
    self.strike_price = strike_price
    self.time = time
    self.interest_rate = interest_rate
    self.volatility = volatility

  def calculate_prices(self, S, sigma) -> tuple[float, float]:
    K = self.strike_price
    t = self.time
    r = self.interest_rate
    d1 = (log(S / K) + (r + (sigma ** 2) / 2) * t) / (sigma * sqrt(t))
    d2 = d1 - (sigma * sqrt(t))
    call_price = S * norm.cdf(d1) - K * exp(-r * t) * norm.cdf(d2)
    put_price = K * exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return call_price, put_price

  def heatmap(self):
    call_2darray = np.zeros((10, 10))
    put_2darray = np.zeros((10, 10))
    S_range = np.linspace(0.8*self.current_price, 1.2*self.current_price, 10)
    sigma_range = np.linspace(0.8*self.volatility, 1.2*self.volatility, 10)
    
    for i, S in enumerate(S_range):
      for j, sigma in enumerate(sigma_range):
        call, put = self.calculate_prices(S, sigma)
        call_2darray[i][j] = call
        put_2darray[i][j] = put
    
    
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

    sns.heatmap(call_2darray, cmap="viridis", annot=True, ax=axes[0], fmt=".2f", annot_kws={"size": 5})
    axes[0].set_title("Call Values")
    axes[0].set_xlabel('Spot Price')
    axes[0].set_ylabel('Volatility')
    
    sns.heatmap(put_2darray, cmap="viridis", annot=True, ax=axes[1], fmt=".2f", annot_kws={"size": 5})
    axes[1].set_title("Put Values")
    axes[1].set_xlabel('Spot Price')
    axes[1].set_ylabel('Volatility')
    
    st.pyplot(fig)
    
    return call_2darray, put_2darray
