import streamlit as st
import controller.controller as control
import os


def display():
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


def new_product():
    """Create a product"""
    # Formulary here
    st.write("Veuillez entrer les informations du nouveau produit.")

    with st.form("product_info"):
        name = st.text_input("🚴 Insérer le nom du produit")

        options = control.get_all_categories()
        # Choose actions to do
        with st.expander("🗂️ Choisissez votre catégorie"):
            choice_cat = st.radio("", options)

        number_of_units = st.text_input("📦 Insérer le stock du produit")
        description = st.text_area("📝 Insérer la description du produit")
        tech_specification = st.text_area(
            "⚙️ Insérer la description technique du produit"
        )
        price_ET = st.text_input("💰 Insérer le prix du produit")

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


def new_category():
    """Create a category"""
    # Formulary here
    st.write("Veuillez entrer les informations de la nouvelle catégorie.")

    with st.form("product_info"):
        name = st.text_input("🚴 Insérer le nom de la catégorie")
        submit_coo = st.form_submit_button("Valider")
        if submit_coo:
            if not name:
                st.error("Il manque une information pour créer le produit ❌")
            else:
                control.create_new_category(name)
                st.success("Catégorie créé ✅")


def new_vat():
    """Create a VAT"""
    # Formulary here
    st.write("Veuillez entrer les informations de la nouvelle TVA.")

    with st.form("product_info"):
        name = st.text_input("🚴 Insérer le nom de la TVA")
        number_of_units = st.text_input("💰 Insérer le taux pas en pourcentage")
        submit_coo = st.form_submit_button("Valider")
        if submit_coo:
            if not name:
                st.error("Il manque une information pour créer le produit ❌")
            else:
                control.create_new_vat(name)
                st.success("TVA créé ✅")


def new_role():
    """Create a role"""
    # Formulary here
    st.write("Veuillez entrer les informations du nouveau rôle.")

    with st.form("product_info"):
        name = st.text_input("🚴 Insérer le nom du rôle")
        submit_coo = st.form_submit_button("Valider")
        if submit_coo:
            if not name:
                st.error("Il manque une information pour créer le produit ❌")
            else:
                control.create_new_role(name)
                st.success("Rôle créé ✅")


if __name__ == "__main__":
    display()
