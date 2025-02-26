import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import json
import requests

# Set page configuration
st.set_page_config(page_title="CAPM Calculator", page_icon="📊", layout="wide")

# Load Lottie Animation from URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None

lottie_success = load_lottie_url("https://lottie.host/3e86d5a3-c3a3-4b19-92bb-4d6e6764d42e/Pc8j6vh3yq.json")  # New fun character

# Custom CSS for better styling
st.markdown("""
    <style>
    .stApp { background-color: #f7f7f7; }
    .main { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px gray; }
    .stTextInput, .stNumberInput { border-radius: 5px !important; }
    </style>
""", unsafe_allow_html=True)

# Sidebar with title
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/4/4c/Modern_Portfolio_Theory.png", use_container_width=True)
st.sidebar.title("📈 CAPM Calculator")
st.sidebar.markdown("This tool helps you calculate the Expected Return using the Capital Asset Pricing Model (CAPM).")

# Main content
st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("📊 Capital Asset Pricing Model (CAPM) Calculator")

# User Inputs
st.write("### 🔢 Enter the following values:")

col1, col2, col3 = st.columns(3)

with col1:
    rf = st.number_input("Risk-Free Rate (rf) in %", value=2.0, step=0.1)

with col2:
    beta = st.number_input("Beta (β)", value=1.0, step=0.1)

with col3:
    rm = st.number_input("Market Return (rm) in %", value=8.0, step=0.1)

# CAPM Calculation Function
def calculate_capm(rf, beta, rm):
    return rf + beta * (rm - rf)

# Calculate Button
if st.button("📌 Calculate CAPM"):
    with st.spinner("Calculating... ⏳"):
        result = calculate_capm(rf, beta, rm)
        st.success(f"📊 CAPM Expected Return: {result:.2f}%")
        
        # Lottie Animation
        if lottie_success:
            st_lottie(lottie_success, height=250, width=250)
        
        # Interactive Graph using Plotly
        st.write("### 📈 CAPM Formula Visualization")
        
        x = np.linspace(0, 2, 10)  # Simulated beta values
        y = rf + x * (rm - rf)  # Expected return

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name="Expected Return", line=dict(color="blue", width=3)))
        fig.add_trace(go.Scatter(x=[beta], y=[result], mode='markers', name="Your Input", marker=dict(size=12, color="red")))

        fig.update_layout(title="CAPM Expected Return vs. Beta",
                          xaxis_title="Beta (β)",
                          yaxis_title="Expected Return (%)",
                          template="plotly_white")

        st.plotly_chart(fig, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
