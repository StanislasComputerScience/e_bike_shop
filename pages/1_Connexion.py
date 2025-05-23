import streamlit as st
import controller.controller as control
import bcrypt

ecommerce_db_name = "ecommerce_database"

st.title("Connexion")

# Formulary here
st.write("Veuillez entrer vos identifiants pour vous connecter.")

with st.form("login_form"):
    email = st.text_input("📧 Insérer votre email")
    password = st.text_input("🔑 Insérer votre mot de passe", type="password")
    col_coo, space, col_deco = st.columns([1, 3, 1])
    with col_coo:
        submit_coo = st.form_submit_button("Se connecter")
    with col_deco:
        submit_dec = st.form_submit_button("Se déconnecter")

if submit_coo:
    try:
        user_info = control.get_user_info(ecommerce_db_name, email)
        bcrypt.checkpw(password.encode(), user_info[0]["password"].encode())
        st.session_state["id_user"] = user_info[0]["id_user"]
        control.connect_user(ecommerce_db_name, user_info[0]["id_user"])
        st.success("Connexion réussie ✅")
    except:
        st.error("Identifiants incorrects ❌")

if submit_coo:
    try:
        pass
    except:
        pass
