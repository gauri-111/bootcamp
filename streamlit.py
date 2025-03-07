import streamlit as st
import numpy as np
import pandas as pd

st.write("chbc")

df=pd.DataFrame({
    'first column': ['a', 'b', 'c', 'd'],
    'second column': [10, 20, 30, 40]
})
df
st.write(df)
st.line_chart(df)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [19.07, 72.87],
    columns=['lat', 'lon'])

st.map(map_data)

x = st.slider('x')
st.write(x, 'squared is', x * x)

st.button("x")

st.selectbox(options=["gauri","amruta"],label="gauri")

st.text_input("Gauri", key="name")

st.number_input("df")

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)