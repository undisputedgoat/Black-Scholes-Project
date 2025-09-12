import streamlit as st
from BlackScholes import BlackScholes

def main():
  st.set_page_config(
    page_title="Black-Scholes Option Pricing Model",
    page_icon="📈",
    layout="wide")
  st.title("Black-Scholes Option Pricing")
  
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    current_price = st.number_input("Current Asset Price", value=100.0)
  with col2:
    strike = st.number_input("Strike Price", value=100.0)
  with col3:
    time = st.number_input("Time to Maturity (Years)", value=1.0)
  with col4:
    volatility = st.number_input("Volatility (σ)", value=0.2)
  with col5:
    interest_rate = st.number_input("Risk-Free Interest Rate", value=0.05)

  model = BlackScholes(current_price, strike, time, interest_rate, volatility)
  call, put = model.calculate_prices(current_price, volatility)
  c1, c2 = st.columns(2)
  with c1: 
    st.metric("Call", f"{call:.2f}")
  with c2: 
    st.metric("Put", f"{put:.2f}")
    
  st.subheader("Options Price - Heatmap")
  model.heatmap()

  # Explanation of the Black_Scholes Equation
  st.latex(r"""
  C = N(d_1) S_t - N(d_2) K e^{-rt}
  """)

  st.latex(r"""
  where \: d_1 = \frac{\ln \frac{S_t}{K} + \left(r + \tfrac{1}{2}\sigma^2\right)t}{\sigma \sqrt{t}}
  """)

  st.latex(r"""
  and \: d_2 = d_1 - \sigma \sqrt{t}
  """)


if __name__ == "__main__":
  main()
