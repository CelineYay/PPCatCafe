import streamlit as st
from pyngrok import ngrok
import ppccGlobals as ppc

ngrok.set_auth_token("") #add your own auth token here
# Start ngrok tunnel to expose the Streamlit server
ngrok_tunnel = ngrok.connect(addr='5011', proto='http', bind_tls=True) #5011
# Print the URL of the ngrok tunnel
print(' * Tunnel URL:', ngrok_tunnel.public_url)
# to get ngrok to run, use "streamlit run PPCatCafe.py --server.port 5011"


st.title("Welcome to our Cafe! 🐱☕️🍰")
st.write("Please pay for entry to hangout with the cats")
st.write("Or just enjoy our drinks and food!")
st.write("All cats are up for adoption! 🐾\n")
st.image("Images/icon.jpg")


st.write("\n\ncontinue as:")
if st.button("Member", key="member_button"):
    st.switch_page("pages/_login.py")
if st.button("Guest", key="mtc_button"):
    st.switch_page("pages/1_meet_the_cats.py")