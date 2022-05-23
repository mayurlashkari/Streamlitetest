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

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))


result =  st.button("Click Submit")
if result:
     st.write('User Is :', title)
     st.write('Age :' ,number)
   
     
else:
     st.write("No Click")

agree = st.checkbox('I agree')

if agree:
     st.write('Great!')


