import streamlit as st
import random
import string
import pyperclip

#========================================FUNCTION========================================
def pwgen (lenght):
    characters = string.ascii_letters + string.digits + string.digits
    password = ''.join(random.choice(characters) for i in range(lenght))
    return password

#========================================RENDER==========================================
st.set_page_config(page_title="Password Generator",page_icon="assets/icon.png", layout= "centered")

st.image("assets/images.png")
st.header("Password Generator")
st.subheader("Generate a strong password to protect your accounts.")
st.markdown("**Enter the desired length of the password:**")

lenght = st.number_input(min_value=0,
                        max_value=64,
                        value=1,
                        step=1,
                        label="Max value: 64",
                        placeholder="Password Lenght",
                        help="Enter a number greater than 0",
                        format="%d")

genbutton = st.button(label="Generate")

if genbutton:

    try:
        if lenght<=0 or lenght>64:
            st.warning("Enter a valid number for the length.")
        else:
            password=pwgen(lenght)
            pyperclip.copy(password)
            st.success(f"Generrated Password: **{password}**")
            st.success("Password copied to clipboard")
    except ValueError:
        st.warning("Error")