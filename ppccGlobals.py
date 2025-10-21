import streamlit as st
from pyngrok import ngrok
curr_user = ""
payed = False
ismember = False

##### Membership here #####
class Member:
    #class for every member account object

    def __init__(self, username: str, password: str, points: float = 0):
        self.username = username
        self.password = password
        self.points = points

    def get_username(self) -> str:
        return self.username

    def check_password(self, input_password: str) -> bool:
        #verify if the provided password correct
        return self.password == input_password

    def add_points(self, amount: float) -> None:
        #add points to the member’s account
        self.points += amount

    def redeem_points(self, amount: float) -> bool:
        #redeem points if the user has enough
        if self.points >= amount:
            self.points -= amount
            return True #redeemed successfully
        return False #sad life too bad
    
    def edit_points(self, new_points: float) -> None:
        self.points = new_points

    def get_points(self) -> float:
        return self.points
    
    def __show_points__(self) -> str:
        return str(self.points)


##### Data here #####
#existing_member = (unique_username)
existing_members = {}
#voucher_codes = {voucher_key_name: [type, description, value]}}
voucher_codes = {
    "PPCCthanksyou25": ["discount","Get 10% off your next visit" ,0.1], 
    "Congrats100customer": ["free", "get $10 off, gst not included", 10.00]
    }
#menu = {category: {item_name: [price, image.png, custom_type]}}
menu = {
    "home": {"Entry":[10.00, ""]},
    "drinks": {"Jasmine Milk tea":[5.50, "drinks_jasmineMilkTea.png", "Toppings"], "Bubble Milk tea":[6.00, "drinks_bubblemilktea.png", "Toppings"], "Matcha Latte":[5.00, "drinks_matchalatte.png","Temperature"], "Mango Milkshake":[5.5, "drinks_mangomilkshake.png"]}, 
    "foods": {"Waffle":[5.50, "foods_waffle.png","Ice Cream"],"Cake":[5.50, "foods_cake.png"]}, 
    "cat treats": {"Donate":[1.00, ""], "Cat Treat":[2.00, "catTreat_treat.jpg"], "Cat Toy":[1.00, "catTreat_toy.png"]},
    }
#custom_drinks = {custom_type: {type_option: [price]}}
custom_drinks = {
    "Toppings": {"None":[0.00],"Bubbles":[0.50], "Pudding":[0.50]},
    "Temperature": {"Hot":[0.00], "Cold":[0.00]},
    "Ice Cream": {"Chocolate":[1.00],"Vanilla":[1.00],"Strawberry":[1.00],"Durian":[1.00]}
    }
#user_cart = {item_name: [quantity, category, custom_option]}
user_cart = {}
#add products into cart


##### Functions here #####

def get_img_path(category, menu_category_item):
    if menu[category][menu_category_item][1] == "":
        return "Images\default.jpg"
    else:
        return f"Images\{menu[category][menu_category_item][1]}"

def single_item_display(category, menu_category_item):
    img_path = get_img_path(category, menu_category_item)
    st.subheader(menu_category_item)
    st.image(img_path, width="stretch")
    st.write("    $" + str(menu[category][menu_category_item][0]))
    #check if customisation avalible
    if len(menu[category][menu_category_item]) > 2:
        #gets the type of customisation options
        custom_type = menu[category][menu_category_item][2] #toppings value like temperature
        custom_options = list(custom_drinks.get(custom_type, {}).keys()) #find options clickable
        custom_price = list(custom_drinks.get(custom_type, {}).values()) #find price
        #st.radio(label, options, index=0, format_func=special_internal_function, key=None
        customed = st.radio(
            custom_type, 
            [f"{opt} (+${custom_drinks[custom_type][opt][0]:.2f})" #show price to 2dp
             if custom_drinks[custom_type][opt][0] > 0 else opt #if price >0 show price else just show option
             for opt in custom_options],
             index=0, #default option selected
             key=category+menu_category_item+custom_type
        )
    #quanity selector
    quantity = st.number_input("Quantity", min_value=0, max_value=20, value=0, key=category+menu_category_item)
    if quantity > 0:
        if len(menu[category][menu_category_item]) > 2:
            user_cart[menu_category_item] = [category, quantity, custom_type, customed]
        else:
            user_cart[menu_category_item] = [category, quantity]
    return