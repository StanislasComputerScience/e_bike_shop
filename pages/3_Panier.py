import streamlit as st
import os
from controller.controller import user_shopping_cart


def display():
    """Display the page "Panier" in the streamlit app."""

    # Request to the DB
    test_id_user = 2
    shopping_cart = user_shopping_cart("bdd/ecommerce_database", test_id_user)

    # Display the title
    st.header("Panier")

    # Display the shopping cart as a table
    column_widths = [1, 3, 3, 1, 1]
    display_table_header(column_widths)
    total_price = 0
    for command_line in shopping_cart:
        total_price += display_table_line(column_widths, command_line)

    column_widths = [4, 2, 1]

    # Display the order button and the total price
    display_order_and_total(column_widths, total_price)


def display_table_header(column_widths: list[int]):
    """Display the shopping cart table header

    Args:
        column_widths (list[int]): Relative widths for each column
    """
    # Dividing the field into columns
    col_image, col_name, col_quantity, col_price, col_total_price = st.columns(
        column_widths
    )

    # Column image
    with col_image:
        st.text("Image")

    # Column product name
    with col_name:
        st.text("Nom du produit")

    # Column quantity in the shopping cart
    with col_quantity:
        st.text("Quantité")

    # Column product price
    with col_price:
        st.text("Prix unitaire")

    # Column command line price
    with col_total_price:
        st.text("Prix")


def display_table_line(column_widths: list[int], command_line: dict) -> int:
    """Display a command line of the shopping cart.

    Args:
        column_widths (list[int]): Relative widths of the columns
        command_line (dict): The command line information

    Returns:
        int: The total cost for this command line
    """
    # Dividing the field into columns
    col_image, col_name, col_quantity, col_price, col_total_price = st.columns(
        column_widths, vertical_alignment="center"
    )

    # Column image
    with col_image:
        st.image(command_line["image_path"], width=50)

    # Column product name
    with col_name:
        st.text(command_line["product_name"])

    # Column quantity in the shopping cart
    with col_quantity:
        st.number_input(
            command_line["product_name"] + "_quantity",
            min_value=0,
            max_value=9999,
            value=command_line["quantity"],
            step=1,
            label_visibility="collapsed",
        )

    # Column product price
    with col_price:
        st.text(str(command_line["price_ET"]) + " €")

    # Column command line price
    with col_total_price:
        st.text(str(command_line["price_ET"] * command_line["quantity"]) + " €")

    return command_line["price_ET"] * command_line["quantity"]


def display_order_and_total(column_widths: list[int], total_price: int):
    """Display the order button and the total cost of the shopping cart

    Args:
        column_widths (list[int]): Relative widths of the columns
        total_price (int): Total cost of the shopping cart
    """
    # Dividing the field into columns
    empty_col, col_order, col_total_price = st.columns(
        column_widths, vertical_alignment="center"
    )

    with col_order:
        st.button("order", icon="🚴")

    with col_total_price:
        st.text(f"Total: {total_price} €")


if __name__ == "__main__":
    display()
