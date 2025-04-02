# -*- coding: utf-8 -*-
"""my_app.py"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Streamlit Widgets")

# --- Widgets ---

# Slider
x = st.slider("Select a value", 0, 100, 50)
st.write("Selected value:", x)

# Text input
name = st.text_input("Enter your name", "Type here...")
st.write("Hello,", name)

# Checkbox
show_data = st.checkbox("Show data")
if show_data:
    st.write("Data is being displayed.")

# Selectbox
option = st.selectbox(
    'Which number do you like best?',
     [1,2,3,4,5,6,7,8,9,10])

st.write('You selected:', option)

# --- Displaying Data ---

st.write("## Displaying Data")

data = {'col1': [1, 2, 3, 4], 'col2': [10, 20, 30, 40]}
df = pd.DataFrame(data)
st.write("Here's a DataFrame:")
st.write(df)

# Displaying a chart
plt.plot(df['col1'], df['col2'])
st.pyplot(plt)



# --- Adding Chat Section After Plot ---

with st.chat_message("user"):
    st.write("Hello 👋")

with st.chat_message("assistant"):
    st.write("Hello human")
    st.bar_chart(df)  # you can reuse the same df here for demo

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
