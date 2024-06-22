import streamlit as st
import pandas as pd
import preprocessor, helper

df = pd.read_csv('../dataset/athlete_events.csv')
region_df = pd.read_csv('../dataset/noc_regions.csv')

df = preprocessor.preprocess(df, region_df)

st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio(
    "Select an option",
    ("Medal Tally", "Overall Analysis", "Country-wise Analysis", "Athlete wise Analysis")
)

# st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header('Medal Tally')
    years, country = helper.country_year_list(df)
    
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select country", country)
    
    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + "'s Overall Tally")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + "'s Tally in " + str(selected_year) + " Olympics")
    st.dataframe(medal_tally)