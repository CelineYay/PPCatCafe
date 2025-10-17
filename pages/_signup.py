import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

st.title("Member Login")

new_username = st.text_input("Username", key="signup_username")
new_password = st.text_input("Password", type="password", key="signup_password")
if st.button("signup", key="signup_button"):
    if new_username not in ppc.existing_members:
        ppc.existing_members.add(new_username)
        curr_user = ppc.Member(password="1234")
        st.success("Signup successful! +5 points")
        curr_user.add_points(5)
        st.write(f"Welcome, f{curr_user} member you have f{curr_user.__show_points__}!")
    else:
        st.error("Username already exists. Please login instead!")