import streamlit as st
import pandas as pd
import preprocessor, helper
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

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
    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]
    
    st.title("Top Statistics")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)
    
    nation_over_time = helper.data_over_time(df, 'region', "No. of Countries")
    st.title("Participating Nations over the years")
    fig = px.line(nation_over_time, x = 'Edition', y = 'No. of Countries')
    st.plotly_chart(fig)
    
    event_over_time = helper.data_over_time(df, 'Event', "No. of Events")
    st.title("Events over the years")
    fig = px.line(event_over_time, x = 'Edition', y = 'No. of Events')
    st.plotly_chart(fig)
    
    athlete_over_time = helper.data_over_time(df, 'Name', "No. of Athletes")
    st.title("Athletes over the years")
    fig = px.line(athlete_over_time, x = 'Edition', y = 'No. of Athletes')
    st.plotly_chart(fig)
    
    st.title('No. of Events over time(Every Sport)')
    fig, ax = plt.subplots(figsize=(20, 20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns= 'Year', values='Event', aggfunc='count').fillna(0).astype('int'),  annot=True)
    st.pyplot(fig)
    
    st.title("Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    
    selected_sport = st.selectbox('Select a Sport', sport_list)
    x= helper.most_successful(df, selected_sport)
    st.table(x)