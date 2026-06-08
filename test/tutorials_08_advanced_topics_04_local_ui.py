# Block 1
import streamlit as st
import pandas as pd
import numpy as np

st.title("My Research Dashboard")
n_points = st.slider("Select number of points", 10, 1000, 100)

data = pd.DataFrame({'x': np.random.randn(n_points), 'y': np.random.randn(n_points)})
st.scatter_chart(data)

