from platform import platform
from sqlite3 import Row
import streamlit as st
import pandas as pd
import json
import altair as alt
import streamlit.components.v1 as cv1

data = open("data/data.json","r")
data_json = json.loads(data.read())




linkedin = open("data/linkedin.txt","r")
linkedin_embed = linkedin.read()

experience = data_json['experience']
languages = data_json['languages'] 
cloud = data_json['clouds']
platforms = data_json['platforms']

st.set_page_config(layout="wide")
st.markdown(f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{width: 20rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{width: 20rem;}}
    </style>
''',unsafe_allow_html=True)
st.title("Carlos D Serrano")
st.markdown("""
###  *Senior Solutions Architect @ Snowflake*

-----""")
st.subheader('')
with st.sidebar:
    st.subheader('Instagram.com/sqlinsights')
    cv1.html(linkedin_embed, height=300, width=600)
    st.json(experience)


wp,ln,ig,yt = st.columns(4)
st.markdown("---")
with wp:
    st.image("resources/qr-code-14.png")
with ln:
    st.image("resources/qr-code-13.png")
with ig:
    st.image("resources/qr-code-11.png")
with yt:
    st.image("resources/qr-code-12.png")


lang = pd.DataFrame.from_dict(data=languages).transpose()
lang.reset_index(inplace=True)
lang.rename(columns={ 0: 'Years'}, inplace=True)
lang.rename(columns={ 'index': 'Language'}, inplace=True)

clouds = pd.DataFrame.from_dict(data=cloud).transpose()
clouds.reset_index(inplace=True)
clouds.rename(columns={ 0: 'Years'}, inplace=True)
clouds.rename(columns={ 'index': 'Cloud'}, inplace=True)

pltfrm = pd.DataFrame.from_dict(data=platforms).transpose()
pltfrm.reset_index(inplace=True)
pltfrm.rename(columns={ 0: 'Years'}, inplace=True)
pltfrm.rename(columns={ 'index': 'Platform'}, inplace=True)


col1, col2 = st.columns(2)

with col1:
    st.header("Language Experience")
    ##Languages
    
    c = alt.Chart(lang).mark_bar().encode(
        x='Language', y='Years', color='Language')
    st.altair_chart(c, use_container_width=True)


with col2:
    st.header("Platforms Experience")
    ##Platforms
    plats = alt.Chart(pltfrm).mark_bar().encode(
        x='Platform', y='Years', color='Platform')
    st.altair_chart(plats, use_container_width=True)


st.write("""## Cloud Experience
""")
cloud_chart = alt.Chart(clouds).mark_bar().encode(
    x='Cloud', y='Years', color='Cloud')
st.altair_chart(cloud_chart, use_container_width=True)
