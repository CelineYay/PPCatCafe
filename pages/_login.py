import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

st.title("Member Login")

login_user = st.text_input("Username", key="login_username")
login_password = st.text_input("Password", type="password", key="login_password")
if st.button("login", key="login_button"):
    if login_user not in ppc.existing_members:
        st.error("Username does not exist. Please sign up first!")
    else:
        curr_user = login_user
        if curr_user.check_password(login_password):
            st.success("Login successful!")
            curr_user.add_points(5)
            st.write(f"Welcome back, f{curr_user} member you have f{curr_user.__show_points__}!")
        else:
            st.error("Incorrect password. Please try again!")

st.write("Don't have an account? Please sign up first!")
if st.button("Signup", key="signup_button"):
    st.switch_page("pages/_signup.py")
