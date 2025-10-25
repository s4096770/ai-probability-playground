import streamlit as st
from simulate import roll_dice, flip_coin
from visuals import plot_distribution

st.set_page_config(page_title="AI Probability Playground", page_icon="🎲")

st.title("🎲 AI Probability Playground")
st.write("Explore randomness and probability — the heart of AI’s magic!")

option = st.selectbox("Choose an experiment:", ["Dice Roll", "Coin Flip"])

if option == "Dice Roll":
    rolls = st.slider("Number of rolls", 10, 1000, 100)
    results = roll_dice(rolls)
    st.write(f"Results from {rolls} rolls:")
    st.bar_chart(results.value_counts())
    plot_distribution(results)

elif option == "Coin Flip":
    flips = st.slider("Number of flips", 10, 1000, 100)
    results = flip_coin(flips)
    heads = int(sum(results))
    tails = flips - heads
    st.write(f"Heads: {heads}, Tails: {tails}")
    st.bar_chart({"Heads": heads, "Tails": tails})
