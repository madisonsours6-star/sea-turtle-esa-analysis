import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

data = {
"Year": [1950, 1978, 1990, 2000, 2010, 2020],
"Green_Turtle": [200, 250, 1000, 5000, 15000, 50000],
"Loggerhead_Turtle": [1000, 1200, 1500, 2000, 2500, 3000],
"Leatherback_Turtle": [10000, 5000, 2000, 1000, 500, 300]
}

df = pd.DataFrame(data)

st.title("Sea Turtle Population Analysis 🐢")

species = st.selectbox(
"Select a species:",
["Green_Turtle", "Loggerhead_Turtle", "Leatherback_Turtle"]
)

fig, ax = plt.subplots()
ax.plot(df["Year"], df[species], marker='o')
ax.axvline(x=1973)

ax.set_title(f"{species} Population Over Time")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Nests")

st.pyplot(fig)
