import streamlit as st

import pandas as pd
import numpy as np
import altair as alt

chart_data = pd.DataFrame(
     np.random.randn(10, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)

title = st.text_input('Enter User Name', 'Life of Brian')
number = st.number_input('Insert a User Age')
d = st.date_input("When's your birthday",datetime.date(2019, 7, 6))
result =  st.button("Click Submit")
if result:
     st.write('User Is :', title)
     st.write('Age :' ,number)
     st.write('DOB :' ,d)
     
else:
     st.write("No Click")

agree = st.checkbox('I agree')

if agree:
     st.write('Great!')


