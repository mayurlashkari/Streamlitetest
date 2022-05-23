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
result =  st.button("Click Submit")
if result:
     st.write('User Is :', title)
     st.write('Age :' ,number)
else:
     st.write("No Click")

agree = st.checkbox('I agree')

if agree:
     st.write('Great!')

txt = st.text_area('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
st.write('Sentiment:', run_sentiment_analysis(txt))
