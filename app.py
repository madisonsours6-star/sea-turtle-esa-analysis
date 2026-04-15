import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Sea Turtle Analysis 🐢", layout="centered")

# Title
st.title("🐢 Sea Turtle Population Tracker")
st.subheader("Analyzing the impact of the Endangered Species Act")

st.markdown("---")

# Data
data = {
"Year": [1950, 1978, 1990, 2000, 2010, 2020],
"Green Turtle": [200, 250, 1000, 5000, 15000, 50000],
"Loggerhead Turtle": [1000, 1200, 1500, 2000, 2500, 3000],
"Leatherback Turtle": [10000, 5000, 2000, 1000, 500, 300]
}

df = pd.DataFrame(data)

# Sidebar
st.sidebar.header("🌊 Customize Your View")

species = st.sidebar.selectbox(
"Choose a species:",
["Green Turtle", "Loggerhead Turtle", "Leatherback Turtle"]
)

show_all = st.sidebar.checkbox("Show all species comparison")

st.markdown("## 📊 Population Trends")

# Plot
fig, ax = plt.subplots()

if show_all:
    ax.plot(df["Year"], df["Green Turtle"], marker='o', label="Green")
    ax.plot(df["Year"], df["Loggerhead Turtle"], marker='o', label="Loggerhead")
    ax.plot(df["Year"], df["Leatherback Turtle"], marker='o', label="Leatherback")
    ax.legend()
else:
    ax.plot(df["Year"], df[species], marker='o')

# ESA marker
ax.axvline(x=1973)

ax.set_xlabel("Year")
ax.set_ylabel("Nesting Population")
ax.set_title("Sea Turtle Population Over Time")

st.pyplot(fig)

st.markdown("---")

# Metrics
st.markdown("## 📈 Key Stats")

start = df[species].iloc[0]
end = df[species].iloc[-1]
growth = ((end - start) / start) * 100

col1, col2, col3 = st.columns(3)

col1.metric("Start Population", start)
col2.metric("Current Population", end)
col3.metric("Growth %", f"{growth:.1f}%")

st.markdown("---")

# Insight section
st.markdown("## 🧠 What does this mean?")

if species == "Green Turtle":
    st.success("💚 Strong recovery! Conservation efforts have been highly effective.")
elif species == "Loggerhead Turtle":
    st.warning("🧡 Moderate growth. Recovery is slower and may need more support.")
else:
    st.error("❤️ Decline detected. Protection alone may not be enough for this species.")

st.markdown("---")

# Fun section
st.markdown("## 🌟 Fun Fact")
st.info("Sea turtles can live for over 50 years and travel thousands of miles!")

st.markdown("---")

# Footer
st.caption("Created as a data science project analyzing conservation impact 🌍")
