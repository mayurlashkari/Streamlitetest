import streamlit as st

import pandas as pd
import numpy as np
import altair as alt
import cv2
import numpy as np



chart_data = pd.DataFrame(
     np.random.randn(10, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)

title = st.text_input('Enter User Name', 'Life of Brian')
number = st.number_input('Insert a User Age')

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)


result =  st.button("Click Submit")
if result:
     st.write('User Is :', title)
     st.write('Age :' ,number)
   
     
else:
     st.write("No Click")

agree = st.checkbox('I agree')

if agree:
     st.write('Great!')


