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
        K = self.strike_price
        t = self.time
        r = self.interest_rate
        S = self.current_price
        sigma = self.volatility
        d1 = (np.log(S / K) + (r + (sigma ** 2) / 2) * t) / (sigma * np.sqrt(t))
        d2 = d1 - (sigma * np.sqrt(t))
        call_price = S * norm.cdf(d1) - K * np.exp(-r * t) * norm.cdf(d2)
        put_price = K * np.exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)
        return call_price, put_price

    def _calculate_prices(self, S, sigma) -> tuple[float, float]:
        """This one's for internal usage because the current price (S) and volatility (sigma) have to change.
        
        Only implemented in heatmap() to account for the variation in values. 
        """
        
        K = self.strike_price
        t = self.time
        r = self.interest_rate
        d1 = (np.log(S / K) + (r + (sigma ** 2) / 2) * t) / (sigma * np.sqrt(t))
        d2 = d1 - (sigma * np.sqrt(t))
        call_price = S * norm.cdf(d1) - K * np.exp(-r * t) * norm.cdf(d2)
        put_price = K * np.exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)
        return call_price, put_price

    def heatmap(self):
        ARRAY_LENGTH = 10
        RANGE = 0.2
        call_2darray = np.zeros((ARRAY_LENGTH, ARRAY_LENGTH))
        put_2darray = np.zeros((ARRAY_LENGTH, ARRAY_LENGTH))
        S_range = np.linspace(start=(1-RANGE)*self.current_price, stop=(1+RANGE)*self.current_price, num=ARRAY_LENGTH)
        sigma_range = np.linspace(start=(1-RANGE)*self.volatility, stop=(1+RANGE)*self.volatility, num=ARRAY_LENGTH)
        
        for i, S in enumerate(S_range):
            for j, sigma in enumerate(sigma_range):
                call, put = self._calculate_prices(S, sigma)
                call_2darray[i][j] = call
                put_2darray[i][j] = put

        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

        sns.heatmap(call_2darray, cmap="viridis", annot=True, ax=axes[0], fmt=".2f", annot_kws={"size": 5},
                    xticklabels=[str(x) for x in np.round(sigma_range, decimals=2)],
                    yticklabels=[str(y) for y in np.round(S_range, 2)])
        axes[0].set_title("Call Values")
        axes[0].set_xlabel("Volatility")
        axes[0].set_ylabel("Current Price")
        
        sns.heatmap(put_2darray, cmap="viridis", annot=True, ax=axes[1], fmt=".2f", annot_kws={"size": 5},
                    xticklabels=[str(x) for x in np.round(sigma_range, decimals=2)],
                    yticklabels=[str(y) for y in np.round(S_range, 2)])
        axes[1].set_title("Put Values")
        axes[1].set_xlabel("Volatility")
        axes[1].set_ylabel("Current Price")
        
        return fig
