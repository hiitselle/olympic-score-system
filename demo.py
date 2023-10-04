
import mdurl
import streamlit as st
import pandas as pd
from  streamlit_autorefresh import st_autorefresh
st.set_page_config(page_title="Olympic Selection Stats", layout="wide")
st_autorefresh(interval=5000)#in ms



st.header(":blue[Laval Stats]")

with st.sidebar:
    genderSel = st.selectbox(
        "Select gender",
        ("Semis", "Finals")
    )

#@st.cache_data(ttl=60)
def load_data(sheets_url):
    return pd.read_csv(sheets_url, dtype=str)

if(genderSel=="Semis"):
    df = load_data("https://docs.google.com/spreadsheets/d/12i_7HsoRs74S0FtzN04Uu1WZeToU6AoyOidHAL6WcGE/export?format=csv&gid=1473230761")
else:
    df = load_data("https://docs.google.com/spreadsheets/d/12i_7HsoRs74S0FtzN04Uu1WZeToU6AoyOidHAL6WcGE/export?format=csv&gid=919701499")
df = df.astype(str)

#st.dataframe(data=df, use_container_width=True)

with st.expander("Current Leader"):
    
    index = df['Actual Ranking'].idxmin()

    if(df['Worst Case'].iloc[index] == "1"):
        st.write(df['Name'].iloc[index] + ":green[first place]")
        
    else:
        st.write(df['Name'].iloc[index] + " :red[is leading & is Beatable!]")




def generateInfo(index):
    st.write("Current Points: " + df['TotalScore'].iloc[index])
    st.write("Current Position: " + df['Actual Ranking'].iloc[index])
    if(df['Is score complete'].iloc[index] == "1"):
        st.write("Worst Case Position: " + df['Worst Case'].iloc[index])
        st.write("Qualified: " + df['Qualified'].iloc[index])
    else:

        st.write("Points to 1st: " + df['Points to 1st'].iloc[index])
        st.write("Points to 2nd: " + df['Points to 2nd'].iloc[index])
        st.write("Points to 3rd: " + df['Points to 3rd'].iloc[index])

for x in range(len(df)):
    with st.expander(df['Name'].iloc[x]):
        generateInfo(x)

st.write("Made by Elle")

