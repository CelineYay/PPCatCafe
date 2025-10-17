import streamlit as st
from pyngrok import ngrok
import ppccGlobals as ppc

total = 0
voucher = False

st.title("PPCatCafe")
st.header("Checkout")

if ppc.payed:
    st.switch_page("pages/done.py")

for item in ppc.user_cart:
    quantity = ppc.user_cart[item][1]
    st.write(f"{item}  x {quantity} (+${ppc.menu[ppc.user_cart[item][0]][item][0] * quantity:.2f})")
    total+= ppc.menu[(ppc.user_cart[item][0])][item][0] * quantity
    if len(ppc.user_cart[item]) >= 4:
        st.write(f"** {ppc.user_cart[item][3]}")
        custom_type = ppc.user_cart[item][2]
        custom_choice = ppc.user_cart[item][3].split(' ')[0]
        total += ppc.custom_drinks[custom_type][custom_choice][0]

st.write("\n\n")

st.write("Vouchers cannot be stacked")
user_voucher = st.text_input("Enter voucher code: ", key="voucher_input")
if user_voucher in ppc.voucher_codes:
    st.success(f"Valid Voucher Code! {ppc.voucher_codes[user_voucher][1]}")
    voucher = True

if voucher:
    if ppc.voucher_codes[user_voucher][0] == "discount":
        total = total * (1 - ppc.voucher_codes[user_voucher][2])
    elif ppc.voucher_codes[user_voucher][0] == "free":
        total = total - ppc.voucher_codes[user_voucher][2]

if st.button("apply", key="apply_button"):
    if total < 0:
        total = 0.00
    if ppc.ismember:
        ppc.curr_user.add_points(total)
        points = ppc.curr_user.get_points()
        st.success(f"Hello, {ppc.curr_user.get_username()}, you have {points}.")
        total = total - (points // 10)
        ppc.curr_user.edit_points(points % 10)
        st.write(f"offset ${points // 10}, remaining points {points % 10}")


    st.write("Gst (9%)")
    total = total*1.09
    st.header(f"** Total: ${total:.2f} **")

if st.button("pay", key="pay_button"):
    ppc.payed = True
    st.switch_page("pages/done.py")