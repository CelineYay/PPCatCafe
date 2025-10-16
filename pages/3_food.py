import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

st.title("PPCatCafe")
for food in ppc.menu["foods"]:
    ppc.single_item_display("foods", food)