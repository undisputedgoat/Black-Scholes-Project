import streamlit as st
import pandas as pd
from BlackScholes import BlackScholes

def main():
    st.set_page_config(
        page_title="Black-Scholes Option Pricing Model",
        page_icon="📈",
        layout="wide")
    st.title("Black-Scholes Option Pricing")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        current_price = st.number_input("Current Asset Price", value=100.0, min_value=1e-6)
    with col2:
        strike = st.number_input("Strike Price", value=100.0, min_value=1e-6)
    with col3:
        time = st.number_input("Time to Maturity (Years)", value=1.0, min_value=1e-6)
    with col4:
        volatility = st.number_input("Volatility (σ)", value=0.2, min_value=1e-6)
    with col5:
        interest_rate = st.number_input("Risk-Free Interest Rate", value=0.05)

    model = BlackScholes(current_price, strike, time, interest_rate, volatility)
    call, put = model.calculate_prices()
    c1, c2 = st.columns(2)
    with c1: 
        st.metric("Call", f"{call:.2f}")
    with c2: 
        st.metric("Put", f"{put:.2f}")
        
    st.subheader("Options Price - Heatmap")
    st.pyplot(model.heatmap())

    st.subheader("Explanation for Black-Scholes")
    df = pd.DataFrame(
        {
        "Variable": ["C", "N", "S", "K", "r", "t", "σ"],
        "Description": ["Theoretical price of a European call option (the output)", 
                        "CDF of the normal distribution",
                        "Current asset price (spot price)",
                        "Strike price",
                        "Risk free interest rate",
                        "Time to maturity",
                        "Volatility of asset"]
        }
    )
    st.dataframe(df.set_index("Variable"))


if __name__ == "__main__":
    main()
