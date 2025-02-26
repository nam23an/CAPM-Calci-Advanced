import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
import os

# Function to check if file exists
def file_exists(file_path):
    return os.path.exists(file_path)

# Function to calculate CAPM with high precision
def calculate_capm(rf, beta, rm):
    return rf + beta * (rm - rf)

# Function to format numbers dynamically
def format_number(value):
    return f"{value:.9f}".rstrip('0').rstrip('.') if '.' in f"{value:.9f}" else f"{value:.9f}"

# Function to show Mario GIF
def show_mario_gif():
    gif_path = "mario.gif"
    if file_exists(gif_path):
        st.image(gif_path, width=120)
    else:
        st.warning("Mario GIF not found!")

# Streamlit UI
st.title("CAPM Calculator")
st.markdown("## Capital Asset Pricing Model (CAPM)")

# Input Fields
rf = st.number_input("Risk-Free Rate (Rf) in %:", min_value=0.0, step=0.1, value=2.0) / 100
beta = st.number_input("Beta (β):", min_value=0.0, step=0.1, value=1.0)
rm = st.number_input("Expected Market Return (Rm) in %:", min_value=0.0, step=0.1, value=8.0) / 100

if st.button("Calculate CAPM"):
    with st.spinner("Calculating..."):
        time.sleep(2)  # Simulating Processing Time
        expected_return = calculate_capm(rf, beta, rm) * 100
        st.success(f"Expected Return: {format_number(expected_return)}%")
        
        # Show Mario GIF
        show_mario_gif()

    # Plot Security Market Line (SML)
    beta_range = np.linspace(0, 2, 100)
    sml = rf * 100 + beta_range * (rm * 100 - rf * 100)
    
    fig, ax = plt.subplots()
    ax.plot(beta_range, sml, label="Security Market Line (SML)", color="blue")
    ax.scatter(beta, expected_return, color='red', label="Your Asset")
    ax.set_xlabel("Beta (β)")
    ax.set_ylabel("Expected Return (%)")
    ax.set_title("Security Market Line")
    ax.legend()
    st.pyplot(fig)

    # Bar Chart of Inputs
    st.subheader("Input Comparison")
    st.bar_chart({"Risk-Free Rate (%)": rf * 100, "Market Return (%)": rm * 100, "Your Expected Return (%)": expected_return})

# Syndicate 16 Signature
st.markdown("---")
st.markdown("### Prepared by - Syndicate 16")
