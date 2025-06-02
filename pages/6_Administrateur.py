import streamlit as st
import const_values as cv

if cv.BDD_TECHNO == "mongodb":
    import controller_mongod.controller_mongod as control
else:
    import controller.controller as control
    
import os


def display() -> None:
    """Main display"""
    try:
        if control.is_admin(st.session_state["id_user"]):
            st.title("Page admin du site")

            options = admin_action_possibilities()

            # Choose actions to do
            with st.expander("Choisissez une action"):
                choix_str = st.radio("", options)

            index_choix = options.index(choix_str)
            admin_actions(index_choix)
        else:
            st.write("Vous n'êtes pas un administrateur")
    except:
        st.write("Vous n'êtes pas un administrateur")


def admin_action_possibilities() -> list[str]:
    """Admin action possibilities

    Returns:
        list[str]: list of actions
    """
    admin_action = [
        "Créer un nouveau produit",
        "Créer une nouvelle catégorie",
        "Créer une nouvelle TVA",
        "Créer un nouveau rôle",
    ]
    return admin_action


def admin_actions(action_choice: int) -> None:
    """Define admin actions

    Args:
        action_choice (int): Number actions admin can do
    """
    if action_choice == 0:
        st.subheader("Nouveau produit")
        new_product()
    elif action_choice == 1:
        st.subheader("Nouvelle catégorie")
        new_category()
    elif action_choice == 2:
        st.subheader("Nouvelle TVA")
        new_vat()
    elif action_choice == 3:
        st.subheader("Nouveau rôle")
        new_role()


def new_product() -> None:
    """Create a product"""
    # Formulary here
    st.write("Veuillez entrer les informations du nouveau produit.")

    with st.form("product_info"):
        name = st.text_input("🚴 Insérer le nom du produit")

        options = control.get_all_categories()
        # Choose actions to do
        with st.expander("🗂️ Choisissez votre catégorie"):
            choice_cat = st.radio("", options)

        number_of_units = st.number_input(
            "📦 Insérer le stock du produit", min_value=0, format="%d"
        )
        description = st.text_area("📝 Insérer la description du produit")
        tech_specification = st.text_area(
            "⚙️ Insérer la description technique du produit"
        )
        price_ET = st.number_input("💰 Insérer le prix du produit", min_value=0.00)

        options = control.get_all_VAT()
        # Choose actions to do
        with st.expander("🧾 Choisissez votre TVA"):
            choice_vat = st.radio("", options)
        uploaded_file = st.file_uploader(
            "📷 Insérer l'image du produit",
            type=["jpg", "jpeg"],
        )
        submit_coo = st.form_submit_button("Valider")
        if submit_coo:
            if not control.is_product_allready_in_base(name):
                if (
                    not name
                    or not number_of_units
                    or not description
                    or not tech_specification
                    or not price_ET
                    or uploaded_file is None
                ):
                    st.error("Il manque une information pour créer le produit ❌")
                else:
                    file_path = os.path.join("bdd/assets/products", uploaded_file.name)
                    control.create_new_product(
                        name,
                        choice_cat,
                        number_of_units,
                        description,
                        tech_specification,
                        price_ET,
                        choice_vat,
                        file_path,
                    )
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    st.success("Produit créé ✅")
                    display_products()
            else:
                st.error("Le produit existe déjà ❌")


def display_products() -> None:
    """Display list of all products"""
    st.subheader("Produits :")
    for product in control.get_all_products():
        st.write(product)


def new_category() -> None:
    """Create a category"""
    # Formulary here
    st.write("Veuillez entrer les informations de la nouvelle catégorie.")

    with st.form("product_info"):
        name = st.text_input("🚴 Insérer le nom de la catégorie")
        submit_coo = st.form_submit_button("Valider")
        if submit_coo:
            if not control.is_category_allready_in_base(name):
                if not name:
                    st.error("Il manque une information pour créer le produit ❌")
                else:
                    control.create_new_category(name)
                    st.success("Catégorie créé ✅")
                    display_category()
            else:
                st.error("La catégorie existe déjà ❌")


def display_category() -> None:
    """Display list of all category"""
    st.subheader("Category :")
    for category in control.get_all_categories():
        st.write(category)


def new_vat() -> None:
    """Create a VAT"""
    # Formulary here
    st.write("Veuillez entrer les informations de la nouvelle TVA.")

    with st.form("product_info"):
        name = st.text_input("🚴 Insérer le nom de la TVA")
        rate = st.number_input("💰 Insérer le taux pas en pourcentage", min_value=0.00)
        submit_coo = st.form_submit_button("Valider")
        if submit_coo:
            if not control.is_vat_allready_in_base(name):
                if not name:
                    st.error("Il manque une information pour créer le produit ❌")
                else:
                    control.create_new_vat(name, rate)
                    st.success("TVA créé ✅")
                    display_vat()

            else:
                st.error("La TVA existe déjà ❌")


def display_vat() -> None:
    """Display list of all VAT"""
    st.subheader("TVA :")
    for vat in control.get_all_VAT():
        st.write(vat)


def new_role() -> None:
    """Create a role"""
    # Formulary here
    st.write("Veuillez entrer les informations du nouveau rôle.")

    with st.form("product_info"):
        name = st.text_input("🚴 Insérer le nom du rôle")
        submit_coo = st.form_submit_button("Valider")
        if submit_coo:
            if not control.is_role_allready_in_base(name):
                if not name:
                    st.error("Il manque une information pour créer le produit ❌")
                else:
                    control.create_new_role(name)
                    st.success("Rôle créé ✅")
                    display_role()

            else:
                st.error("Le rôle existe déjà ❌")


def display_role() -> None:
    """Display list of all role"""
    st.subheader("Rôle :")
    for role in control.get_all_role():
        st.write(role)


if __name__ == "__main__":
    display()
