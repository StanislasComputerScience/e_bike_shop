import controller as control
def load_products_and_c():
    # loading product
    l_products = control.product_catalog()
    # List of product's name for the radio button
    name_products = [p["name"] for p in l_products]
    if "c" not in st.session_state:
        st.session_state.c = 0
        st.session_state.c = name_products.index(st.session_state.choix_radio)
    return "toto"