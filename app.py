import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go  # Interactive graph
import requests  # To fetch Lottie animations
from streamlit_lottie import st_lottie  # Animation support

# Set page configuration
st.set_page_config(page_title="CAPM Calculator", page_icon="📊", layout="wide")

# Load Lottie Animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return None

# Animation URL (Change to any preferred Lottie animation)
lottie_success = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_hjmovzsy.json")

# Sidebar
st.sidebar.title("📈 CAPM Calculator")
st.sidebar.markdown("This tool calculates the *Expected Return* using the *Capital Asset Pricing Model (CAPM)*.")

# Main content
st.title("📊 Capital Asset Pricing Model (CAPM) Calculator")
st.write("### 🔢 Enter the values:")

col1, col2, col3 = st.columns(3)

with col1:
    rf = st.number_input("Risk-Free Rate (rf) in %", value=2.0, step=0.1)

with col2:
    beta = st.number_input("Beta (β)", value=1.0, step=0.1)

with col3:
    rm = st.number_input("Market Return (rm) in %", value=8.0, step=0.1)

# CAPM Formula
def calculate_capm(rf, beta, rm):
    return rf + beta * (rm - rf)

# Calculate Button
if st.button("📌 Calculate CAPM"):
    with st.spinner("Calculating... ⏳"):
        result = calculate_capm(rf, beta, rm)
        st.success(f"📊 CAPM Expected Return: {result:.2f}%")

        # Display animation after calculation
        st_lottie(lottie_success, height=200, width=200)

    # Interactive Graph with Plotly
    st.write("### 📈 CAPM Formula Interactive Graph")

    x = np.linspace(0, 2, 10)  # Simulated beta values
    y = rf + x * (rm - rf)  # Expected return

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Expected Return", line=dict(color="blue", width=3)))
    fig.add_trace(go.Scatter(x=[beta], y=[result], mode="markers", name="Your Input", marker=dict(color="red", size=12)))

    fig.update_layout(
        title="Expected Return vs Beta (CAPM Model)",
        xaxis_title="Beta (β)",
        yaxis_title="Expected Return (%)",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)
