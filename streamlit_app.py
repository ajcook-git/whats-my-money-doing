# import altair as alt
# import numpy as np
import datetime
import pandas as pd
# import plotly.express as px
import streamlit as st
import textwrap

"""
# Adam's Financial Dashboard
This is a dashboard for Adam. Yes, I know it's public.
"""

df = pd.read_csv('data/newdata.csv', index_col='Date')

if not all(df.iloc[datetime.datetime.now().month].notna()):
    st.write(textwrap.dedent("""
        **Warning:** it looks like your data is out of date!
    """))

credit_accs = {'Barclaycard', 'NatwestCredit'}
credit_cols = list(credit_accs)
debit_accs = set(df.columns).difference(credit_cols)
debit_cols = list(debit_accs)

debit_df = df[debit_cols]
# debit_df['Total'] = debit_df.transpose().sum()
credit_df = df[credit_cols]
# credit_df['Total'] = credit_df.transpose().sum()

col1, col2 = st.columns(2)
with col1:
    total = debit_df.iloc[datetime.datetime.now().month].sum()
    st.write(f"Total in accounts: £{total:,}")

with col2:
    total = credit_df.iloc[datetime.datetime.now().month].sum()
    st.write(f"Total owed: £{total:,}")

st.write("""
### These lines represent actual cash
Ideally, these will all be going up! 
""")
st.line_chart(debit_df)

st.write("""
### These lines represent credit card debt
Ideally, these will all be going down...
""")
st.line_chart(credit_df)

st.write("""### Here's the raw data I'm reading from
...so you know what I'm working with!
""")
st.dataframe(df)

st.write("#### Well, this is all very easy")