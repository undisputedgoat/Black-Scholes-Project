import pytest
import numpy as np
from BlackScholes import BlackScholes

@pytest.fixture
def bs_model():
    return BlackScholes(current_price=100, strike_price=100, time=1, interest_rate=0.05, volatility=0.2)

def test_init(bs_model):
    assert bs_model.current_price == 100
    assert bs_model.strike_price == 100
    assert bs_model.time == 1
    assert bs_model.interest_rate == 0.05
    assert bs_model.volatility == 0.2

def test_calculate_prices(bs_model):
    call, put = bs_model.calculate_prices()
    # Expected values from manual Black-Scholes calc (rounded for float precision)
    assert np.isclose(call, 10.45, atol=0.01)  # Approx 10.45-10.46 depending on norm precision
    assert np.isclose(put, 5.57, atol=0.01)

def test_calculate_prices_edge_case():
    # Edge case: t=0, should return max(S-K, 0) for call, max(K-S, 0) for put
    bs = BlackScholes(current_price=100, strike_price=90, time=0, interest_rate=0.05, volatility=0.2)
    call, put = bs.calculate_prices()
    assert np.isclose(call, 10, atol=0.01)  # Intrinsic value
    assert np.isclose(put, 0, atol=0.01)

    bs = BlackScholes(current_price=80, strike_price=90, time=0, interest_rate=0.05, volatility=0.2)
    call, put = bs.calculate_prices()
    assert np.isclose(call, 0, atol=0.01)
    assert np.isclose(put, 10, atol=0.01)


def test_private_calculate_prices(bs_model):
    """Manual calc: d1 ≈ (log(110/100) + (0.05 + 0.0625/2)*1)/(0.25*sqrt(1)) ≈ (0.0953 + 0.08125)/0.25 ≈ 0.7062
    d2 ≈ 0.7062 - 0.25 ≈ 0.4562
    Call ≈ 110*norm.cdf(0.7062) - 100*exp(-0.05)*norm.cdf(0.4562) ≈ 110*0.7599 - 95.1229*0.6756 ≈ 83.59 - 64.27 ≈ 19.305
    Put ≈ 100*exp(-0.05)*norm.cdf(-0.4562) - 110*norm.cdf(-0.7062) ≈ 95.1229*0.3244 - 110*0.2401 ≈ 30.86 - 26.41 ≈ 4.428
    """
    call, put = bs_model._calculate_prices(S=110, sigma=0.25)
    assert np.isclose(call, 19.305, atol=0.01)
    assert np.isclose(put, 4.428, atol=0.02)