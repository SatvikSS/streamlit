import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('startup_cleaned.csv')
st.sidebar.title('Startup Fundings')

def load_inverstor_details(investor):
    st.title(investor)
    last5_df = df[df['Investors Name'].str.contains(investor)].head()[['Date', 'Startup', 'Vertical', 'City  Location', 'Amount']]
    st.subheader('Most recent Investments')
    st.dataframe(last5_df)

    big_series = df[df['Investors Name'].str.contains(investor)].groupby('Startup')['Amount'].sum().sort_values(ascending=False).head()
    st.subheader('Biggest Investments')
    fig, ax = plt.subplots()
    ax.bar(big_series.index,big_series.values)
    st.pyplot(fig)

option = st.sidebar.selectbox('Categories',['Overall Analysis','StartUp','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp',sorted(df['Startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Analysis')
    st.title('StartUp Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select Investor',sorted(set(df['Investors Name'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Analysis')
    if btn2:
        load_inverstor_details(selected_investor)
    else:
        st.title('Investor Analysis')