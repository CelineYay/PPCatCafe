import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

if ppc.ismember:
    st.success(f"Welcome back, {ppc.curr_user.get_username()}! You now have {ppc.curr_user.__show_points__()} points.")
ppc.single_item_display("home", "Entry")

#cats = {cat_name: [description, image.png]}
cats = {
    "Garry": ["Our best boy tuxedo cat with a unique mark.", "Garry_photo.jpg"],
    "Rui": ["Female Shorthaired Calico that loves to eat too fast", "Rui_photo.jpg"],
    "Lembu": ["7 year old male rescued from the streets", "Lembu_photo.jpg"],
    "Chiko": ["Furry Bengal cat! :D", "Chiko_photo.jpg"],
    "Uni": ["The gentlemenest of gentlemen.", "Uni_photo.jpg"]
}

for cat in cats:
    st.header(cat)
    st.write(cats[cat][0])
    st.image(f"Images/{cats[cat][1]}")



