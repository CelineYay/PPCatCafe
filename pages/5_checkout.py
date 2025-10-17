import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

st.title("PPCatCafe")
st.header("Checkout")
total = 0

for item in ppc.user_cart:
    st.write(f"{item}")