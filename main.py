import streamlit as st

import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

#st.dataframe(df)  # Same as st.write(df)
st.dataframe(df.style.highlight_max(axis=0))
