import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

if ppc.ismember:
    st.success(f"Welcome back, {ppc.curr_user.get_username()}! You now have {ppc.curr_user.__show_points__()} points.")
ppc.single_item_display("home", "Entry")



