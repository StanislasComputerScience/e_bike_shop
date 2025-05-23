import streamlit as st
import controller.controller as control


def display():
    ecommerce_db_name = "ecommerce_database"

    # Request to the DB
    if "id_user" in st.session_state:
        shopping_cart = control.user_shopping_cart(
            ecommerce_db_name, st.session_state["id_user"]
        )
        user_info = control.get_all_info_user(
            ecommerce_db_name, st.session_state["id_user"]
        )
    else:
        shopping_cart = list()
        user_info = list()

    # Display the title
    st.title("Votre commande")

    # Display User Information
    display_table_header(user_info)

    # Display the shopping cart as a table
    column_widths = [1, 2, 2, 1, 1, 1]
    display_table_header(column_widths)

    st.subheader("Panier :")


def display_table_header(user_info: list[dict]) -> None:
    st.text(f"Utilisateur: {user_info["name"]} {user_info["firstname"]}")
    st.text(f"Mail: {user_info["email"]}")
    st.text(f"Téléphone: {user_info["phone"]}")


if __name__ == "__main__":
    display()
