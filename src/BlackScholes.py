from numpy import exp, sqrt, log
import numpy as np
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
    
  def calculate_prices(self) -> tuple[float, float]:
    S = self.current_price
    K = self.strike_price
    t = self.time
    r = self.interest_rate
    sigma = self.volatility
    d1 = (log(S / K) + (r + (sigma ** 2) / 2) * t) / (sigma * sqrt(t))
    d2 = d1 - (sigma * sqrt(t))
    call_price = S * norm.cdf(d1) - K * exp(-r * t) * norm.cdf(d2)
    put_price = K * exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1) 
    return call_price, put_price
  
  def heatmap(self):
    """Heatmap displays current price over volatility"""
    current_price_range = np.linspace(start=self.current_price*0.5, stop=self.current_price*1.5, num=10)
    sigma_range = np.linspace(start=self.volatility*0.5, stop=self.volatility*1.5, num=10)
    
    current_price_grid, sigma_grid = np.meshgrid(current_price_range, sigma_range)
    # values = tuple(zip(current_price_grid.ravel(), sigma_grid.ravel()))
    
    fig_call, ax_call = plt.subplots(figsize=(10, 8))
    sns.heatmap(current_price_grid, xticklabels=np.round(current_price_range, 2), yticklabels=np.round(sigma_range, 2), annot=True, fmt=".2f", cmap="viridis", ax=ax_call)
    ax_call.set_title('CALL')
    ax_call.set_xlabel('Spot Price')
    ax_call.set_ylabel('Volatility')
    
    # Plotting Put Price Heatmap
    fig_put, ax_put = plt.subplots(figsize=(10, 8))
    sns.heatmap(sigma_grid, xticklabels=np.round(current_price_range, 2), yticklabels=np.round(sigma_range, 2), annot=True, fmt=".2f", cmap="viridis", ax=ax_put)
    ax_put.set_title('PUT')
    ax_put.set_xlabel('Spot Price')
    ax_put.set_ylabel('Volatility')
    
    plt.show()
    return fig_call, fig_put
