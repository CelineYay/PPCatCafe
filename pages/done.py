import streamlit as st
from pyngrok import ngrok
import ppccGlobals as ppc

if ppc.payed:
    st.success("Thank you for your purchase!")
    st.image("Images/check.png", "your order will be ready soon!", width="stretch")
    if st.button("new user"):
        ppc.payed = False
        ppc.curr_user = ""
        ppc.user_cart = {}
        ppc.ismember = False
        st.switch_page("PPCatCafe.py")
else:
    st.switch_page("pages/checkout.py")