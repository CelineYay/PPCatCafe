import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

st.title("PPCatCafe")
st.header("Cat Treats\n")
for cattreat in ppc.menu["cat treats"]:
    ppc.single_item_display("cat treats", cattreat)