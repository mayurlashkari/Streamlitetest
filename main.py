import streamlit as st

import pandas as pd
import numpy as np
import altair as alt

chart_data = pd.DataFrame(
     np.random.randn(10, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)
result =  st.button("Click Here")
if result:
     st.write(":smile:"*5)
else:
     st.write("No Click")

agree = st.checkbox('I agree')

if agree:
     st.write('Great!')
