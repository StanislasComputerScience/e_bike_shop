import streamlit as st
import os


def display():

    # TEMPORARY: create a fake dictionnary for having a first version
    folder = "./assets/produits/"
    command_lines = []

    for idx, file in enumerate(os.listdir(folder)):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            command_lines.append(
                {
                    "nom": f"Produit_{idx}",
                    "quantité": idx,
                    "chemin_image": file_path,
                    "prix": idx * 100,
                }
            )

    st.subheader("Panier")

    column_widths = [1, 3, 3, 1, 1]
    display_table_header(column_widths)
    total_price = 0
    for command_line in command_lines:
        total_price += display_table_line(column_widths, command_line)

    column_widths = [4, 2, 1]
    display_order_and_total(column_widths, total_price)


def display_table_header(column_widths: list[int]):
    # Dividing the page into columns
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
    # Dividing the page into columns
    col_image, col_name, col_quantity, col_price, col_total_price = st.columns(
        column_widths, vertical_alignment="center"
    )

    # Column image
    with col_image:
        st.image(command_line["chemin_image"], width=50)

    # Column product name
    with col_name:
        st.text(command_line["nom"])

    # Column quantity in the shopping cart
    with col_quantity:
        st.number_input(
            command_line["nom"] + "_quantity",
            min_value=0,
            max_value=9999,
            value=command_line["quantité"],
            step=1,
            label_visibility="collapsed",
        )

    # Column product price
    with col_price:
        st.text(str(command_line["prix"]) + " €")

    # Column command line price
    with col_total_price:
        st.text(str(command_line["prix"] * command_line["quantité"]) + " €")

    return command_line["prix"] * command_line["quantité"]


def display_order_and_total(column_widths: list[int], total_price: int):
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
