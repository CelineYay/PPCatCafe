import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

st.title("PPCatCafe")
st.header("Checkout")

if curr_user != None:
    st.write(f"Welcome back, f{curr_user} member you have f{curr_user}!")

