import time
import streamlit as st
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.01)
     my_bar.progress(percent_complete + 1)

with st.spinner('Wait for it...'):
    time.sleep(5)
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)
