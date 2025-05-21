import os
import streamlit as st

# Initialisation
if "c" not in st.session_state:
    st.session_state.c = 0

st.subheader("Produits les plus populaires :")

# Créer 2 colonnes
col1, col2 = st.columns(2)

with col1:
    st.image("./assets/Velo1.jpeg", caption="Vélo 1", use_container_width=True)

with col2:
    st.image("./assets/Velo2.jpeg", caption="Vélo 2", use_container_width=True)