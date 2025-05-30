import streamlit as st

# import controller.controller as control
import controller_mongod.controller_mongod as controlmdb
import bcrypt


def display() -> None:
    """Main display"""
    st.title("Connexion")

    # Formulary here
    st.write("Veuillez entrer vos identifiants pour vous connecter.")

    with st.form("login_form"):
        email = st.text_input("📧 Insérer votre email")
        password = st.text_input("🔑 Insérer votre mot de passe", type="password")
        col_coo, space, col_disc = st.columns([1, 3, 1])
        with col_coo:
            submit_coo = st.form_submit_button("Se connecter")
        with col_disc:
            submit_disc = st.form_submit_button("Se déconnecter")

    if submit_coo:
        try:
            user_info = controlmdb.get_user_info_connect(email)
            bcrypt.checkpw(password.encode(), user_info[0]["password"].encode())
            st.session_state["id_user"] = user_info[0]["id_user"]
            controlmdb.connect_user(user_info[0]["id_user"])
            st.success("Connexion réussie ✅")
        except:
            st.error("Identifiants incorrects ❌")

    if submit_disc:
        try:
            controlmdb.disconnect_user(st.session_state.get("id_user"))
            st.session_state.pop("id_user")
            st.success("Déconnexion réussie ✅")
        except:
            st.error("Vous êtes déjà déconnectés ❌")


if __name__ == "__main__":
    display()
