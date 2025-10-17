import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

st.title("PPCatCafe")
st.header("Drinks\n")
for drink in ppc.menu["drinks"]:
    ppc.single_item_display("drinks", drink)