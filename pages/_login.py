import streamlit as st
from pyngrok import ngrok
import ppccGlobals as ppc

st.title("Member Login")

login_user = st.text_input("Username", key="login_username")
login_password = st.text_input("Password", type="password", key="login_password")
if st.button("login", key="login_button"):
    if login_user not in ppc.existing_members:
        st.error("Username does not exist. Please sign up first!")
    else:
        ppc.curr_user = ppc.existing_members[login_user]
        if ppc.curr_user.check_password(str(login_password)):
            st.success("Login successful!")
            ppc.curr_user.add_points(5)
            ppc.ismember = True
            st.switch_page("pages/1_meet_the_cats.py")
        else:
            st.error("Incorrect password. Please try again!")

st.write("Don't have an account? Please sign up first!")
if st.button("Signup", key="signup_button"):
    st.switch_page("pages/_signup.py")
