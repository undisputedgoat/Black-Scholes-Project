import streamlit as st
import matplotlib.pyplot as plt
from BlackScholes import BlackScholes

def main():
  st.set_page_config(
    page_title="Black-Scholes Option Pricing Model",
    page_icon="📈",
    layout="wide")
  st.title("Black-Scholes Option Pricing")
  col1, col2 = st.columns([1, 3])
  
  with col1:
    current_price = st.number_input("Current Asset Price", value=100.0)
    strike = st.number_input("Strike Price", value=100.0)
    time = st.number_input("Time to Maturity (Years)", value=1.0)
    volatility = st.number_input("Volatility (σ)", value=0.2)
    interest_rate = st.number_input("Risk-Free Interest Rate", value=0.05)
    
  with col2:
    model = BlackScholes(current_price, strike, time, interest_rate, volatility)
    call, put = model.calculate_prices()
    c1, c2 = st.columns(2)
    with c1: 
      st.metric("Call", f"{call:.2f}")
    with c2: 
      st.metric("Put", f"{put:.2f}")
    
    st.subheader("Options Price - Interactive Heatmap")
    st.write("Explore how option prices fluctuate with varying 'Spot Prices and Volatility' levels using interactive heatmap parameters, all while maintaining a constant 'Strike Price'.")
    st.write(model.heatmap())

if __name__ == "__main__":
  main()
