import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

st.title("PPCatCafe")
st.header("Checkout")
total = 0

for item in ppc.user_cart:
    '''
    st.write(item)
    st.write(ppc.user_cart[item])
    '''
    st.write(f"{item}  x {ppc.user_cart[item][1]}")
    total+= ppc.menu[(ppc.user_cart[item][0])][item][0]
    if len(ppc.user_cart[item])>=3:
        st.write(f"    {item[3]}")
        total+= ppc.custom_drinks[(item[2])][(item[3]).split(' ')[0]]