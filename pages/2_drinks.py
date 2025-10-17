import streamlit as st
from pyngrok import ngrok
import ppccGlobals as ppc

st.title("PPCatCafe")
st.header("Drinks\n")
for drink in ppc.menu["drinks"]:
    ppc.single_item_display("drinks", drink)