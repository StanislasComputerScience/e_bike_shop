import streamlit as st
import const_values as cv

if cv.BDD_TECHNO == "mongodb":
    import controller_mongod.controller_mongod as control
    import controller_mongod.tools as tool
else:
    import controller.controller as control
    import controller.tools as tool

from bson import ObjectId


# --- function called on radio change ---
def changement_produit():
    st.session_state.c = name_products.index(st.session_state.choix_radio)


# # radio button index initialisation
if "c" not in st.session_state:
    st.session_state.c = 0

# loading list of products and their names for the radio button
(l_products, name_products) = tool.load_products_and_c()

# produit sélectionné
product_selected = l_products[st.session_state.c]

# --- sidebar display ---
st.sidebar.subheader("Fichiers dans 'produits' :")

st.sidebar.radio(
    "Sélectionnez un produit :",
    name_products,
    index=st.session_state.c,
    key="choix_radio",
    on_change=changement_produit,
)

# --- page header ---

# Button navigation
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    if st.button("Précédent"):
        st.session_state.c = (st.session_state.c - 1) % len(l_products)
        st.rerun()

with col2:
    st.markdown(
        f"""
        <div style='
            text-align:center;
            font-weight:bold;
            font-size:32px;
            margin-bottom:10px;
        '>
            {product_selected["name"]}
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    if st.button("Suivant"):
        st.session_state.c = (st.session_state.c + 1) % len(l_products)
        st.rerun()

# progress bar
st.progress((st.session_state.c + 1) / len(l_products))

# --- Image and shopping cart button ---

# affichage principal
st.subheader("Affichage du produit sélectionné :")

colImage, colToOrder = st.columns([3, 1])

with colImage:
    st.image(product_selected["image_path"], width=300)


with colToOrder:
    shopping_cart_id = None
    submit_buy = st.button("Ajouter au panier")
    if submit_buy:
        try:
            if not isinstance(st.session_state["id_user"], ObjectId):
                id_product = product_selected["id_prod"]
            else:
                id_product = l_products[st.session_state.c]["_id"]
        except:
            st.error("Vous devez vous connecter pour ajouter à votre panier ❌")

        if "id_user" in st.session_state:
            id_user = st.session_state["id_user"]
            shopping_cart_id = control.user_open_shopping_cart_id(id_user)

            if shopping_cart_id:
                if not control.is_command_line_exist(shopping_cart_id, id_product):
                    vat = (
                        product_selected["price_it"] - product_selected["price_ET"]
                    ) / product_selected["price_ET"]
                    control.add_new_command_line(
                        id_product,
                        shopping_cart_id,
                        product_selected["price_ET"],
                        vat,
                    )
                    st.switch_page("pages/4_Panier.py")
                else:
                    st.error("Le produit est déjà dans le panier ❌")
            else:
                control.add_new_shoppingcart(id_user)
                shopping_cart_id = control.user_open_shopping_cart_id(id_user)
                if shopping_cart_id:
                    vat = (
                        product_selected["price_it"] - product_selected["price_ET"]
                    ) / product_selected["price_ET"]
                    control.add_new_command_line(
                        id_product,
                        shopping_cart_id,
                        product_selected["price_ET"],
                        vat,
                    )
                    st.switch_page("pages/4_Panier.py")
                else:
                    raise ValueError("shopping_cart_id should exist...")

# --- page main body ---

st.write(product_selected["description"])
st.write(product_selected["tech_specification"])

val_et = round(product_selected["price_ET"], 2)
# st.write(f"Prix TCC: {val_et:.2f} €")

val_it = round(product_selected["price_it"], 2)
# st.write(f"Prix TCC: {val_it:.2f} €")

st.markdown(
    f"""
<b style="font-size:20px">🧾  Prix HT : {val_et} €</b><br>
<b style="font-size:20px">💰  Prix TTC : {val_it} €</b>
""",
    unsafe_allow_html=True,
)
