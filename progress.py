import time
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )


with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

df1 = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

my_table = st.table(df1)

df2 = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))


# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
my_chart.add_rows(df2)
# Now the chart shown in the Streamlit app contains the data for
# df1 followed by the data for df2.
my_chart = st.vega_lite_chart({
     'mark': 'line',
     'encoding': {'x': 'a', 'y': 'b'},
     'datasets': {
       'some_fancy_name': df1,  # <-- named dataset
      },
     'data': {'name': 'some_fancy_name'},
 }),
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
