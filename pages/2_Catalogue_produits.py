import os
import streamlit as st
import controller.controller as control
import controller.tools as tool


# --- function called on radio change ---
def changement_produit():
    st.session_state.c = name_products.index(st.session_state.choix_radio)


# # radio button index initialisation
if "c" not in st.session_state:
    st.session_state.c = 0

# loading product

# List of product's name for the radio button
(l_products, name_products) = tool.load_products_and_c()

# --- function called on radio change ---
def changement_produit():
    st.session_state.c = name_products.index(st.session_state.choix_radio)

# --- sidebar display ---
st.sidebar.subheader("Fichiers dans 'produits' :")

st.sidebar.radio(
    "Sélectionnez un produit :",
    name_products,
    index=st.session_state.c,
    key="choix_radio",
    on_change=changement_produit,
)




# Button navigation
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    if st.button("Précédent"):
        st.session_state.c = (st.session_state.c - 1) % len(l_products)

with col2:
    st.markdown(
        f"""
        <div style='
            text-align:center;
            font-weight:bold;
            font-size:32px;
            margin-bottom:10px;
        '>
            Produit n°{st.session_state.c + 1}
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    if st.button("Suivant"):
        st.session_state.c = (st.session_state.c + 1) % len(l_products)

# progress bar
st.progress((st.session_state.c + 1) / len(l_products))

# produit sélectionné
product_selected = l_products[st.session_state.c]

# affichage principal
st.subheader("Affichage du produit sélectionné :")

colImage, colToOrder = st.columns([3, 1])

with colImage:
    st.image(product_selected["image_path"], width=300)


with colToOrder:
    id_product = product_selected["id_prod"]
    shopping_cart_id = None 

    if "id_user" in st.session_state:
        id_user = st.session_state["id_user"]
        submit_buy = st.button("Ajouter au panier")
        if submit_buy:
            shopping_cart_id = control.user_open_shopping_cart_id(id_user)  # user_id ==> id_shopping_cart
            if shopping_cart_id:
                if not control.is_command_line_exist(shopping_cart_id, id_product):
                    vat = (product_selected["price_it"] - product_selected["price_ET"]) / product_selected["price_Et"]
                    control.add_new_command_line(id_product, shopping_cart_id, product_selected["price_ET"], vat)
            else: #shopping doesn't exist
                control.add_new_shoppingcart(id_user)
                shopping_cart_id = control.user_open_shopping_cart_id(id_user)  # user_id ==> id_shopping_cart
                vat = (product_selected["price_it"] - product_selected["price_ET"]) / product_selected["price_Et"]
                control.add_new_command_line(id_product, shopping_cart_id, product_selected["price_ET"], vat)
            st.switch_page("pages/4_Panier.py")

    

    # if shopping_cart_id:
    #     st.write(f"Il y a un shopping_cart_id : {shopping_cart_id}")

    #     result = control.commande_ver_panier(shopping_cart_id, id_product)
    #     if result:
    #         quantity = result[0].get("quantity", 0)
    #         if quantity > 0:
    #             st.write(f"🧺 Le produit est présent {quantity} fois dans votre panier.")
    #         else:
    #             st.write("🛒 Ce produit n'apparaît pas dans votre panier.")
    #     else:
    #         st.write("🛒 Ce produit n'apparaît pas dans votre panier.")
    # else:
    #     if st.button("Ajouter au panier"):
    #         st.write("Il n'y a pas de shopping_cart")
    #     st.write("Aucun panier ouvert pour cet utilisateur.")


        # quantity = control.commande_ver_panier(shopping_cart_id, id_product)[0]["quantity"] #product_selected["id_prod"])[0]["quantity"]
        # if quantity: 
        #     st.write(f"le produit apparait dans votre panier {quantity} fois")
        # else:
        #     st.write("le produite n'apparait pas dans votre commande")
   
    # control.commande_ver_panier(2, 13)[0]["quantity"]
    

    # if st.button("Ajouter au panier"):
    #     st.write("toto")
    #     st.write("dans votre panier : fois")

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
