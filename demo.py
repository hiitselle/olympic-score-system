import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go
import mdurl
import streamlit as st
import pandas as pd
from  streamlit_autorefresh import st_autorefresh
st.set_page_config(page_title="Olympic Selection Stats", layout="wide")
st_autorefresh(interval=3000)#in ms



def ch_bg_to_green():
 st.balloons()

 st.markdown(
    """
    <style>
    div[data-testid="stAppViewContainer"] {
           position: absolute;
           background: palegreen;
           color: rgb(49, 51, 63);
           inset: 0px;
           overflow: hidden;
    }
    header[data-testid="stHeader"] {
               position: fixed;
               top: 0px;
               left: 0px;
               right: 0px;
               height: 2.875rem;
               background: palegreen;
               outline: none;
               z-index: 999990;
               display: block;
    }   
   </style>
    """,
    unsafe_allow_html=True
 )

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.freepik.com/free-vector/hand-painted-watercolor-pastel-sky-background_13223496.htm#query=background&position=3&from_view=keyword&track=sph");
    }
   </style>
    """,
    unsafe_allow_html=True
)

st.header(":violet[Laval Stats]")

with st.sidebar:
    genderSel = st.selectbox(
        "Select gender",
        ("Male Semis", "Female Semis" ,"Male Final" ,"Female Finals")
    )

#@st.cache_data(ttl=60)
def load_data(sheets_url):
    return pd.read_csv(sheets_url, dtype=str)

if(genderSel=="Male Semis"):
    df = load_data("https://docs.google.com/spreadsheets/d/12i_7HsoRs74S0FtzN04Uu1WZeToU6AoyOidHAL6WcGE/export?format=csv&gid=1473230761")
 
elif(genderSel=="Female Semis"):
    df = load_data("https://docs.google.com/spreadsheets/d/12i_7HsoRs74S0FtzN04Uu1WZeToU6AoyOidHAL6WcGE/export?format=csv&gid=1802658245")
 
elif(genderSel=="Male Final"):
    df = load_data("https://docs.google.com/spreadsheets/d/12i_7HsoRs74S0FtzN04Uu1WZeToU6AoyOidHAL6WcGE/export?format=csv&gid=28593922")    
    
else:
    df = load_data("https://docs.google.com/spreadsheets/d/12i_7HsoRs74S0FtzN04Uu1WZeToU6AoyOidHAL6WcGE/export?format=csv&gid=919701499")
df = df.astype(str)

#st.dataframe(data=df, use_container_width=True)
df_metric = df.copy()
df_metric['TotalScore'] = df_metric['TotalScore'].astype('float')
df_metric = df_metric.sort_values(by='TotalScore', ascending=True)
df_metric = df_metric.tail(8)
df_metric['color'] = ''
for z in range(len(df_metric)):
    if(df_metric['Qualified'].iloc[z] == "Qualified for Finals :)") or (df_metric['Qualified'].iloc[z] == "Podium Garentee!!!!") :
        df_metric['color'].iloc[z] = 'green'
        #st.write(df_metric['color'].iloc[z])
    else:
        df_metric['color'].iloc[z] = 'red'
#st.dataframe(data=df_metric, use_container_width=True)
plot_assym = go.Figure(go.Bar(x=df_metric['TotalScore'], y=df_metric["Name"], orientation='h',text=df_metric['TotalScore'].astype('str'),marker={'color': df_metric['color']}))
st.sidebar.plotly_chart(plot_assym)
with st.expander("Current Leader"):
    
    index = df['Actual Ranking'].idxmin()

    if(df['Worst Case'].iloc[index] == "1"):
        st.success(df['Name'].iloc[index] + " Qualified!")
        ch_bg_to_green()
    else:
        st.error(df['Name'].iloc[index] + " :red[is leading & is Beatable!]")


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

    if(df['Qualified'].iloc[index] == "Qualified for Finals :)") or (df['Qualified'].iloc[index] == "Podium Garentee!!!!") :
        
 
        #st.write(index)
        st.success(df['Name'].iloc[index] + " :green[confirmed qualified]")
        st.markdown(
                    """
                    <style>
    
                    div[data-testid="stExpander"]:nth-of-type(""" + str(index+5) + """) {
                         background: 	palegreen;
                         color: black; # Expander content color
                    }

                    </style>
                    """,
                    unsafe_allow_html=True
                    )
    else:
        #st.write(index)
        
        st.error(df['Name'].iloc[index] + " :red[not qualified]") 
        st.markdown(
                    """
                    <style>
    
                    div[data-testid="stExpander"]:nth-of-type(""" + str(index+5) + """) {
                         background: 	#ffcccb;
                         color: black; # Expander content color
                    }

                    </style>
                    """,
                    unsafe_allow_html=True
                    )
                 
for x in range(len(df)):
    with st.expander(df['Name'].iloc[x]):
        generateInfo(x)

st.write("Made by Elle")



