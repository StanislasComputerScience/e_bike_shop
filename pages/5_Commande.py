import streamlit as st
import controller.controller as control

ecommerce_db_name = "ecommerce_database"

st.title("Votre commande")

user_info = control.get_all_info_user(ecommerce_db_name, st.session_state["id_user"])
st.text(f"Utilisateur: {user_info["name"]} {user_info["firstname"]}")
st.text(f"Mail: {user_info["email"]}")
st.text(f"Téléphone: {user_info["phone"]}")

st.subheader("Panier :")
