import streamlit as st
from pyngrok import ngrok
import ppccGlobals as ppc

st.title("PPCatCafe")
st.header("Cat Treats")
for cattreat in ppc.menu["cat treats"]:
    ppc.single_item_display("cat treats", cattreat)