import streamlit as st
import nasa_api as api
import pandas as pd

apod = api.get_apod()

st.title(apod['title'])
st.image(apod['image'], caption=apod['copyright'])
st.text(apod['description'])



#print(apod)