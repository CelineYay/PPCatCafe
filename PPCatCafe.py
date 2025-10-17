import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

st.title("Welcome to our Cafe! 🐱☕️🍰")
st.write("Please pay for entry to hangout with the cats")
st.write("Or just enjoy our drinks and food!")
st.write("All cats are up for adoption! 🐾\n")


st.write("\n\ncontinue as:")
if st.button("Member", key="member_button"):
    st.switch_page("pages/_login.py")
if st.button("Guest", key="mtc_button"):
    st.switch_page("pages/1_meet_the_cats.py")