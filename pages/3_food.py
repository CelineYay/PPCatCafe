import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

st.title("PPCatCafe")
st.header("Human Food")
for food in ppc.menu["foods"]:
    ppc.single_item_display("foods", food)