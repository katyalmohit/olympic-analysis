import streamlit as st
import pandas as pd
import preprocessor, helper

df = preprocessor.preprocess()

st.sidebar.radio(
    "Select an option",
    ("Medal Tally", "Overall Analysis", "Country-wise Analysis", "Athlete wise Analysis")
)

st.dataframe(df)

if user_menu == 'Medal Tally':
    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)