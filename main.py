import streamlit as st
import sklearn
import pickle
import warnings

warnings.filterwarnings("ignore")

model = pickle.load(open('model.pkl', 'rb'))

def results(most,temp):
    val = model.predict([[most,temp]])
    return val

st.set_page_config(layout="wide",)

st.title("Automatic Irrigation system")

col1, col2 = st.columns([1,1],gap="small")


with col1:
    moist = st.text_input(label="Enter moisture value",value=30)

with col2:
    temp = st.text_input(label="Enter Temperature in 'C",value=20)

result = results(moist,temp)

st.metric(label="Result",value=result[0])

from PIL import Image

image = Image.open('rain.jpg')

st.image(image, caption='Water pump')