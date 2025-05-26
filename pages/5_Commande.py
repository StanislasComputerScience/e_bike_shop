import streamlit as st
import controller.controller as control


def display() -> None:
    """Main display"""
    try:
        # Request to the DB
        if "id_user" in st.session_state:
            id_shoppingcart = control.user_open_shopping_cart_id(
                st.session_state["id_user"]
            )
            if id_shoppingcart:
                shopping_cart = control.user_shopping_cart(id_shoppingcart)
            else:
                shopping_cart = list()
            user_info = control.get_all_info_user(st.session_state["id_user"])
        else:
            shopping_cart = list()
            user_info = list()

        # Display the title
        st.title("Votre commande")

        # Display User Information
        display_table_header(user_info)

        # Display the shopping cart as a table
        column_widths = [1, 2, 2, 1, 1, 1]
        display_table_sub_header(column_widths)

        total_price_ET, total_price_IT = 0, 0
        for command_line in shopping_cart:
            add_prices = display_table_line(column_widths, command_line)
            total_price_ET += add_prices[0]
            total_price_IT += add_prices[1]

        # Display the total price
        column_widths = [4, 2]
        display_order_and_total(column_widths, total_price_ET, total_price_IT)

        # Display address choice
        display_address_choice()

    except:
        st.text("Il est nécessaire de vous connecter pour voir votre commande.")


def display_table_header(user_info: list[dict]) -> None:
    """Display header who contain user information

    Args:
        user_info (list[dict]): user information
    """
    st.text(f"Utilisateur: {user_info["name"]} {user_info["firstname"]}")
    st.text(f"Mail: {user_info["email"]}")
    st.text(f"Téléphone: {user_info["phone"]}")


def display_table_sub_header(column_widths: list[int]) -> None:
    """Display the shopping cart table header

    Args:
        column_widths (list[int]): Relative widths for each column
    """
    st.subheader("Panier :")

    # Dividing the field into columns
    (
        col_image,
        col_name,
        col_quantity,
        col_price_ET,
        col_total_price_ET,
        col_total_price_IT,
    ) = st.columns(column_widths)

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
    with col_price_ET:
        st.text("Prix HT unitaire")

    # Column command line price
    with col_total_price_ET:
        st.text("Prix HT")

    # Column command line price
    with col_total_price_IT:
        st.text("Prix TTC")


def display_table_line(column_widths: list[int], command_line: dict) -> tuple[int, int]:
    """Display a command line of the shopping cart.

    Args:
        column_widths (list[int]): Relative widths of the columns
        command_line (dict): Command line information

    Returns:
        int: Total cost for this command line
    """
    # Dividing the field into columns
    (
        col_image,
        col_name,
        col_quantity,
        col_price_ET,
        col_total_price_ET,
        col_total_price_IT,
    ) = st.columns(column_widths, vertical_alignment="center")

    # Column image
    with col_image:
        st.image(command_line["image_path"], width=50)

    # Column product name
    with col_name:
        st.text(command_line["product_name"])

    # Column quantity in the shopping cart
    with col_quantity:
        st.text(command_line["quantity"])

    # Column product price ET
    with col_price_ET:
        st.text(f"{command_line["price_ET"]:10.2f} €")

    # Column command line price ET
    with col_total_price_ET:
        total_price_ET = command_line["price_ET"] * command_line["quantity"]
        st.text(f"{total_price_ET:10.2f} €")

    # Column command line price IT
    with col_total_price_IT:
        total_price_IT = total_price_ET * (1 + command_line["rate_vat"])
        st.text(f"{total_price_IT:10.2f} €")

    return total_price_ET, total_price_IT


def display_order_and_total(
    column_widths: list[int], total_price_ET: int, total_price_IT: int
):
    """Display the total cost of the shopping cart

    Args:
        column_widths (list[int]): Relative widths of the columns
        total_price_ET (int): Total cost of the shopping cart (excl. taxes)
        total_price_IT (int): Total cost of the shopping cart (incl. taxes)
    """
    # Dividing the field into columns
    empty_col, col_total_price = st.columns(column_widths, vertical_alignment="bottom")

    with col_total_price:
        st.text(
            f"Prix total HT: {total_price_ET:10.2f} €\nPrix total TTC: {total_price_IT:10.2f} €"
        )


def display_address_choice() -> None:
    """Display in streamlit all address to permit to the user the choice"""
    user_address = control.get_user_address(st.session_state["id_user"])

    options = [f"{rue}, {ville}" for rue, ville in user_address]

    with st.expander("Choisissez une adresse de livraison"):
        choix_str = st.radio("", options)

    # Trouver l'index correspondant
    index_choix = options.index(choix_str)

    # Récupérer la rue et la ville depuis la liste originale
    rue_choisie, ville_choisie = user_address[index_choix]

    if st.button("order", icon="🚴") and index_choix is not None:
        control.create_invoice(st.session_state["id_user"])
        st.write("Commande effectué")


if __name__ == "__main__":
    display()
