import streamlit as st
import ngrok as ng
import ppccGlobals as ppc

##### Data here #####

#voucher_codes = {voucher_key_name: {type: [description, value]}}
voucher_codes = {"PPCCthanksyou25": {"discount": ["Get 10'%' off your next visit" ,0.1]}, "Congrats100customer":{"free": ["1 free slice of cake", "Cake"]}, "SUTDCTDGOTU":{"free": ["free entry to the cat cafe", "Entry"]}}
# cats = {cat_name: [description, image.png]}
cats = {""}
# menu = {category: {item_name: [price, image.png, additionalInfomation]}}
menu = {
    "home": {"Entry":[10.00, ""]},
    "drinks": {"Jasmine Milk tea":[5.50, "drinks_jasmineMilkTea.png", "topping"], "Bubble Milk tea":[6.00, "drinks_bubblemliktea.jpg", "topping"], "Matcha Latte":[5.00, "drinks_matchalatte.png","temperature"], "Mango Milkshake":[5.5, "drinks_mangomilkshake.png"]}, 
    "foods": {"Waffle":[5.50, "foods_waffle.png"],"Cake":[5.50, "foods_cake.png"]}, 
    "cat treats": {"Donate":[1.00, ""], "Cat Treat":[2.00, "catTreat_treat.png"], "Cat Toy":[1.00, "catTreat_toy.png"]},
    }
#custom_drinks = 
custom_drinks = {
    "toppings": {"Bubbles":[0.50, ""], "Pudding":[0.50, ""]},
    "temperature": {"Hot":[0.00, ""], "Cold":[0.00, ""]}
    }
# user_cart = {item_name: [quantity]}
user_cart = {}

##### Functions here #####

def get_img_path(category, menu_category_item):
    if menu[category][menu_category_item][1] == "":
        return "Images\default.jpg"
    else:
        #TODO add the rest of the item images
        if menu_category_item != "Bubble Milk tea":
            return "Images\default.jpg"
        return f"Images\{menu[category][menu_category_item][1]}"

def single_item_display(category, menu_category_item):
    img_path = get_img_path(category, menu_category_item)
    st.subheader(menu_category_item)
    st.image(img_path, width="stretch")
    st.write("    $" + str(menu[category][menu_category_item][0]))
    if len(menu[category][menu_category_item]) > 2:
        st.write("*" + menu[category][menu_category_item][2] + "*")
    quantity = st.number_input("Quantity", min_value=0, max_value=10, value=0, key=category+menu_category_item)
    return quantity