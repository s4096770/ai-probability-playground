import matplotlib.pyplot as plt
import streamlit as st

def plot_distribution(data):
    """Plot a histogram of the data."""
    fig, ax = plt.subplots()
    ax.hist(data, bins=range(1, 8), align="left", rwidth=0.8, color='skyblue', edgecolor='black')
    ax.set_xlabel("Outcome")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of outcomes")
    st.pyplot(fig)
