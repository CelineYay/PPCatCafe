import streamlit as st
from pyngrok import ngrok
import ppccGlobals as ppc

st.title("Member Signup\n")

new_username = st.text_input("Username", key="signup_username")
new_password = st.text_input("Password", type="password", key="signup_password")
if st.button("signup", key="signup_button"):
    if new_username not in ppc.existing_members:
        #dict of existing members updated in signup and login pages
        ppc.existing_members[new_username] = ppc.Member(username = str(new_username),password=str(new_password))
        #class object curr_user updated to the newly signed up user
        ppc.curr_user = ppc.existing_members[new_username]
        st.success("Signup successful! +5 points")
        #sets adds the points to object class member
        ppc.curr_user.add_points(5)
        st.write(f"Welcome, {new_username}! You have {ppc.curr_user.__show_points__()} points.")
    else:
        st.error("Username already exists. Please login instead!")
if st.button("login", key="gologin_button"):
            st.switch_page("pages/_login.py")