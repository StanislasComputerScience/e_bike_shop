import os
import streamlit as st
import controller.controller as control


# --- function called on radio change ---
def changement_produit():
    st.session_state.c = name_products.index(st.session_state.choix_radio)


# radio button index initialisation
if "c" not in st.session_state:
    st.session_state.c = 0

# loading product
l_products = control.product_catalog()
# st.write(l)


# List of product's name for the radio button
name_products = [p["name"] for p in l_products]


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

# product selected
product_selected = l_products[st.session_state.c]

# principal display
st.subheader("Affichage du produit sélectionné :")
st.image(product_selected["image_path"], width=300)
st.write(product_selected["description"])
st.write(f"prix : {product_selected['price_it']}")
st.write(product_selected["tech_specification"])
