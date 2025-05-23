import os
import streamlit as st


# --- Fonction appelée quand le radio change ---
def changement_produit():
    st.session_state.c = noms_produits.index(st.session_state.choix_radio)


# Initialisation de l'index du bouton radio
if "c" not in st.session_state:
    st.session_state.c = 0

# Chargement des produits depuis le dossier
dossier = "./bdd/assets/products/"
l_produits = []

for i, f in enumerate(os.listdir(dossier)):
    chemin = os.path.join(dossier, f)
    if os.path.isfile(chemin):
        l_produits.append(
            {
                "nom": f"Produit_{i}",
                "description": f"Produit n°{i+1} : vélo performant pour usage quotidien.",
                "chemin_image": chemin,
            }
        )

# Liste des noms pour le bouton radio
noms_produits = [p["nom"] for p in l_produits]


# --- Affichage du menu latéral ---
st.sidebar.subheader("Fichiers dans 'produits' :")

st.sidebar.radio(
    "Sélectionnez un produit :",
    noms_produits,
    index=st.session_state.c,
    key="choix_radio",
    on_change=changement_produit,
)

# Boutons navigation
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    if st.button("Précédent"):
        st.session_state.c = (st.session_state.c - 1) % len(l_produits)

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
        st.session_state.c = (st.session_state.c + 1) % len(l_produits)

# Barre de progression
st.progress((st.session_state.c + 1) / len(l_produits))

# Produit sélectionné
produit_selectionne = l_produits[st.session_state.c]

# Affichage principal
st.subheader("Affichage du produit sélectionné :")
st.image(produit_selectionne["chemin_image"], width=300)
st.write(produit_selectionne["description"])
